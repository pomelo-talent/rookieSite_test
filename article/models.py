from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class ArticleType(models.Model):
    type_name = models.CharField(max_length=15)
    def __str__(self):
        return self.type_name

class Article(models.Model):
    # title's format: char
    title = models.CharField(max_length=30)
    article_type = models.ForeignKey(ArticleType, on_delete=models.DO_NOTHING, null=True)
    # content's format: text
    content = RichTextUploadingField()
    # created_time's format: datetime
    created_time = models.DateTimeField(auto_now_add=True)
    # last_updated_time's format: datetime
    last_updated_time = models.DateTimeField(auto_now=True)
    # DO_NOTHING: When the author is deleted, his/her article is not deleted
    # default=1-->superuser
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    # logically deleted, not physically deleted from db 
    is_deleted = models.BooleanField(default=False)
    page_view = models.IntegerField(default=0)

    def __str__(self):
        return "<Article: %s>" % self.title


