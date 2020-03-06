from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    my_dict = {"insert_me": "Now I am from AppTwo/index.py"}
    return render(request, 'AppTwo/index.html', context=my_dict)
