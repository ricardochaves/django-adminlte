from django.test import TestCase

from django.forms.boundfield import BoundField
from django.forms import Widget

from .templatetags.extra_functions import add_class

# Create your tests here.


class ExtraFunciontionsTests(TestCase):

    def teste_add_class(self):
        field = Widget()
        add_class(field, "teste")
        self.assertEqual('', 'Ricardo')
