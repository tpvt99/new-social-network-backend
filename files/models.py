from django.db import models
from user.models import User
import os
from uuid import uuid4
import hashlib
from django.utils.deconstruct import deconstructible

# Create your models here.

@deconstructible
class UploadToPathAndRename(object):
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        image_id = instance.pk
        if type(image_id) == str:
            image_id_hash = hashlib.md5(str.encode(image_id)).hexdigest()
        elif type(image_id) == int:
            image_id_hash = hashlib.md5(str.encode(str(image_id))).hexdigest()
        if instance.user:
            user_id = instance.user.id
            user_id_hash = hashlib.md5(str.encode(str(user_id))).hexdigest()
        fn = '{}/{}_{}_{}.{}'.format(user_id_hash, user_id, image_id_hash, uuid4().hex , ext)
        return os.path.join(self.path, fn)

class Image(models.Model):
    image = models.ImageField(upload_to=UploadToPathAndRename('uploads/'), height_field = "image_height", width_field = "image_width", null = True)
    image_height = models.PositiveIntegerField(default = 0, null = True)
    image_width = models.PositiveIntegerField(default = 0, null = True)
    image_id = models.CharField(max_length = 50, unique = True) # used when generate same image but different size to serve different purpose
    has_saved = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    # type of image which is profile picture or new feed or both to have different sizes
    image_type = models.CharField(max_length = 100, null = True) #newfeed #profileimage #event
    time = models.DateTimeField(auto_now_add = True)
