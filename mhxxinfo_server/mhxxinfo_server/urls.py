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
from quest.views import getKariwaza

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^questsAll/$', getQuestAllList, name='getQuestAllList'),
    url(r'^quests/$', getQuestList, name='getQuestList'),
    url(r'^quest/$', getQuest, name='getQuest'),
    url(r'^searchQuest/$', getSearchQuest, name='getSearchQuest'),
    url(r'^keyQuest/$', getKeyQuest, name='getKeyQuest'),
    url(r'^kariwaza/$', getKariwaza, name='getKariwaza'),
]
