from django.shortcuts import render, redirect
from .models import products
from .models import Thems

# Create your views here.
from django.http import HttpResponse, JsonResponse

def home (request):
    return render(request, 'pages/home.html')

def about (request):
    return render(request, 'pages/aboutpage.html') 

def more (request):
    return render(request, 'pages/more.html')

def contact (request):
    return render(request, 'pages/contact.html')

# Retrive all blogs models
def product (request):
    
    product= products.objects.all()
    return render(request, 'pages/aboutpage.html',{'products':product})

# Retrive all thems models
def them (request):

    them= Thems.objects.all()
    return render(request, 'pages/more.html', {'thems':them})

# Retrive all blogdetails models
def productdetails (request, product_slug):
    
    product= products.objects.all()
    productdetails= products.objects.get(slug= product_slug)
    return render(request, 'pages/details.html',{'products':product, 'productdetails': productdetails})

# Retrive all eachside models
def eachside (request, product_slug):

    each= products.objects.get(slug= product_slug)
    return render(request, 'pages/each.html', {'each':each})
    
def custom_404(request, exception):
    return render(request, 'pages/404error.html', {}, status=404)

# Retrive manager page
def manager (request):
    return render(request, 'manager/dashboard.html')

def productsmg (request):
    productsmg= products.objects.all()
    return render(request, 'manager/productsadmin.html',{'products':productsmg})

def themsmg (request):
    themsmg= Thems.objects.all()
    return render(request, 'manager/themsadmin.html', {'thems':themsmg})

def add_products(request):
    if request.method == "POST":
        name= request.POST.get('name')
        writer= request.POST.get('writer')
        content= request.POST.get('content')
        img= request.POST.get('image')
        cost= int(request.POST.get('cost',0))
        print(name)

        productsmg= products(

            name=name,
            writer=writer,
            content=content,
            img=img,
            cost=cost,
        )
        productsmg.save()

    return redirect('/manager/productsad/')

def edit_products(request,product_id):
    try:
        product= products.objects.get(id=product_id)
    except products.DoesNotExist:
        return redirect('/manager/productsad/')
    
    
    if request.method == "POST":
        name= request.POST.get('name')
        writer= request.POST.get('writer')
        content= request.POST.get('content')
        img= request.POST.get('image')
        cost= int(request.POST.get('cost',0))
        
        product.name= name
        product.writer= writer
        product.content= content
        product.img= img
        product.cost= cost

        product.save()
    return redirect('/manager/productsad/')
        
def delete_products(request,product_id):
    try:
        productdl= products.objects.get(id=product_id)
    except products.DoesNotExist:
        return redirect('/manager/productsad/')
    if request.method == "POST":
        productdl.delete()
    return redirect('/manager/productsad/')
        
        