from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    contact_number = models.CharField(max_length=12, null=True, blank=True)
    profile_pic = models.ImageField(blank=True, upload_to='articles_images/')

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
