from django.shortcuts import render

# Create your views here.

def miTienda (request):
    return render(request,'tendero/inicio.html')