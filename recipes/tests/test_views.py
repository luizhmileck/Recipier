from django.test import TestCase, Client
from recipes.models import Recipe


class TestViwes(TestCase):

    def test_recipes_list_get(self):
        response = client.get()
