from django.contrib import admin
from .models import Vendor, Capacitor, Resistor

# Register your models here.
admin.site.register(Vendor)
admin.site.register(Resistor)
admin.site.register(Capacitor)
