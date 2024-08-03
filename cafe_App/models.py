from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField

# Create your models here.

userchoices = (
    (1, "Admin"),
    (2, "Employee"),
    (3, "Client"),
)


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['Phone_number', 'username']

    name = models.CharField(max_length=255, null=True, blank=True)
    user_type = models.IntegerField(default=1, choices=userchoices)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.username


class Staff(models.Model):
    staff_id = models.CharField(max_length=3, null=True, blank=True)
    staff_name = models.CharField(max_length=220, null=True, blank=True)
    staff_phonenum = models.CharField(max_length=13, null=True, blank=True)


class Food_items(models.Model):
    item_name = models.CharField(max_length=50, null=True, blank=True)
    item_id = models.IntegerField(unique=True,null=True, blank=True)
    description = models.CharField(max_length=225, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    price = models.DecimalField(decimal_places=2, max_digits=7, null=True, blank=True)


class Address(models.Model):
    address1 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(max_length=20, null=True, blank=True)


class Orders(models.Model):
    order_id = models.IntegerField(null=True, blank=True)
    staff_id = models.CharField(max_length=3, null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    item_id = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    order_time = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=7, null=True, blank=True)
    delivery_ENUM = ('Dine-in', 'Takeout', 'Delivery')
    add_id = models.IntegerField(null=True, blank=True)

