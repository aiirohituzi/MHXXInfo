from django.db import models

class Request(models.Model):
    town = models.CharField(max_length=10)
    requestName = models.CharField(max_length=30)
    requestName_kr = models.CharField(max_length=30)
    condition = models.TextField()
    reward = models.TextField()