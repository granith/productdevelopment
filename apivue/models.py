from django.db import models


class RiskTypes(models.Model):
    name = models.CharField("Name", max_length=255)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.name

class FieldTypes(models.Model):
    FIELD_TYPES = (
        ("Text", 'text'),
        ("Number", 'number'),
        ("Date", 'date'),
        ("enum", 'enum'),
    )
    field_name = models.CharField("Field Name", max_length=30)
    type = models.CharField(max_length=1, choices=FIELD_TYPES)

    def __str__(self):
        return self.field_name

class RiskFields(models.Model):
    risks = models.ForeignKey(RiskTypes, on_delete=models.CASCADE,null=True)
    field_types = models.ManyToManyField(FieldTypes)
    depth = 1

    def __str__(self):
        return self.risks.name
