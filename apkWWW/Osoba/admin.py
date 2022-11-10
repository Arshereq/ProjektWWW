from django.contrib import admin
from .models import Osoba
from .models import Druzyna


# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'druzyna']
    list_filter = ('druzyna',)


admin.site.register(Osoba, PersonAdmin)
admin.site.register(Druzyna)
