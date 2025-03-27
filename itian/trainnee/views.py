from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from .models import Trainee
from course.models import Course
from trainnee.forms import TraineeForm


def login(request):
    return render(request,"trainee/login.html")
def register(request):
    return render(request,"trainee/register.html")



# from database
# def trainee_detail(request,id):
#     trainee = get_object_or_404(Trainee,pk=id)
#     return render(request,"trainee/crud/detail.html",context={"trainee":trainee})

def trainee_index(request):
    # trainees = Trainee.objects.all()  
    trainees= Trainee.getAllTrainees()  
    return render(request, "trainee/crud/index.html", context={"trainees": trainees})




def trainee_create(request):
    courses = Course.objects.all()
    if request.method == "POST":
        form = TraineeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("trainee_index")
    else:
        form = TraineeForm()
    return render(request, "trainee/crud/createTrainee.html", context={"courses": courses, "form": form})

def trainee_delete(request,id):
    # request is not used in this function
    trainee=get_object_or_404(Trainee,pk=id)
    trainee.delete()
    url=reverse('trainee_index')
    return redirect(url)



def trainee_update(request,id):
    # trainee = get_object_or_404(Trainee,pk=id)
    trainee=Trainee.getTrainee(id) 
    courses = Course.objects.all()
    if request.method == "POST":
        form = TraineeForm(request.POST, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect("trainee_index")
    else:
        form = TraineeForm(instance=trainee)
    return render(request, "trainee/crud/createTrainee.html", context={"courses": courses,"form":form})




