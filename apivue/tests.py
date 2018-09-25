import json
from django.test import TestCase
from .models import RiskTypes
from django.urls import reverse
from rest_framework.test import APITestCase

# Create your tests here.

class RiskTypesAPIViewTestCase(APITestCase):
    url = 'http://127.0.0.1:8000/api/risktypes/'

    def test_risk_types(self):
        """
        Test to verify that a post call with risk types
        """
        risk_data = {
            "name": "New",
        }
        response = self.client.post(self.url, risk_data)
        self.assertEqual(201, response.status_code)
