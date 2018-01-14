from django.db import models
from django.conf import settings

TRAIT_TYPE = [
        'active',
        'calm',
        'caring',
        'clean',
        'cheerful',
        'gentle',
        'helpful',
        'humorous',
        'kind'
        ]

# Create your models here.

def upload_trait_picture(instance , filename):
    return 'trait/{0}'.format(filename)

class Trait(models.Model):
    user_send = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True, related_name="%(app_label)s_%(class)s_user_send")
    user_receive = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True, related_name="%(app_label)s_%(class)s_user_receive")
    trait_type = models.CharField(max_length = 100)
    text = models.TextField()
    image = models.ImageField(upload_to=upload_trait_picture, null = True)
