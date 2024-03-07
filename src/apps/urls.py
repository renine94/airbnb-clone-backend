from django.urls import include
from django.urls import path

urlpatterns = [
    path("auth/", include("src.apps.accounts.urls.auth")),
    # path("v1/", include("src.apps.accounts.urls.v1")),
    path("v1/", include("src.apps.property.urls.v1")),
    # path("v2/", include("src.apps.accounts.urls.v2")),
    # path("v2/", include("src.apps.property.urls.v2")),
]
