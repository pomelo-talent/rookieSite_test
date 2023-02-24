from django.contrib import admin
from .models import ArticleType, Article

# Register your models here.
@admin.register(ArticleType)
class ArticleTypeAdmin(admin.ModelAdmin):
    # () tuple
    list_display = ("id", "type_name")

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # () tuple
    list_display = ("id", "title", "article_type", "content", "author", "is_deleted", "created_time", "last_updated_time")
    ordering = ("-id",)

#admin.site.register(Article, ArticleAdmin)
