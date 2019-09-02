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
    list_display = ('id', 'title', 'description','content','public_time','picture','article_author_id')
    ordering = ('id',)

class ImgAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'src','summary')
    ordering = ('id',)


admin.site.register(ArticleType,ArticleTypeAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Img,ImgAdmin)
