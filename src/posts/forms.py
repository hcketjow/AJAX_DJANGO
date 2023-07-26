from django import forms
from django.forms import TextInput
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class':"form-control",
                'placeholder':"Title",
                'type':"text",
            }),
            'body': forms.TextInput(attrs={
                'class':"form-control",
                'placeholder':"Body",
                'type':"text",
            }),
        }
        labels = {
            'title':'Title',
            'body':'Body',
        }
    