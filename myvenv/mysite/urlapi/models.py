from django.db import models


class Cat(models.Model):
    cat_id = models.AutoField(default = 1, primary_key = True)
    name = models.TextField()
    locate = models.TextField()
    character = models.TextField()
    preferences = models.TextField()


class Post(models.Model):
    post_id = models.IntegerField(),
    title = models.CharField(max_length = 1000),
    content = models.CharField(max_length = 1000),
    writer = models.CharField(max_length = 1000),
    creat_at = models.DateTimeField(),
    update_at = models.DateTimeField(),