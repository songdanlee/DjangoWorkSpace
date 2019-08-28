from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=16)
    birthday = models.DateField()
    email = models.EmailField()
    address = models.TextField()
    photo = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name


class ArticleType(models.Model):
    label = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.label

class Article(models.Model):
    title = models.CharField(max_length=32)
    article_author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    # models.CASCADE 级联删除，作者删除，文章删除
    # models.SET_NULL 设置空，作者删除，文章的作者设置为null
    # models.SET_DEFAULT 设置默认值，作者删除，文章的作者设置为默认值，需要配合default参数使用
    desciption = models.TextField()
    content = models.TextField()
    article_type = models.ManyToManyField(to=ArticleType)
    public_time = models.DateField(auto_now=True)
    picture = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title