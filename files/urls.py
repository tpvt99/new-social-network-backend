from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import UploadImage, DownloadImage

app_name = 'files'

urlpatterns = [
    url(r'^upload/image/$', UploadImage.as_view(), name="image"),

    url(r'^download/image/$', DownloadImage.as_view(), name="image")

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
