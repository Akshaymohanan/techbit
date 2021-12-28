from django.shortcuts import render, redirect
from .models import Projects

def home(request):
    products = Projects.objects.all()

    img=[]
    for i in range(len(products)):
        img.append(products[i].image)

    return render(request, 'home.html', {'product':products, 'm':img})

def product(request,id):
    product = Projects.objects.get(id=id)
    return render(request, 'product.html',{'product':product})