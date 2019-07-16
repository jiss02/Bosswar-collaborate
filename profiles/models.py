from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    email = models.EmailField(null=True) 
    tel = PhoneNumberField(unique=True)
    point = models.IntegerField(default=500)

    def __str__(self):
        return self.user