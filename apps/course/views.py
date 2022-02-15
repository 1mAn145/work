from apps.course.forms import CreateCourseForm
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from apps.course.models import Course, Tasks
# from apps.course.models import Course

def index(request):
    course= Course.objects.all()
    return render(request,"index.html",{'course':course})

def create_course(request):
    if request.method == "POST":
        form = CreateCourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = Course()
            course.user=request.user
            course.save()
            return redirect("/")
        else:
            messages.info("Error")
    return render(request,'create_course.html')

def course_detail(request,id):
    course1=get_object_or_404(Course,id=id)
    course = Course.objects.get(id=id)
    
    contex={
        'course':course,
        'course1':course1
    }
    return render(request, 'course_detail.html',contex)

def task(request,id):
    task=Tasks.objects.get(id=id)
    contex={
        'task':task
    }
    return render(request,'task_detail.html',contex)

    