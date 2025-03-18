from django.db import models
from django.shortcuts import reverse

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

    @property
    def delete_url(self):
        return reverse('course_delete', args=[self.id])

    @property
    def show_url(self):
        return reverse('course.show', args=[self.id])

