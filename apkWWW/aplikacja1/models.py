from django.db import models

# Create your models here.
# kod z oficjalnej dokumentacji Django
class Osoba(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    Miesiace=(
        ('1','Styczeń'),
        ('2','Luty'),
        ('3','Marzec'),
        ('4','Kwiecień'),
        ('5','Maj'),
        ('6','Czerwiec'),
        ('7','Lipiec'),
        ('8','Sierpień'),
        ('9','Wrzesień'),
        ('10','Październik'),
        ('11','Listopad'),
        ('12','Grudzień'),
    )
    miesiac_urodzenia = models.CharField(max_length=60, choices=Miesiace)

