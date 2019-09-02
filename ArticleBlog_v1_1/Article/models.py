from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=16)
    birthday = models.DateField()
    email = models.EmailField()
    address = RichTextField()
    photo = models.ImageField(upload_to="images/img")

    def __str__(self):
        return self.name


class ArticleType(models.Model):
    label = models.CharField(max_length=32)
    description = RichTextField()

    def __str__(self):
        return self.label

class Article(models.Model):
    title = models.CharField(max_length=32)
    article_author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    # models.CASCADE 级联删除，作者删除，文章删除
    # models.SET_NULL 设置空，作者删除，文章的作者设置为null
    # models.SET_DEFAULT 设置默认值，作者删除，文章的作者设置为默认值，需要配合default参数使用
    description = RichTextField()
    content = RichTextField()
    article_type = models.ManyToManyField(to=ArticleType)
    public_time = models.DateField(auto_now=True)
    picture = models.ImageField(upload_to="images")
    click = models.IntegerField(default=0) # 点击率 默认为0
    recomment = models.IntegerField(default=0) # 推荐 0 默认， 1为推荐


    def __str__(self):
        return self.title


class Img(models.Model):
    """
    upload_to: 上传文件地址
    """
    src = models.FileField(max_length=64, verbose_name='图片地址', upload_to='app/static/app/upload')
    title = models.CharField(max_length=64, verbose_name='标题')
    summary = models.CharField(max_length=128, verbose_name='简介')

    class Meta:
        verbose_name_plural = '图片'

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

if __name__ == '__main__':
    # article = Article()
    # article.title = "菊花台"
    # article.article_author = Author.objects.get(id=1)
    # article.desciption = "你的泪光柔弱中带伤"
    # article.content = "菊花灿烂的伤，你的笑容已泛黄"
    # import datetime

    # article.public_time = datetime.datetime.now()
    # article.picture = "images/st.jpg"
    # article.save()
    # article.article_type.add(ArticleType.objects.get(id=1))
    # article.article_type.add(ArticleType.objects.get(id=2))
    # article.article_type.add(ArticleType.objects.get(id=3))
    # article.save()


    # atype = ArticleType.objects.get(id=4) # 个人日记
    # articles = Article.objects.filter(id__gt=150).all()
    # for i in articles:
    #     i.article_type.add(atype)
    #     i.save()
    pass