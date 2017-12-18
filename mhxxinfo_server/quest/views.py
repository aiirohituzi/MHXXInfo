from django.shortcuts import render
from django.http import HttpResponse
from quest.models import Quest
import json

def getQuestList(request):
    data = []
    rating = request.GET.get('rating', False)
    # print(rating)
    
    if not rating:
        return HttpResponse('False')

    for q in Quest.objects.filter(rating=rating):
        data.append({
            'id': q.id,
            'questName': q.questName,
            'questName_kr': q.questName_kr,
            'rating': q.rating,
            'questMap': q.questMap,
            'condition_main': q.condition_main,
        })

    print("Get - Quest List")
    data = json.dumps(data, indent=4)
    print(data)
    
    return HttpResponse(data, content_type = "application/json")



def getQuest(request):
    data = []
    questId = request.GET.get('id', False)

    if not questId:
        return HttpResponse('False')

    for q in Quest.objects.filter(id=questId):
        data.append({
            'id': q.id,
            'questName': q.questName,
            'questName_kr': q.questName_kr,
            'rating': q.rating,
            'contents': q.contents,
            'questMap': q.questMap,
            'questTime': q.questTime,
            'condition_main': q.condition_main,
            'condition_sub': q.condition_sub,
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