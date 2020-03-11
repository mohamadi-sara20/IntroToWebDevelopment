from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

class CBView(View):
    def get(self, request):
        return HttpResponse('CLASS-BASED VIEWS ARE COOL')

class IndexView(TemplateView):
    template_name = 'index.html'
