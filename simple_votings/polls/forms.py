from django import forms
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.forms import ModelForm
from django.shortcuts import redirect
from django.urls import reverse_lazy

from polls.models import Poll


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.success(self.request, f"You have successfully logged in as {self.request.user.username}!")
        return redirect(self.get_success_url())

    def get_success_url(self):
        return self.get_redirect_url() or reverse_lazy('index')


class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three', 'question_type']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your question'}),
            'option_one': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Option 1'}),
            'option_two': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Option 2'}),
            'option_three': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Option 3'}),
            'question_type': forms.Select(attrs={'class': 'form-control'}),
        }
