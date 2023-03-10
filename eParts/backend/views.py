import re
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .seralizer import VendorSerializer
from .models import Vendor

# Create your views here.


def home(request):
    return HttpResponse("Hello eParts!")


def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A %d %B, %Y, at %X")

    match_object = re.match("[a-zA-Z]+", name)
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = f"Hello there {clean_name} {formatted_now}"

    return HttpResponse(content=content)


@api_view(["GET"])
def getAllVendors(request):
    vendors = queryset = Vendor.objects.all().order_by("id")
    serializer = VendorSerializer(queryset, many=True)
    return Response({"vendors": serializer.data})
