from django.urls import path
from backend import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", view=views.home, name="hello"),
    path("hello_there/<name>", view=views.hello_there, name="hello_there"),
    path("getAllVendors/", view=views.getAllVendors, name="getAll_vendors"),
]
