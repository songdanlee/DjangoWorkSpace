from django.db import models


# Create your models here.
class LoginUser(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=32, null=True, blank=True)


    username = models.CharField(max_length=32,null=True,blank=True)
    phone_num = models.CharField(max_length=11,null=True,blank=True)
    address = models.TextField()
    photo = models.ImageField(upload_to='image')
    gender = models.CharField(max_length=10,null=True,blank=True)

