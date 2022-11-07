from rest_framework import serializers
from .models import Druzyna, Osoba, Miesiace
from datetime import date


class OsobaSerializer(serializers.Serializer):

    # pole tylko do odczytu, tutaj dla id działa też autoincrement
    id = serializers.IntegerField(read_only=True)
    Imie = serializers.CharField(required=True)
    Nazwisko = serializers.CharField(required=True)
    miesiac_urodzenia = serializers.ChoiceField(choices=Miesiace, default=Miesiace)
    data_dodania = serializers.DateField()
    Druzyna = serializers.PrimaryKeyRelatedField(queryset=Druzyna.objects.all())

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
        instance.Imie = validated_data.get('imie', instance.Imie)
        instance.Nazwisko = validated_data('nazwisko', instance.Nazwisko)
        instance.Druzyna = validated_data.get('druzyna', instance.Druzyna)
        instance.save()
        return instance
class DruzynaSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    nazwa=serializers.CharField(required=True)
    kraj=serializers.CharField(required=True)

    def create(self, validated_data):
        return Druzyna.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa',instance.nazwa)
        instance.kraj = validated_data.get('kraj',instance.kraj)
        instance.save()
        return instance