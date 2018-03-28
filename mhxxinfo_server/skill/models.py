from django.db import models


class Skill(models.Model):
    skillType = models.CharField(max_length=30)
    skillName = models.TextField()
    point = models.TextField()
    effect = models.TextField()