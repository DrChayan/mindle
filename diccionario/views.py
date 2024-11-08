from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def pagDicc(request):
    return render(request, 'pagdicc.html')
