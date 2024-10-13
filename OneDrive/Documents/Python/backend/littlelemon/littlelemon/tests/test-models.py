from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def instance(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")

class MenuViewTest(TestCase):
    def setup(self):
        item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item2 = Menu.objects.create(title="IceCream", price=80, inventory=100)

        self.assertEqual(item1, "IceCream : 80")
        self.assertEqual(item2, "IceCream : 80")