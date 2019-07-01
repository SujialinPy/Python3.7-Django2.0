from django.db import models
#一个模型类在数据库中对应一张表，在模型类中定义的属性，对应该模型中表的属性
# Create your models here.

class Grades(models.Model):
    object = models.Manager()
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    # lasttime = models.DateField(auto_now=True)
    def __str__(self):
        return self.gname
    # class Meta:
    #     db_table="grades"#定义表名
        # ordering=[]#对象的默认排序字段

#自定义模型管理器
class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager,self).get_queryset().filter(isDelete=False)

    def createStudent(self, name, age, gender, contend, grade, lastT, createT, isD=False):
        stu = self.model()
        stu.sname = name
        stu.sgender = gender
        stu.sage = age
        stu.scontend = contend
        stu.sgrade =grade
        stu.lastTime = lastT
        stu.createTime = createT
        return stu


class Students(models.Model):
    #自定义模型管理器
    stuObj =models.Manager()
    #d有了自定义模型管理器后object()无用了
    stuObj2 =StudentsManager()

    sname= models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField(db_column="age")
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    #关联外键    #2.0版本需要on_delete = models.CASCADE
    sgrade =models.ForeignKey(Grades, on_delete = models.CASCADE, related_name='cls_one')
























































    # lastTime =models.DateField(auto_now=True)
    # creatTime =models.DateField(auto_now_add=True)
    def __str__(self):
        return self.sname
    # lastTime =models.DateTimeField(auto_now=True)
    # creatTime =models.DateTimeField(auto_now_add=True)
    # class Meta:
    #     db_table="students"
    #     ordering=['id']#升序，降序[-'id']
        #注意：排序会增加数据库的开销

    #定义一个类方法创建对象
    # @classmethod
    # def createStudent(cls, name, age, gender, contend, grade, lastT, createT, isD=False):
    #     stu = cls(sname = name, sage = age,sgender = gender, scontend = contend, sgrede = grade, lastTime = lastT,
    #     createTime = createT, isDelete=isD)
    #
    #     return stu
    #
    #

