

from django.shortcuts import render,get_object_or_404, redirect, reverse
from django.http import HttpResponse
from .models import Course

def hello(request):
    return HttpResponse("<h1>Hello, Products Hello</h1>")

from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello, Products Hello</h1>")


courses = Course.objects.all()

def courses_home(request):
    # return with template home.html
    return render(request,"course/home.html",context={"courses":courses})


def courseForm(request):
    # return with template home.html
    return render(request,"course/courseForm.html")


# DtatBase

def course_index(request):
    courses = Course.objects.all()
    return render(request,"course/crud/index.html",context={"courses":courses})



# create new course
def course_create(request):
    
    if request.method=="POST":
        course=Course(name=request.POST.get('name'),description=request.POST["description"],duration=request.POST["duration"])
        course.save()
        # return redirect(course.show_url)
    return render(request,"course/crud/createCourse.html")


def course_delete(request,id):
    course=get_object_or_404(Course,pk=id)
    course.delete()
    url=reverse('course_index')
    return redirect(url)








