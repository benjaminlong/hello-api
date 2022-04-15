from django.contrib import admin

from hello_api.stock.models import Location

# Register your models here.

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
