from django.db import models

# Create your models here.
# kod z oficjalnej dokumentacji Django
class Druzyna(models.Model):
    nazwa = models.CharField(max_length=60, blank=False)
    kraj = models.CharField(max_length=2)
    class Meta:
        ordering=['nazwa']

    def __str__(self):
        return f'{self.nazwsasa} ({self.kraj})'
class Osoba(models.Model):
    name = models.CharField(max_length=60, blank=False)
    surname = models.CharField(max_length=60, blank=False)
    class Miesiace(models.IntegerChoices):
        Styczen = 1
        Luty = 2
        Marzec =3
        Kwiecien = 4
        Maj = 5
        Czerwiec = 6
        Lipiec = 7
        Sierpien =8
        Wrzesien =9
        Pazdziernik =10
        Listopad =11
        Grudzien = 12
    #NIE DZIALA TA WERSJA
    #miesiac = models.IntegerChoices('miesiac','Styczeń Luty Marzec Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')
    #miesiac.choices
    #miesiac_urodzenia = models.CharField(max_length=60, choices=Miesiace)
    miesiac_urodzenia = models.IntegerField(choices=Miesiace.choices)
    data_dodania = models.DateField(auto_now=True)
    Druzyna = models.ForeignKey(Druzyna,on_delete=models.SET_NULL,null=True)
    class Meta:
        ordering=['surname']

    def __str__(self):
        return (self.name+' '+self.surname)

