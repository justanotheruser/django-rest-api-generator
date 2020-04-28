import json
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from player.models import Artist, Album, Track


class ArtistTestCase(TestCase):

    def setUpTestData():
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

    def setUp(self):
        Artist.objects.create(name='Metallica')
        Artist.objects.create(name='Weezer')

    def test_list(self):
        response = APIClient().get('/artist/')
        self.assertEqual(json.loads(response.content), [
                         {'pk': 1, 'name': 'Metallica'}, {'pk': 2, 'name': 'Weezer'}])

    def test_retrieve(self):
        response = APIClient().get('/artist/1/')
        self.assertEqual(json.loads(response.content), {
                         'pk': 1, 'name': 'Metallica'})
        response = APIClient().get('/artist/2/')
        self.assertEqual(json.loads(response.content),
                         {'pk': 2, 'name': 'Weezer'})

    def test_post(self):
        response = APIClient().post('/artist/', {'name': 'The Strokes'})
        self.assertEqual(response.status_code, 201)

    def test_delete(self):
        response = APIClient().delete('/artist/1/')
        self.assertEqual(response.status_code, 204)

    def test_put(self):
        response = APIClient().post('/artist/', {'name': 'Strokes'})
        self.assertEqual(response.status_code, 201)
        response = APIClient().put('/artist/3/', {'name': 'The Strokes'})
        self.assertEqual(response.status_code, 200)