"""a URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^plustag/', include('plustag.urls')),
    url(r'^moment/', include('moment.urls')),
    url(r'^group/', include('group.urls')),
    url(r'^trait/', include('trait.urls')),
    url(r'^skill/', include('skill.urls')),
    url(r'^status/', include('status.urls')),
    url(r'^post/', include('post.urls')),
    url(r'^act/', include('act.urls')),
    url(r'^anonymous/',include('anonymous.urls')),
    url(r'^goal/', include('goal.urls')),
    url(r'^scholarship/', include('scholarship.urls')),
    url(r'^contest/', include('contest.urls')),
    url(r'^diary/', include('diary.urls')),
    url(r'^event/', include('event.urls')),
    url(r'^plan/', include('plan.urls')),
    url(r'^page/', include('page.urls')),
    url(r'^friend/', include('friend.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^activities/', include('activities.urls')),
    url(r'^activity/', include('activity.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^', include('security.urls')),
    url(r'^', include('network.urls')),
    url(r'^', include('account.urls')),
    url(r'^', include('message.urls')),
    url(r'^', include('pro.urls')),
    url(r'^', include('noti.urls')),
    url(r'^', include('user.urls')),
    url(r'^', include('files.urls')),
    url(r'^', include('web.urls')),
    url(r'^', include('frontpage.urls')),
    url(r'^admin/', admin.site.urls),
]
