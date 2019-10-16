from django.contrib import admin
from .models import House

# Register your models here.
class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'points')
admin.site.register(House, HouseAdmin)