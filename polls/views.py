from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hola, este es el indice de encuestas :).")


# Create your views here.
