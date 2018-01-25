from django.db import models

# Create your models here.
class Quest(models.Model):
    questName = models.CharField(max_length=30)
    questName_kr = models.CharField(max_length=30)

    rating = models.CharField(max_length=8)
    contents = models.CharField(max_length=200, null=True)
    questMap = models.CharField(max_length=10)
    questTime = models.CharField(max_length=5)

    condition_main = models.CharField(max_length=50)
    condition_sub = models.CharField(max_length=50, null=True)

    down_payment = models.CharField(max_length=7)

    rewardMoney_main = models.CharField(max_length=7)
    rewardMoney_sub = models.CharField(max_length=7, null=True)

    reward_main = models.CharField(max_length=300)
    reward_sub = models.CharField(max_length=300, null=True)

    keyQuest = models.CharField(max_length=1, default='0')
    precedingQuestId = models.CharField(max_length=5, default='0')

    def __str__(self):
        return self.questName

    

class Request(models.Model):
    requestName = models.CharField(max_length=30)
    requestName_kr = models.CharField(max_length=30)
    condition = models.CharField(max_length=50)
    reward = models.CharField(max_length=100)



class Kariwaza(models.Model):
    category = models.CharField(max_length=20)
    kariwazaName = models.CharField(max_length=50)
    level = models.CharField(max_length=5)
    condition = models.CharField(max_length=100)