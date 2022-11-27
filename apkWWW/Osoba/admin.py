from django.contrib import admin
from .models import Osoba
from .models import Druzyna
from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'druzyna']
    list_filter = ('druzyna',)


admin.site.register(Osoba, PersonAdmin)
admin.site.register(Druzyna)

TokenAdmin.raw_id_fields=['user']
