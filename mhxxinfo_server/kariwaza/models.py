from django.db import models


class Kariwaza(models.Model):
    category = models.CharField(max_length=20)
    kariwazaName = models.CharField(max_length=50)
    level = models.CharField(max_length=5)
    condition = models.CharField(max_length=100)