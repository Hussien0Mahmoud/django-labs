from django.urls import path
from course.views import course_index,course_create,course_delete,course_update


urlpatterns = [
    
     path('', course_index, name='course_index'),
    
    path('create', course_create, name='course_coursecreate'),
    path('delete/<int:id>', course_delete, name='course_delete'),
    path('update/<int:id>', course_update, name='course_update'),
]