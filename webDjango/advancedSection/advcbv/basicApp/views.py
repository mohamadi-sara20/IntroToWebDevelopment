from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                 ListView, DetailView,
                                 CreateView, UpdateView,
                                 DeleteView)
from django.http import HttpResponse
from django.urls import reverse_lazy
from . import models

class CBView(View):
    def get(self, request):
        return HttpResponse('CLASS-BASED VIEWS ARE COOL')

class IndexView(TemplateView):
    template_name = 'basicApp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'basicApp/schoolList.html'


class SchoolDetailView(DetailView):
    context_object_name = 'schoolsDetails'
    model = models.School
    template_name = 'basicApp/schoolDetail.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name', 'principal')

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basicApp:list')
