from rest_framework import serializers
from .models import Druzyna, Osoba, Miesiace
from datetime import date
from django.contrib.auth.models import User


class OsobaSerializer(serializers.Serializer):
    # pole tylko do odczytu, tutaj dla id działa też autoincrement
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)
    miesiac_urodzenia = serializers.ChoiceField(choices=Miesiace, default=Miesiace)
    data_dodania = serializers.DateField()
    druzyna = serializers.PrimaryKeyRelatedField(queryset=Druzyna.objects.all())

    def validate(self, data):
        if not data['imie'].isalpha():
            raise serializers.ValidationError("Imie nie moze zawierać cyfr!!!")
        if data['data_dodania'] > date.today():
            raise serializers.ValidationError("Halo halo pan z przeszłości ??")
        return data

    # przesłonięcie metody create() z klasy serializers.Serializer
    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    # przesłonięcie metody update() z klasy serializers.Serializer
    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data('nazwisko', instance.nazwisko)
        instance.druzyna = validated_data.get('druzyna', instance.druzyna)
        instance.save()
        return instance


class DruzynaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nazwa = serializers.CharField(required=True)
    kraj = serializers.CharField(required=True)

    def create(self, validated_data):
        return Druzyna.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.kraj = validated_data.get('kraj', instance.kraj)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    osoba = serializers.PrimaryKeyRelatedField(many=True, queryset=Osoba.objects.all())
    osoba = serializers.ReadOnlyField(source='wlasciciel.Nazwa')

    class Meta:
        model = User
        fields = ['id', 'Nazwa', 'Osoba']
