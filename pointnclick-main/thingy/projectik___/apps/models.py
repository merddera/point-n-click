from django.db import models


# Create your models here.


class CommentFor(models.Model):
    comments = models.CharField(default="", max_length=500)
    related = models.CharField(default="", max_length=80)
