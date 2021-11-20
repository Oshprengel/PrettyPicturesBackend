from django.urls import path
from . import views

urlpatterns = [
  path("", views.home),
  path("locations",views.locations),
  path("locations/<str:location>/",views.pictures)
]