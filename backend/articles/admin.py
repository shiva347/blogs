from django.contrib import admin
from articles import models

admin.site.register(models.Blog)
admin.site.register(models.Article)


