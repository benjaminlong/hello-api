from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)


class Warehouse(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=20)

    company = models.ForeignKey(
            Company, related_name="warehouses", on_delete=models.CASCADE)


class Location(models.Model):
    secteur = models.CharField(max_length=5)
    etagere = models.CharField(max_length=5)
    rayon = models.CharField(max_length=5)

    warehouse = models.ForeignKey(
            Warehouse, related_name='locations', on_delete=models.CASCADE)


