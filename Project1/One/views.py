from django.shortcuts import render
from django.shortcuts import HttpResponse
from  One.models import Student
from  One.models import Grade
from  One.models import Teacher 

# Create your views here.
def add_grade(requset):
    add_grade = Grade(g_name=123)
    add_grade.save()
    return HttpResponse("add sucess")
    

def add_stu(request): 
    # 1.add_stu=Student.crate('jack','123')
    add_stu=Student.objects.create(s_name='jack',s_grade_id=1)
    add_stu.save()
    return HttpResponse("add sucess")

def get_studentall(request):
    stu=Student.objects.all
    context={
        'stu':stu
    }
    # print(dir(stu))
    return render(request,'index.html',context)


def get_gradeBystu(requset,id):
    g=Student.objects.get(pk=id).s_grade
    context={
        'grade':g
    }
    return render(requset,'grade.html',context)

def get_studentBygrade(requset,id):
    grade=Grade.objects.get(pk=id)
    stu=grade.student_set.all()
    context={
        'students':stu
    }
  
    return render(requset,'student_list.html',context=context)

def get_teaBygrade(requset,id):
    g= Grade.objects.get(pk=id)
    th = g.teacher_set.all()
    context={
        'teacher':th
    }
    return render(requset,'teacher_list.html',context=context)



def del_stu(request):
    stu=Student.objects.filter(s_name='jack')
    stu.delete()
    return HttpResponse('del sucess')
