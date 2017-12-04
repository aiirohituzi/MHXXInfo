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
            'condition': q.condition,
            'reward': q.reward,
        })

    print("Get - Quest data")
    data = json.dumps(data, indent=4)
    print(data)
    
    return HttpResponse(data, content_type = "application/json")