from django.urls import path
from trainnee.views import hello,trainee_home,traineeForm,register,login,trainee_index,trainee_create,trainee_delete


urlpatterns = [
    path('helloworld', hello, name='hellopage'),
    path('trainee_home', trainee_home, name='trainee_home'),
    
    path('traineeForm', traineeForm, name='traineeForm'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    
    path('trainee_index', trainee_index, name='trainee_index'),
    
    path('create', trainee_create, name='trainee_createTrainee'),
    path('<int:id>/delete', trainee_delete, name='trainee_delete'),
]