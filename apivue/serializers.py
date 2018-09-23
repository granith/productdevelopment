from rest_framework import serializers

from .models import RiskFields, RiskTypes, FieldTypes


class RiskTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskTypes
        fields = ('name',)

class FieldTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldTypes
        fields = ('field_name', 'type',)

class RiskFieldsSerializer(serializers.ModelSerializer):
    risks = RiskTypesSerializer()
    field_types = FieldTypesSerializer(many=True)

    class Meta:
        model = RiskFields
        fields = ('risks', 'field_types',)

    def create(self, validated_data):
        fields_data = validated_data.pop('field_types')
        fieldtyp = RiskFields.objects.create(**validated_data)
        for field_data in fields_data:
            FieldTypes.objects.create(field_name=fieldtyp, **field_data)
        return fieldtyp
