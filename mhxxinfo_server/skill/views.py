from django.shortcuts import render
from django.http import HttpResponse

from skill.models import Skill
import json
from django.db.models import Q



def getSearchSkill(request):
    data = []

    searchRange = request.GET.get('searchRange', False)
    keyword = request.GET.get('keyword', False)
    
    if not keyword:
        return HttpResponse('False')

    if searchRange == 'type':
        for s in Skill.objects.filter(Q(skillType__icontains=keyword)):
            data.append({
                'category': 'Skill',
                'id': s.id,
                'result': s.skillType
            })
    elif searchRange == 'skillName':
        for s in Skill.objects.filter(Q(skillName__icontains=keyword)):
            data.append({
                'category': 'Skill',
                'id': s.id,
                'result': s.skillType
            })
    elif searchRange == 'effect':
        for s in Skill.objects.filter(Q(effect__icontains=keyword)):
            data.append({
                'category': 'Skill',
                'id': s.id,
                'result': s.skillType
            })

    print("Get - Search Skill")
    data = json.dumps(data, indent=4)
    print(data)
    
    return HttpResponse(data, content_type = "application/json")



def getSkill(request):
    data = []
    
    for s in Skill.objects.all():
        data.append({
            'skillType': s.skillType,
            'skillName': s.skillName,
            'point': s.point,
            'effect': s.effect,
        })

    print("Get - Skill")
    data = json.dumps(data, indent=4)
    print(data)
    
    return HttpResponse(data, content_type = "application/json")



def getSkillById(request):
    data = []
    id = request.GET.get('id', False)

    if not id:
        return HttpResponse('False')

    for s in Skill.objects.filter(id=id):
        data.append({
            # 'id': s.id,
            'skillType': s.skillType,
            'skillName': s.skillName,
            'point': s.point,
            'effect': s.effect
        })

    print("Get - Skill by ID")
    data = json.dumps(data, indent=4)
    print(data)

    return HttpResponse(data, content_type = "application/json")