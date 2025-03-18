from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    course = models.ForeignKey('course.Course', on_delete=models.SET_NULL, null=True, related_name='trainees')

    def __str__(self):
        return f'{self.name}'

    @property
    def delete_url(self):
        return reverse('trainee_delete', args=[self.id])

    @property
    def show_url(self):
        return reverse('trainee.show', args=[self.id])

