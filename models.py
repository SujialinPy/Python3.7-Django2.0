from django.db import models

# Create your models here.

class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

class Students(models.Model):
    sname= models.CharField(max_length=20)
    sgender = models.BooleanField()
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    #关联外键
    sgrade =models.ForeignKey('Grades', on_delete = models.CASCADE)
    #2.0版本需要on_delete = models.CASCADE
    #2.0版本需要on_delete = models.CASCADE


