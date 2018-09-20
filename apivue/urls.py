from django.conf.urls import url, include
from rest_framework import routers,viewsets, permissions
from .api import RiskFieldsViewSet, RiskTypesViewSet, FieldsTypeViewSet

router = routers.DefaultRouter()
router.register('riskfields', RiskFieldsViewSet)
router.register('risktypes', RiskTypesViewSet)
router.register('fieldtypes', FieldsTypeViewSet)

urlpatterns = [
    url('^', include(router.urls)),
]
