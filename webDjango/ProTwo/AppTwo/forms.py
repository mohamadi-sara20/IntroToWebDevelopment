from django import forms

class FormName(forms.Form):
    name = forms.CharField(max_length=264, unique=True)
