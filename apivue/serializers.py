from rest_framework import serializers

from .models import RiskFields, RiskTypes, FieldTypes


class RiskFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskFields
        fields = ('risks', 'field_types')
        depth = 1

class RiskTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskTypes
        fields = ('name',)

class FieldTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldTypes
        fields = ('field_name', 'type',)
