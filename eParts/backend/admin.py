from django.contrib import admin
from .models import Vendor, PartType, Part, Storage


class PartInline(admin.StackedInline):
    model = Part


class PartAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": [
                    # "vendor",
                    "part_type_id",
                    "vendor",
                    "part_number",
                    "description",
                    # "part_number",
                    "value",
                    "in_stock",
                    "storage_location_id",
                ]
            },
        ),
        # (
        #     "Vendors",
        #     {
        #         "fields": ["vendor"],
        #         "classes": ["collapse"],
        #     },
        # ),
    ]
    search_fields = ["part_number"]
    list_filter = ["vendor", "part_type_id"]
    inLines = [PartInline]


# Register your models here.
admin.site.register(Vendor)
admin.site.register(PartType)
admin.site.register(Part, PartAdmin)
admin.site.register(Storage)
# admin.site.register(Resistor)
# admin.site.register(Capacitor)
