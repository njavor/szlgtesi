from django.contrib import admin

from jelenletiv.models import Alkalom, Foglalkozas, Osztaly, Tanulo

admin.site.register(Alkalom)
admin.site.register(Foglalkozas)
admin.site.register(Tanulo)
admin.site.register(Osztaly)
