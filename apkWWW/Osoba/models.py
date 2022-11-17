from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.
# kod z oficjalnej dokumentacji Django
class Druzyna(models.Model):
    nazwa = models.CharField(max_length=60, blank=False)
    kraj = models.CharField(max_length=2)
    class Meta:
        ordering=['nazwa']

    def __str__(self):
        return f'{self.nazwa} ({self.kraj})'
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
class Osoba(models.Model):
    imie = models.CharField(max_length=60, blank=False)
    nazwisko = models.CharField(max_length=60, blank=False)

    #NIE DZIALA TA WERSJA
    #miesiac = models.IntegerChoices('miesiac','Styczeń Luty Marzec Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')
    #miesiac.choices
    #miesiac_urodzenia = models.CharField(max_length=60, choices=Miesiace)

    miesiac_urodzenia = models.IntegerField(choices=Miesiace.choices)
    data_dodania = models.DateField(auto_now=True)
    druzyna = models.ForeignKey(Druzyna, on_delete=models.SET_NULL, null=True)

    owner = models.ForeignKey('auth.User', null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['nazwisko']

    def __str__(self):
        return (self.imie +' ' + self.nazwisko)



