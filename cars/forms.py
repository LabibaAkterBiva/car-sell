from django import forms 
from .models import Car,Comment
class PostForm(forms.ModelForm):
    class Meta:
        model = Car

        fields='__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']