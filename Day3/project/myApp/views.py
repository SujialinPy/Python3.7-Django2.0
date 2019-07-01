from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# def index(request):
#     return HttpResponse("SS")

from .models import Students,Grades
def students(request):
    studentsList = Students.stuObj.all()
    return render(request, 'myApp/students.html',{"students":studentsList})

# def addstudent(request):
#     grade = Grades.object.get(pk=1)
#     stu = Students.createStudent("刘德华",34,True,"我是刘德华",grade,"2017-12-2","2017-12-2")
#     stu.save()
#     return  HttpResponse("sjkdbaskj ")

from django.http import HttpResponsePermanentRedirect
def addstudent2(request):
    grade = Grades.object.get(pk=1)
    stu = Students.stuObj2.createStudent("刘德华",34,True,"我是刘德华",grade,"2017-12-2","2017-12-2")
    stu.save()
    return HttpResponse("251351")
#分页显示
# def stupage(request, page):
#     studentList = Students.stuObj2.all()[(page - 1)]


def main(request):
    username =request.session.get('name', "游客")
    return render(request, 'myApp/main.html', {'username':username})
def login(request):
    return render(request, 'myApp/login.html ')

#重定向
from django.shortcuts import redirect
def showmain(request):
    username = request.POST.get('username')
    #存储session
    request.session['name'] = username
    request.session.set_expiry(10)#设置session过期时间
    return redirect('/main/')