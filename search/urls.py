#urls

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

#view
from .views import HeaderSearch

app_name = 'search'

urlpatterns= [ 
    url(r'^header$', HeaderSearch.as_view(), name = 'header')

]

