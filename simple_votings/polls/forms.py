from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from polls.models import Poll


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your question'}),
            'option_one': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Option 1'}),
            'option_two': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Option 2'}),
            'option_three': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Option 3'}),
        }
