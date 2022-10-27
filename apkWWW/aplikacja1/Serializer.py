from rest_framework import serializers
from .models import Druzyna, Osoba, Miesiace


class OsobaSerializer(serializers.Serializer):

    # pole tylko do odczytu, tutaj dla id działa też autoincrement
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    surname = serializers.CharField(required=True)
    miesiac_urodzenia = serializers.ChoiceField(choices=Miesiace, default=Miesiace.Styczen)
    Druzyna = serializers.PrimaryKeyRelatedField(queryset=Druzyna.objects.all())

    # przesłonięcie metody create() z klasy serializers.Serializer
    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    # przesłonięcie metody update() z klasy serializers.Serializer
    def update(self, instance, validated_data):
        instance.name = validated_data.get('imie', instance.name)
        instance.surname = validated_data('nazwisko', instance.surname)
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