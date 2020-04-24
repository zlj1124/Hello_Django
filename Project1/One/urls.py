# -*- coding: utf-8 -*-
from django.conf.urls import url
from .import views
urlpatterns = []
urlpatterns += [
    url(r'getall/',views.get_studentall),
    url(r'getgrade/(\d+)/', views.get_gradeBystu, name='grade'),
    url(r'getteacher/(\d+)/', views.get_teaBygrade,name='teacher'),
    url(r'addgrade', views.add_grade),
    url(r'addstu', views.add_stu),
    url(r'delstu', views.del_stu),
    url(r'getall/', views.add_grade),

  
    
  
]