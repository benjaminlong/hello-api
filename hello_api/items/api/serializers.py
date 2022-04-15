from rest_framework import serializers

from hello_api.items.models import Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ["pk", "serial_number", "reference"]
