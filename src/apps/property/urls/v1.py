from django.urls import path

from .. import views

urlpatterns = [
    path("property/", views.PropertyListAPI.as_view(), name="property-list"),
]
