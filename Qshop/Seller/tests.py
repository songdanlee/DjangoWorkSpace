from django.test import TestCase

# Create your tests here.
from Buyer.models import *


class OurTest(TestCase):

    def setUp(self) -> None:
        pass


    def test_insert(self):
        self.assertEqual("萝卜","萝卜")

    def tearDown(self) -> None:
        pass

