from django.db import models


class Cat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    locate = models.TextField()
    character = models.TextField()
    preferences = models.TextField()

