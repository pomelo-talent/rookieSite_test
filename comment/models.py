from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
#from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Comment(models.Model):
    # ContentType table: 1-app->n-models
    # to judge which app does the "Comment" appear in, like: "Comment" appears in article app
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    # like: to judge which article does the "Comment" appear in
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-comment_time',]
    

