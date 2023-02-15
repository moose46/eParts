from rest_framework import serializers
from .models import Vendor, Capacitor, Resistor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ["company_name", "web_site"]


class CapacitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capacitor
        fields = "__all__"


class ResistorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resistor
        fields = "__all__"
