from django.db import models


class Recruitment(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=32)
    introduction = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=32)
    field = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    exp_year = models.DecimalField(decimal_places=2, max_digits=5)
    cv = models.FileField(upload_to='uploads/')
