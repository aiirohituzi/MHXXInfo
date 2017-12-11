from django.shortcuts import render
from django.http import HttpResponse
from quest.models import Quest
import json

def getQuest(request):
    data = []
    
    for q in Quest.objects.all():
        data.append({
            'id': q.id,
            'questName': q.questName,
            'rating': q.rating,
            'contents': q.contents,
            'questMap': q.questMap,
            'questTime': q.questTime,
            'condition_main': q.condition_main,
            'condition_sum': q.condition_sub,
            'down_payment': q.down_payment,
            'rewardMoney_main': q.rewardMoney_main,
            'rewardMoney_sub': q.rewardMoney_sub,
            'reward_main': q.reward_main,
            'reward_sub': q.reward_sub,
        })

    print("Get - Quest data")
    data = json.dumps(data, indent=4)
    print(data)
    
    return HttpResponse(data, content_type = "application/json")