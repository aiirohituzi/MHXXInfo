from django.db import models

# Create your models here.
class Quest(models.Model):
    questName = models.CharField(max_length=30)

    rating = models.CharField(max_length=8)
    contents = models.CharField(max_length=200, null=True)
    questMap = models.CharField(max_length=10)
    questTime = models.CharField(max_length=5)

    condition_main = models.CharField(max_length=50)
    condition_sub = models.CharField(max_length=50, null=True)

    down_payment = models.IntegerField()

    rewardMoney_main = models.IntegerField()
    rewardMoney_sub = models.IntegerField()

    reward_main = models.CharField(max_length=300, null=True)
    reward_sub = models.CharField(max_length=300)

    def __str__(self):
        return self.questName