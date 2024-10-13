from django.db import models

# Create your models here.
class Menu(models.Model):
    ID = models.IntegerField(5)
    Title = models.CharField(255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(5)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    ID = models.IntegerField(11)
    Name = models.CharField(255)
    No_of_guests = models.IntegerField(6)
    BookingDate = models.DateTimeField()