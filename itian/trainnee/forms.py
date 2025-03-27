from django import forms
from .models import Trainee

class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = ['name', 'email', 'course']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
        }
        
        
        