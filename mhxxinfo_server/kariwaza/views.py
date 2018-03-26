from django.shortcuts import render
from django.http import HttpResponse

from quest.models import Kariwaza
import json
from django.db.models import Q



def getSearchKariwaza(request):
    data = []

    searchRange = request.GET.get('searchRange', False)
    keyword = request.GET.get('keyword', False)
    
    if not keyword:
        return HttpResponse('False')

    if searchRange == 'category':
        for k in Kariwaza.objects.filter(Q(category__icontains=keyword)):
            data.append({
                'category': 'Kariwaza',
                'id': k.id,
                'result': k.category + ' : ' + k.kariwazaName
            })
    elif searchRange == 'name':
        for k in Kariwaza.objects.filter(Q(kariwazaName__icontains=keyword)):
            data.append({
                'category': 'Kariwaza',
                'id': k.id,
                'result': k.kariwazaName + '(' + k.category+ ')',
            })

    print("Get - Search kariwaza")
    data = json.dumps(data, indent=4)
    print(data)
    
    return HttpResponse(data, content_type = "application/json")



def getKariwaza(request):
    data = []
    
    for k in Kariwaza.objects.all():
        data.append({
            'id': k.id,
            'category': k.category,
            'kariwazaName': k.kariwazaName,
            'level': k.level,
            'condition': k.condition,
        })

    print("Get - Kariwaza")
    data = json.dumps(data, indent=4)
    print(data)
    
    return HttpResponse(data, content_type = "application/json")



def getKariwazaById(request):
    data = []
    id = request.GET.get('id', False)

    if not id:
        return HttpResponse('False')

    for k in Kariwaza.objects.filter(id=id):
        data.append({
            # 'id': k.id,
            'category': k.category,
            'kariwazaName': k.kariwazaName,
            'level': k.level,
            'condition': k.condition
        })

    print("Get - Kariwaza by ID")
    data = json.dumps(data, indent=4)
    print(data)

    return HttpResponse(data, content_type = "application/json")