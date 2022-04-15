from django.contrib import admin

from hello_api.items.models import Item, Reference, Brand


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass
