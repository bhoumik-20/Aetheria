from django import forms
from .models import Board

class BoardCreateForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'description', 'is_public']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter board title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Describe your vision board...',
                'rows': 4
            }),
            'is_public': forms.CheckboxInput(attrs={
                'class': 'checkbox-input'
            })
        }
