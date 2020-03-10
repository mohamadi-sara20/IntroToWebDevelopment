from django.shortcuts import render

# Create your views here.

def index(request):
    my_dict = {'msg': 'hello, index msg'}
    return render(request, 'basic_app/index.html', context=my_dict)

def other(request):
    my_dict = {'msg': 'hi, other msg'}
    return render(request, 'basic_app/other.html', context=my_dict)

def relative(request):
    my_dict = {'msg': 'hey, relative msg'}
    return render(request, 'basic_app/relative.html', context=my_dict)
