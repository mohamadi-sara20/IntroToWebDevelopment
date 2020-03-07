from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Topic, Webpage, Access
# Create your views here.
def index(request):
    webpages_list = Access.objects.order_by('date')
    date_dict = {'access': webpages_list}
    # my_dict = {"insert_me": "Now I am from AppTwo/index.py"}
    return render(request, 'AppTwo/index.html', context=date_dict)
