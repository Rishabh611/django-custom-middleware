from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def exceptionView(request):
    a = 2
    print(a[2])
    return HttpResponse("yo")
