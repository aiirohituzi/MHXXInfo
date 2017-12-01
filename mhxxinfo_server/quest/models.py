from django.db import models

# Create your models here.
class Quest(models.Model):
    questName = models.CharField(max_length=30)

    rating = models.CharField(max_length=8, null=True)
    contents = models.CharField(max_length=200, null=True)
    condition = models.CharField(max_length=50, null=True)
    reward = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.questName