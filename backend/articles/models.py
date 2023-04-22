from django.db import models

from core.models import TimeStampModel
from users.models import User


class Blog(TimeStampModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class Article(TimeStampModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles_images/', null=True, blank=True)

    def __str__(self):
        return self.title

