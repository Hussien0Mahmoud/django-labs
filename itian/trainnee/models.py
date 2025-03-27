from django.db import models
from django.shortcuts import reverse, get_object_or_404

from course.models import Course

# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='trainees')
    
    # course = models.ForeignKey('course.Course', on_delete=models.SET_NULL, null=True, related_name='trainees')


    def __str__(self):
        return f'{self.name}'

    @property
    def delete_url(self):
        return reverse('trainee_delete', args=[self.id])

    @property
    def show_url(self):
        return reverse('trainee.show', args=[self.id])
    
    @classmethod
    def getAllTrainees(cls):
        return cls.objects.all()
        # return cls.objects.filter(week=3) 
    
    @classmethod
    def getTrainee(cls,id):
        # return get_object_or_404(cls,pk=id)
        return get_object_or_404(cls.getAllTrainees(),pk=id)

