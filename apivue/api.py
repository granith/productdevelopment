from rest_framework import viewsets, permissions

from .models import RiskFields, RiskTypes, FieldTypes
from .serializers import RiskFieldsSerializer, RiskTypesSerializer, FieldTypesSerializer


class RiskFieldsViewSet(viewsets.ModelViewSet):
    queryset = RiskFields.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = RiskFieldsSerializer

class RiskTypesViewSet(viewsets.ModelViewSet):
    queryset = RiskTypes.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = RiskTypesSerializer

class FieldsTypeViewSet(viewsets.ModelViewSet):
    queryset = FieldTypes.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = FieldTypesSerializer
