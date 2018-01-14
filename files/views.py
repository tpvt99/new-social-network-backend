from django.shortcuts import render
from django.views.generic import View
import PIL
import math
from io import BytesIO
from django.http import JsonResponse, HttpResponse
from PIL import Image
import uuid
from .models import Image as ImageModel
from user.method import get_user
from authentication.auth import check_authentication
from security.response import set_response_header
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.http import FileResponse

image_type = ['post_status','event_backgroundimage','activity_backgroundimage', 'network_profileimage']

# Create your views here.

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

def image_resize(maxWidth, maxHeight, width, height):
    maxWidth = maxWidth
    maxHeight = maxHeight
    ratio = 0
    width = width
    height = height
    if width > maxWidth:
        ratio = maxWidth / width
        height = height * ratio
        width = width * ratio

    if height > maxHeight:
        ratio = maxHeight / height
        width = width * ratio
        height = height * ratio
    return [width, height]

def handle_image_pillow(image):
    try:
        image = Image.open(image)
    except OSError:
        response = JsonResponse({'status_type':'error'})
        set_response_header(response)
        return response
    r_w, r_h = image_resize(530, 530, image.width, image.height)
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize((math.floor(r_w), math.floor(r_h)), Image.ANTIALIAS)

    image_buffer = BytesIO()
    image.save(fp = image_buffer, format = 'jpeg', optimize = True, quality = 70, progressive = True)
    image_buffer_val = image_buffer.getvalue()
    return ContentFile(image_buffer_val)

class UploadImage(View):
    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super(UploadImage, self).dispatch(*args, **kwargs)

    def options(self, request):
        pass

    def post(self, request):
        if check_authentication(request):
            # the person who upload image
            user = get_user(request)
            
            # the real file
            upload_file = request.FILES['image']

            # the type of image
            image_type = request.POST.get('imageType')
            if image_type and image_type != '':
                pass
            else:
                image_type = 'post_status'

            pillow_image = handle_image_pillow(upload_file)
            final_image = InMemoryUploadedFile(pillow_image, None, 'base.jpg', 'image/jpeg', pillow_image.tell, None)
            final_pillow_image = Image.open(final_image)

            img_model = ImageModel.objects.create(user = user, image_type = image_type, image_width = final_pillow_image.width, image_height = final_pillow_image.height, image_id = uuid.uuid4().hex)
            img_model.image = final_image
            img_model.save()
            data = {
                    'status_type': 'ok',
                    'photo_id': img_model.id,
                    'photo_url': img_model.image.url
                }
            response = JsonResponse(data)
            set_response_header(response)
            return response
        else:
            response = JsonResponse({'status_type':'error'})
            set_response_header(response)
            return response

class DownloadImage(View):
    def get(self, request):
        with open('/home/web/Pictures/asf.jpeg', 'rb') as f:
            return HttpResponse(f.read(), content_type = 'image/jpeg')
