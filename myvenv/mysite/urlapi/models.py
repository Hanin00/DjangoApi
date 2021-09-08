from django.db import models


class Cat(models.Model):
    cat_id = models.AutoField(default = 1, primary_key = True)
    name = models.TextField()
    locate = models.TextField()
    character = models.TextField()
    preferences = models.TextField()
