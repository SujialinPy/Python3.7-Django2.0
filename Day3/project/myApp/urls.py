from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$',views.index),
    url(r'^students/$',views.students, name="index"),
    #分页
    # url(r'^students/(\d+)',views.stupage),
    # url(r'^addstudent/$',views.addstudent),
    url(r'^addstudent2/$',views.addstudent2),
    url(r'^main/$', views.main),
    url(r'^login/$', views.login),
    url(r'^showmain/$', views.showmain)
]
