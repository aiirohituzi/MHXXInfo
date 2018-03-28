from django.shortcuts import render
from django.http import HttpResponse

from quest.models import Quest
import json
from django.db.models import Q

def getAllSearch(request):
    data = []

    searchRange = request.GET.get('searchRange', False)
    keyword = request.GET.get('keyword', False)
    
    if not keyword:
        return HttpResponse(data, content_type = "application/json")

    if searchRange == 'all':
        for q in Quest.objects.filter(Q(questName__icontains=keyword) | Q(questName_kr__icontains=keyword)):
            data.append({
                'category': 'Quest',
                'id': q.id,
                'result': '퀘스트 : ' + q.questName_kr + '(' + q.questName+ ')',
            })

        for k in Kariwaza.objects.filter(Q(kariwazaName__icontains=keyword)):
            data.append({
                'category': 'Kariwaza',
                'id': k.id,
                'result': '수기 : ' + k.kariwazaName,
            })

        for r in Request.objects.filter(Q(requestName__icontains=keyword) | Q(requestName_kr__icontains=keyword)):
            data.append({
                'category': 'Request',
                'id': r.id,
                'result': '마을의뢰 : ' + r.requestName_kr + '(' + r.requestName + ')',
            })

        for s in Skill.objects.filter(Q(skillType__icontains=keyword) | Q(skillName__icontains=keyword) | Q(effect__icontains=keyword)):
            data.append({
                'category': 'Skill',
                'id': s.id,
                'result': '스킬 : ' + s.skillType,
            })

    elif searchRange == 'Quest':
        for q in Quest.objects.filter(Q(questName__icontains=keyword) | Q(questName_kr__icontains=keyword)):
            data.append({
                'category': 'Quest',
                'id': q.id,
                'result': '퀘스트 : ' + q.questName_kr + '(' + q.questName+ ')',
            })

    elif searchRange == 'Kariwaza':
        for k in Kariwaza.objects.filter(Q(kariwazaName__icontains=keyword)):
            data.append({
                'category': 'Kariwaza',
                'id': k.id,
                'result': '수기 : ' + k.kariwazaName,
            })

    elif searchRange == 'Request':
        for r in Request.objects.filter(Q(requestName__icontains=keyword) | Q(requestName_kr__icontains=keyword)):
            data.append({
                'category': 'Request',
                'id': r.id,
                'result': '마을의뢰 : ' + r.requestName_kr + '(' + r.requestName + ')',
            })

    elif searchRange == 'Skill':
        for s in Skill.objects.filter(Q(skillType__icontains=keyword) | Q(skillName__icontains=keyword) | Q(effect__icontains=keyword)):
            data.append({
                'category': 'Skill',
                'id': s.id,
                'result': '스킬 : ' + s.skillType,
            })

    print("Get - All Search")
    data = json.dumps(data, indent=4)
    print(data)
    
    return HttpResponse(data, content_type = "application/json")



def getSearchQuest(request):
    data = []

    searchRange = request.GET.get('searchRange', False)
    keyword = request.GET.get('keyword', False)
    
    if not keyword:
        return HttpResponse('False')

    if searchRange == 'name':
        for q in Quest.objects.filter(Q(questName__icontains=keyword) | Q(questName_kr__icontains=keyword)):
            data.append({
                'category': 'Quest',
                'id': q.id,
                'result': q.questName_kr + '(' + q.questName+ ')'
            })
    elif searchRange == 'rating':
        for q in Quest.objects.filter(Q(rating__icontains=keyword)):
            data.append({
                'category': 'Quest',
                'id': q.id,
                'result': q.rating + ' : ' + q.questName_kr + '(' + q.questName+ ')',
            })
    elif searchRange == 'map':
        for q in Quest.objects.filter(Q(questMap__icontains=keyword)):
            data.append({
                'category': 'Quest',
                'id': q.id,
                'result': q.questName_kr + '(' + q.questName+ ') / ' + q.questMap,
            })
    elif searchRange == 'condition':
        for q in Quest.objects.filter(Q(condition_main__icontains=keyword) | Q(condition_sub__icontains=keyword)):
            data.append({
                'category': 'Quest',
                'id': q.id,
                'result': q.questName_kr + '(' + q.questName+ ') / ' + q.condition_main,
            })

    print("Get - Search Quest")
    data = json.dumps(data, indent=4)
    print(data)
    
    return HttpResponse(data, content_type = "application/json")



def getQuestAllList(request):
    data = []

    for q in Quest.objects.all():
        data.append({
            'id': q.id,
            'questName': q.questName,
            'questName_kr': q.questName_kr,
            'rating': q.rating,
            'questMap': q.questMap,
            'condition_main': q.condition_main,
        })

    print("Get - Quest All List")
    data = json.dumps(data, indent=4)
    print(data)
    
    return HttpResponse(data, content_type = "application/json")



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
            'precedingQuestId' : q.precedingQuestId,
        })

    print("Get - Quest data")
    data = json.dumps(data, indent=4)
    print(data)
    
    return HttpResponse(data, content_type = "application/json")



def getKeyQuest(request):
    data = []
    
    for q in Quest.objects.filter(keyQuest='1'):
        data.append({
            'id': q.id,
            'questName': q.questName,
            'questName_kr': q.questName_kr,
            'rating': q.rating,
            'questMap': q.questMap,
            'condition_main': q.condition_main,
        })

    print("Get - Key Quest")
    data = json.dumps(data, indent=4)
    print(data)
    
    return HttpResponse(data, content_type = "application/json")