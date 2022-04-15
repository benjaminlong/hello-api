import uuid
from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=128)


class Model(models.Model):
    name = models.CharField(max_length=64)

    brand = models.ForeignKey(
            Brand, null=True, blank=True, on_delete=models.SET_NULL)


class Reference(models.Model):
    url = models.URLField(null=True, blank=True)

    model = models.ForeignKey(
            Model, related_name="references", on_delete=models.CASCADE)


class Item(models.Model):
    serial_number = models.CharField(max_length=64, null=True, blank=True)

    reference = models.ForeignKey(
            Reference, null=True, blank=True, on_delete=models.SET_NULL)
    location = models.ForeignKey(
            "stock.Location", null=True, blank=True, on_delete=models.SET_NULL)



class Picture(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    file = models.FileField()

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
