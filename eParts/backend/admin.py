from django.contrib import admin
from .models import Vendor, PartType, Part

# Register your models here.
admin.site.register(Vendor)
admin.site.register(PartType)
admin.site.register(Part)
# admin.site.register(Resistor)
# admin.site.register(Capacitor)
