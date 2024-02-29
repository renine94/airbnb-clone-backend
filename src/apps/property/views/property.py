from rest_framework.response import Response
from rest_framework import generics

from ..models import Property
from ..serializers import PropertiesListSerializer


class PropertyListAPI(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertiesListSerializer
    authentication_classes = []
    permission_classes = []
