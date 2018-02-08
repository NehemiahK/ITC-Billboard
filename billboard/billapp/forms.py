from django import forms
from .models import Post

from django.contrib.auth.models import User # import the user creation from django
# from django.views.decorators.csrf import csrf_protect

# @csrf_protect
#creating a model/form
# forms is altering the Post model and is what gets passed on to the views.
class PostForm(forms.ModelForm): # the form that is filled out

    class Meta:
        model = Post # the model being is used post whihc was imported
        fields = ('title', 'text', 'author') # fields from models
        labels = {
            'title': "",
            'text': "",
            'author': "",
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'text': forms.Textarea(attrs={'cols':100,'placeholder': 'Enter message here'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
