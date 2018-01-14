# urls

from django.conf.urls import url

from .views import Profile, Head, Bio
from .views import ChangeProfilePic, Name
from .views import AddEditPlace, AddEditWork, AddEditEducation, Content, ChangeBackgroundPic
from .views import BasicInfo

app_name = 'pro'

urlpatterns = [
    url(r'^profile/fetch$', Profile.as_view(), name='profile'),

    url(r'^profile/info$', BasicInfo.as_view(), name='info'),
    
    url(r'^profilepic/$', ChangeProfilePic.as_view(), name='profilepic'),

    url(r'^backgroundpic/$', ChangeBackgroundPic.as_view(), name='backgroundpic'),


    url(r'^head/$', Head.as_view(), name='head'),

    url(r'^bio/$', Bio.as_view(), name='bio'),

    url(r'^content/$', Content.as_view(), name='content'),

    url(r'^name/$', Name.as_view(), name='name'),

    url(r'^place/(?P<type>[a-z]+)/$', AddEditPlace.as_view(), name='place'),

    url(r'^work/(?P<type>[a-z]+)/$', AddEditWork.as_view(), name='work'),

    url(r'^edu/(?P<type>[a-z]+)/(?P<kind>[a-z]+)/$', AddEditEducation.as_view(), name='edu')


    ]
