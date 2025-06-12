from django.db import models


class Beans(models.Model):
    name = models.CharField(max_length=200)
    roster = models.CharField(max_length=200)
    roast = models.CharField(max_length=20, null=True)
    origin = models.CharField(max_length=100)
    price = models.FloatField()
    rating = models.IntegerField()
    review = models.TextField()