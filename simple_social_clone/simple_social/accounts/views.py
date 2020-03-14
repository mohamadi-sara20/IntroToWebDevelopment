from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

class SignUp(CreateView):
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    form_class = forms.UserCreateForm
