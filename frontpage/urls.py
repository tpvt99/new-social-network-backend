# urls

from django.conf.urls import url

# view
from .views import Register, Login, Logout

app_name = 'frontpage'

urlpatterns = [

        url(r'^register/$', Register.as_view(), name='register'),

        url(r'^login/$', Login.as_view(), name='login'),

        url(r'^logout$', Logout.as_view(), name='logout'),

        ]
