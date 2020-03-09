from django.shortcuts import render
from basicApp import forms
# Create your views here.
def index(request):
    return render(request, 'basicApp/index.html')

def form_name(request):
    form = forms.FormName(request.POST)
    if form.is_valid():
        print('VALIDATED!')
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['text'])


    return render(request, 'basicApp/formPage.html', context={'form': form})
