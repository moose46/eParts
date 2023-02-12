from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Vendor(models.Model):
    company_name = models.CharField(max_length=100, null=False, blank=False)
    web_site = models.CharField(max_length=128, name="Web Site", null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, name="Phone Number", blank=True)
    createdAt = models.DateTimeField(auto_now=True)

    updatedAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["company_name"]


class Tolerance(models.TextChoices):
    OnePercent = "1%"
    FivePercent = "5%"
    TenPercent = "10%"
    TwentyPercent = "20%"
    GreaterThanTwentyPercent = "> 20%"


class Composition(models.TextChoices):
    MetalFilm = "Metal Film"
    Carbon = "Carbon"
    WireWound = "Wire Wound"
    Ceramic = "Ceramic"
    Power = "Power Resistor"


class part(models.Model):
    createdAt = models.DateTimeField(auto_now=True)
    in_stock = models.IntegerField(
        name="# In Stock", null=False, default=0, blank=False
    )
    updatedAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    part_number = models.CharField(
        name="Part or Stock#", blank=True, null=True, max_length=32
    )
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        ordering = ["vendor"]


class Resistor(part):
    tolerance = models.CharField(
        max_length=32, choices=Tolerance.choices, default=Tolerance.FivePercent
    )
    value = models.IntegerField(null=False, blank=False, name="Ohms")
    composition = models.CharField(
        max_length=32, choices=Composition.choices, default=Composition.Carbon
    )
    wattage = models.IntegerField(name="Watts", blank=False, null=False)


class Capacitor(part):
    value = models.IntegerField(null=False, blank=False, default=0, name="Mfd")
    # class Meta:
    #     ordering = ["vendor"]
