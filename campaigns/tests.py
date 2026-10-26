from rest_framework.test import APITestCase
from rest_framework import status


# Create your tests here.
class TestReportCampagna(APITestCase):
    def test_campagna_inesistente(self):
        risposta = self.client.get("/api/campagne/999/report/")  # Ritorna oggetto Response

        self.assertEqual(
            risposta.status_code,
            status.HTTP_404_NOT_FOUND
        )