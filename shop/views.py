from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order
from math import ceil

# Create your views here.
def index(request):
    # products=Product.objects.all()
    # print(products)
    
    # n=len(products)
    # nslides=n//4+ceil((n/4)-n//4)
    #allProds=[[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
    allprods=[]
    catProds= Product.objects.values('category','prod_id')
    cats = {item['category'] for item in catProds}
    for i in cats:
        prod = Product.objects.filter(category=i)
        n=len(prod)
        nslides=n//4+ceil((n/4)-n//4)
        allprods.append([prod,range(1,nslides),nslides])
        

    params = {'allprods':allprods}  

    #params={'no_of_slides':nslides,'range':range(1,nslides),'products':products}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        desc=request.POST['desc']
        thanks = True
        c= Contact(name=name, phone=phone, email=email,desc=desc)
        c.save()
        return render(request,'shop/contact.html',{'thanks': thanks})
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def prodview(request,id):
    product=Product.objects.filter(prod_id=id)
    return render(request,'shop/prodview.html',{'product':product[0]})

def checkout(request):
    if request.method=='POST':
        items_json=request.POST['itemJson']
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address1'] + " " + request.POST['address2']
        city=request.POST['city']
        state=request.POST['state']
        zip_code=request.POST['zip_code']
        phone=request.POST['phone']
        
        order= Order(items_json=items_json, name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id=order.order_id
        return render(request,'shop/checkout.html',{'thank': thank,'id': id})
    return render(request,'shop/checkout.html')
