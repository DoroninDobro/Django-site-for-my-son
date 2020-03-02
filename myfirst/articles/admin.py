from django.contrib import admin

from . models import Article, Comment
# Register your models here.

# class PostModelAdmin(admin.ModelAdmin):
#     list_display = ["article_title"]
#     list_display_links = ["article_title"]
#     list_editable = ["article_title"]
#     list_filter = ["article_title"]
#     search_fields = ["article_title"]
#     class Meta:
#         model = Article

admin.site.register(Article)#, PostModelAdmin)
admin.site.register(Comment)