from django.urls import path
from trainnee.views import register,login,trainee_index,trainee_create,trainee_delete,trainee_update


urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    
    path('tr_home', trainee_index, name='trainee_index'),
    
    path('create', trainee_create, name='trainee_createTrainee'),
    path('<int:id>/delete', trainee_delete, name='trainee_delete'),
    
    path('<int:id>/update', trainee_update, name='updateTrainee'),
]


