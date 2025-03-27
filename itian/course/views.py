

from django.shortcuts import render,get_object_or_404, redirect, reverse
from django.http import HttpResponse
from .models import Course
from .forms import CourseForm


from django.shortcuts import render
from django.http import HttpResponse


courses = Course.objects.all()





def course_index(request):
    courses = Course.objects.all()
    return render(request,"course/crud/index.html",context={"courses":courses})


def course_create(request):
    if request.method=="POST":
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_index')
    else:
        form=CourseForm()
    return render(request,"course/crud/createCourse.html",context={"form":form})


def course_delete(request,id):
    course=get_object_or_404(Course,pk=id)
    course.delete()
    url=reverse('course_index')
    return redirect(url)

 
def course_update(request,id):
    course=get_object_or_404(Course,pk=id)
    if request.method=="POST":
        form=CourseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_index')
    else:
        form=CourseForm(instance=course)
    return render(request,"course/crud/createCourse.html",context={"form":form})







