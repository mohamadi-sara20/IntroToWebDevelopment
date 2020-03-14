from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionsMixin)
from django.urls import reverse
from django.views import generic
from groups.models import Group

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Group


class SignleGroup(generic.DetailView):
    model = Group

class ListGroup(generic.ListView):
    model = Group
