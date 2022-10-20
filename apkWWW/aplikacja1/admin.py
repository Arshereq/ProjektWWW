from django.contrib import admin
from .models import Osoba
from .models import Druzyna
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'Druzyna']
    list_filter = ('Druzyna',)


admin.site.register(Osoba,PersonAdmin)
admin.site.register(Druzyna)


