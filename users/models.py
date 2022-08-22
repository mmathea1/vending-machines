from django.db import models

# Create your models here.


class User(models.Model):
    code = models.CharField(max_length=4, blank=False, null=False)
