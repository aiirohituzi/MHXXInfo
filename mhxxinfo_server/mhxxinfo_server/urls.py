"""mhxxinfo_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from quest.views import getQuestAllList
from quest.views import getQuestList
from quest.views import getQuest
from quest.views import getSearchQuest
from quest.views import getKeyQuest
from quest.views import getAllSearch
from quest.views import getSearchQuest

from kariwaza.views import getKariwaza
from kariwaza.views import getKariwazaById
from kariwaza.views import getSearchKariwaza

from requestQuest.views import getRequestQuest
from requestQuest.views import getRequestQuestById
from requestQuest.views import getSearchRequest

from skill.views import getSkill
from skill.views import getSkillById
from skill.views import getSearchSkill

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^questsAll/$', getQuestAllList, name='getQuestAllList'),
    url(r'^quests/$', getQuestList, name='getQuestList'),
    url(r'^quest/$', getQuest, name='getQuest'),
    url(r'^searchQuest/$', getSearchQuest, name='getSearchQuest'),
    url(r'^keyQuest/$', getKeyQuest, name='getKeyQuest'),
    url(r'^kariwaza/$', getKariwaza, name='getKariwaza'),
    url(r'^requestQuest/$', getRequestQuest, name='getRequestQuest'),
    url(r'^skill/$', getSkill, name='getSkill'),
    url(r'^allSearch/$', getAllSearch, name='getAllSearch'),
    url(r'^kariwazaById/$', getKariwazaById, name='getKariwazaById'),
    url(r'^requestQuestById/$', getRequestQuestById, name='getRequestQuestById'),
    url(r'^skillById/$', getSkillById, name='getSkillById'),
    
    url(r'^searchQuest/$', getSearchQuest, name='getSearchQuest'),
    url(r'^searchKariwaza/$', getSearchKariwaza, name='getSearchKariwaza'),
    url(r'^searchRequest/$', getSearchRequest, name='getSearchRequest'),
    url(r'^searchSkill/$', getSearchSkill, name='getSearchSkill'),
]
