from django.shortcuts import render ,get_object_or_404, redirect, reverse
from django.http import HttpResponse
from .models import Trainee
from course.models import Course


def hello(request):
    # request is not used in this function
    return HttpResponse("<h1>Hello, Products Hello</h1>")


trainees=[
    {"id":1, "name":"Hussien","email":"hussien@gmail.com","course":"React"},
    {"id":2, "name":"Ibrahim","email":"ibrahim@gmail.com","course":"Java"},
    {"id":3, "name":"Ahmed","email":"ahmed@gmail.com","course":"Django"},
    {"id":4, "name":"Mohamed","email":"mohamed@gmail.com","course":"Html"},
    {"id":5, "name":"Yasser","email":"yasser@gmail.com","course":"Python"},
]

def trainee_home(request):
    # return with template home.html
    return render(request,"trainee/home.html",context={"trainees":trainees})

def traineeForm(request):
    # return with template home.html
    return render(request,"trainee/traineeForm.html")

def login(request):
    # return with template home.html
    return render(request,"trainee/login.html")
def register(request):
    # return with template home.html
    return render(request,"trainee/register.html")



# from database
# def trainee_detail(request,id):
#     trainee = get_object_or_404(Trainee,pk=id)
#     return render(request,"trainee/crud/detail.html",context={"trainee":trainee})

def trainee_index(request):
    trainees = Trainee.objects.all()
    return render(request,"trainee/crud/index.html",context={"trainees":trainees})



# create new trainee
def trainee_create(request):
    courses = Course.objects.all()
    
    if request.method == "POST":
        trainee = Trainee(name=request.POST["name"], email=request.POST["email"], course=request.POST["course"])
        trainee.save()
        # return redirect(trainee.show_url)
    
    return render(request, "trainee/crud/createTrainee.html", context={"courses": courses})

def trainee_delete(request,id):
    # request is not used in this function
    trainee=get_object_or_404(Trainee,pk=id)
    trainee.delete()
    url=reverse('trainee_index')
    return redirect(url)
    return redirect(url)






