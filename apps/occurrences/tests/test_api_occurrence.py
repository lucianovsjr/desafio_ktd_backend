from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.occurrences.models import Status, Road

URL_OCCURRENCE = reverse('occurrence-list')
URL_STATUS = reverse('status-list')
URL_ROAD = reverse('road-list')


def concat_url(url, pk):
    return ''.join((url, str(pk), '/'))


class OccurrenceCreateApiTest(APITestCase):
    def setUp(self):
        User.objects.create_superuser(username='desafio', password='desafio')

        _status = Status.objects.create(name='Fazendo', color_hex='#00ff00')
        _road = Road.objects.create(name='BR-040', uf_code='41', length=1179)

        self.status_url = concat_url(URL_STATUS, _status.pk)
        self.road_url = concat_url(URL_ROAD, _road.pk)

        self.client.login(username="desafio", password="desafio")

    def test_create(self):
        data = {"description": "Quiquia modi etincidunt modi.",
                "road": self.road_url, "km": "65", "status": self.status_url}
        resp = self.client.post(URL_OCCURRENCE, data)

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        with self.subTest():
            for key, value in data.items():
                if key in ('road', 'status'):
                    self.assertIn(value, resp.data[key])
                else:
                    self.assertEqual(resp.data[key], value)


class OccurrenceApiTest(APITestCase):
    def setUp(self):
        User.objects.create_superuser(username='desafio', password='desafio')

        _status = Status.objects.create(name='Fazendo', color_hex='#00ff00')
        _road = Road.objects.create(name='BR-040', uf_code='41', length=1179)

        self.client.login(username="desafio", password="desafio")

        self.data = {"description": "Quiquia modi etincidunt modi.",
                     "km": "65", "road": concat_url(URL_ROAD, _road.pk),
                     "status": concat_url(URL_STATUS, _status.pk)}
        self.client.post(URL_OCCURRENCE, self.data)
        self.occurrence_url = concat_url(URL_OCCURRENCE, 1)

    def test_get(self):
        resp = self.client.get(self.occurrence_url)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        with self.subTest():
            for key, value in self.data.items():
                if key in ('road', 'status'):
                    self.assertIn(value, resp.data[key])
                else:
                    self.assertEqual(resp.data[key], value)

    def test_update(self):
        _status = Status.objects.create(name='Feito', color_hex='#0000ff')
        _road = Road.objects.create(name='BR-116', uf_code='41', length=230)
        data = {"description": "Labore numquam adipisci quisquam ipsum.",
                "km": "65", "road": concat_url(URL_ROAD, _road.pk),
                "status": concat_url(URL_STATUS, _status.pk)}

        resp = self.client.put(self.occurrence_url, data)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        with self.subTest():
            for key, value in data.items():
                if key in ('road', 'status'):
                    self.assertIn(value, resp.data[key])
                else:
                    self.assertEqual(resp.data[key], value)

    def test_delete(self):
        resp = self.client.delete(self.occurrence_url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)

        resp = self.client.get(self.occurrence_url)
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)


class OccurrenceUnAuthenticatedApiTest(APITestCase):
    def setUp(self):
        self._status = Status.objects.create(name='Fazendo', color_hex='#00ff00')
        self._road = Road.objects.create(name='BR-040', uf_code='41', length=1179)
        self.data = {"description": "Quiquia modi etincidunt modi.",
                     "km": "65", "road": concat_url(URL_ROAD, self._road.pk),
                     "status": concat_url(URL_STATUS, self._status.pk)}

        self.occurrence_url = concat_url(URL_OCCURRENCE, 1)

    def test_create(self):
        resp = self.client.post(URL_OCCURRENCE, self.data)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_get(self):
        resp = self.client.get(self.occurrence_url)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_put(self):
        resp = self.client.put(self.occurrence_url)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete(self):
        resp = self.client.delete(self.occurrence_url)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
