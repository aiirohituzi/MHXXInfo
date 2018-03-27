from django.shortcuts import render
from django.http import HttpResponse

from requestQuest.models import Request
import json
from django.db.models import Q

def getSearchRequest(request):
    data = []

    searchRange = request.GET.get('searchRange', False)
    keyword = request.GET.get('keyword', False)
    
    if not keyword:
        return HttpResponse('False')

    if searchRange == 'name':
        for r in Request.objects.filter(Q(requestName__icontains=keyword) | Q(requestName_kr__icontains=keyword)):
            data.append({
                'category': 'Request',
                'id': r.id,
                'result': r.requestName_kr + '(' + r.requestName + ')'
            })
    elif searchRange == 'reward':
        for r in Request.objects.filter(Q(reward__icontains=keyword)):
            data.append({
                'category': 'Request',
                'id': r.id,
                'result': r.town + ' : ' + r.requestName_kr + '(' + r.requestName + ')'
            })

    print("Get - Search Request Quest")
    data = json.dumps(data, indent=4)
    print(data)
    
    return HttpResponse(data, content_type = "application/json")



def getRequestQuest(request):
    data = []
    
    for r in Request.objects.all():
        data.append({
            'town': r.town,
            'requestName': r.requestName,
            'requestName_kr': r.requestName_kr,
            'condition': r.condition,
            'reward': r.reward,
        })

    print("Get - Request")
    data = json.dumps(data, indent=4)
    print(data)
    
    return HttpResponse(data, content_type = "application/json")



def getRequestQuestById(request):
    data = []
    id = request.GET.get('id', False)

    if not id:
        return HttpResponse('False')

    for r in Request.objects.filter(id=id):
        data.append({
            # 'id': r.id,
            'town': r.town,
            'requestName': r.requestName,
            'requestName_kr': r.requestName_kr,
            'condition': r.condition,
            'reward': r.reward
        })

    print("Get - Request by ID")
    data = json.dumps(data, indent=4)
    print(data)

    return HttpResponse(data, content_type = "application/json")
