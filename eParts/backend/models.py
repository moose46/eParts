from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class base(models.Model):
    createdAt = models.DateTimeField("date created", auto_now=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    updatedAt = models.DateTimeField("date last updated", auto_now_add=True, null=False)
    description = models.CharField(
        "description", max_length=128, blank=True, null=False, default="N/A"
    )

    class Meta:
        abstract = True


class Vendor(base):
    company_name = models.CharField(
        "company name", max_length=100, null=False, blank=False
    )
    email = models.CharField(
        max_length=32, blank=False, null=False, default="none@none.com"
    )
    web_site = models.CharField(max_length=128, null=True, blank=True, default="")
    phone = models.CharField(max_length=32, null=True, name="Phone Number", blank=True)
    street = models.CharField(max_length=64, null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    state = models.CharField(max_length=64, null=True, blank=True)
    country = models.CharField(max_length=64, null=True, blank=True)
    zip = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.company_name

    class Meta:
        ordering = ["company_name"]


class Tolerance(models.TextChoices):
    OnePercent = "1%"
    FivePercent = "5%"
    TenPercent = "10%"
    TwentyPercent = "20%"
    GreaterThanTwentyPercent = "> 20%"


class ResistorType(models.TextChoices):
    MetalFilm = "Metal Film"
    Carbon = "Carbon"
    WireWound = "Wire Wound"
    Ceramic = "Ceramic"
    Power = "Power Resistor"


class CapacitorType(models.TextChoices):
    Electrolytic = "Electrolytic"
    Polymer = "Polymer"
    Mica = "Mica"
    OrangeDrop = "Orange Drop"


class PartType(base):
    description = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ["description"]


class Part(base):
    part_number = models.CharField(
        name="Part or Stock#", blank=True, null=True, max_length=32
    )
    in_stock = models.IntegerField(
        name="# In Stock", null=False, default=0, blank=False
    )
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    part_id = models.ForeignKey(PartType, on_delete=models.CASCADE, name="Part Type")

    class Meta:
        # abstract = True
        ordering = ["vendor"]


class Resistor(Part, base):
    tolerance = models.CharField(
        "resistor tolerance",
        max_length=32,
        choices=Tolerance.choices,
        default=Tolerance.FivePercent,
    )
    ohms = models.IntegerField(null=False, blank=False, name="Ohms")
    resistor_type = models.CharField(
        "composition",
        max_length=32,
        choices=ResistorType.choices,
        default=ResistorType.Carbon,
    )
    wattage = models.FloatField(name="Watts", blank=False, null=False)


class FormFactors(models.TextChoices):
    Axial = "Axial"
    Radial = "Radial"
    Can = "Can"


class Capacitor(Part, base):
    mfd = models.FloatField(null=False, blank=False, default=0, name="Mfd")
    composition = models.CharField(
        max_length=32,
        name="Composition",
        choices=CapacitorType.choices,
        null=False,
        blank=False,
        default=CapacitorType.Polymer,
    )
    voltage = models.IntegerField(name="Voltage Rating", blank=False, null=False)
    axial_radial = models.CharField(
        "capacitor form factor",
        max_length=32,
        choices=FormFactors.choices,
        null=False,
        default=FormFactors.Axial,
    )
    # class Meta:
    #     ordering = ["vendor"]
