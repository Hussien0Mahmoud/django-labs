from django.urls import path
from course.views import hello,courses_home,courseForm,course_index,course_create,course_delete


urlpatterns = [
    path('helloworld', hello, name='hellopage'),
    
    path('courses_home', courses_home, name='courses_home'),
    
    path('courseForm', courseForm, name='courseForm'),
    
     path('course_index', course_index, name='course_index'),
    
    path('create', course_create, name='course_coursecreate'),
    path('delete/<int:id>', course_delete, name='course_delete'),
]