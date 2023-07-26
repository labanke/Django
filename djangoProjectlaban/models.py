# responsible for making tables in the database
# The class should be typed singular but will appear plural in database

from django.db import models


class People(models.Model):
    name = models.CharField(max_length=30, blank=False)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=30, blank=False, null=False)


def __str__(self):
    return self.name
