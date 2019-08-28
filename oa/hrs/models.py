from django.db import models

# Create your models here.
class Dept(models.Model):
    """部门类"""

    no = models.IntegerField