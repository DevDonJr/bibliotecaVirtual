from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse('login.html')

def cadastro(request):
    return render(request, 'cadastro.html')