from django.contrib import admin
from Article.models import *
# Register your models here.


class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'label', 'description')
    ordering = ('id', )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age','gender','birthday','email','address','photo')
    ordering = ('id',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desciption','content','public_time','picture','article_author_id')
    ordering = ('id',)


admin.site.register(ArticleType,ArticleTypeAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Article,ArticleAdmin)