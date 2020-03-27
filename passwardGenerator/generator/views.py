from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html')

def password(request):
    simbol = [chr(x) for x in range(97, 123)]
    if request.GET.get('uppercase'):
        simbol += [chr(x) for x in range(65, 91)]
    if request.GET.get('numbers'):
        simbol += [str(x) for x in range(10)]
    if request.GET.get('special'):
        simbol += list('!@#$%^&*()_+')
    length = int(request.GET.get('length', 7))
    password = ''.join([random.choice(simbol) for x in range(length)])

    return render(request, 'generator/password.html', {'password': password})
