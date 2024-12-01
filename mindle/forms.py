from django import forms    
class trastornoForm(forms.Form):
    inputTrastorno = forms.CharField(max_length=200)