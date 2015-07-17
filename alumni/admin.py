from django.contrib import admin

from .models import Name

class NameAdmin(admin.ModelAdmin):
    fields = ['address_text', 'lat', 'lon']
    list_display = ('name_text', 'address_text', 'lat', 'lon')

admin.site.register(Name, NameAdmin)
