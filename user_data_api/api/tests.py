from django.test import TestCase
from .models import UserDataModel
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status


class ModelTestCase(TestCase):

    def setUp(self):
        self.userdata_name = 'test user data'
        self.userdata = UserDataModel(name=self.userdata_name)

    def test_model_can_create_userdata(self):
        old_count = UserDataModel.objects.count()
        self.userdata.save()
        new_count = UserDataModel.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.userdata = {'name': 'abc'}
        self.response = self.client.post(
            reverse('create'),
            self.userdata,
            format='json'
        )

    def test_api_can_create_userdata(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

