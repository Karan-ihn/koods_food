from django.shortcuts import render,HttpResponse,redirect
from shop.models import Product,Contact,Orders
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    products = Product.objects.all()
    params = {'products': products}
    return render(request,'shop/index.html',params)

def handlelogin(request):
    if request.method == "POST":
        login_username = request.POST['loginusername']
        login_password = request.POST['loginpassword']

        user = authenticate(username=login_username,password=login_password)
        if user is not None:
            login(request,user)
            messages.success(request,'logged in succesfully')
            return redirect('/')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('/')
    return HttpResponse('404 - not found')        



def handlelogout(request):
    logout(request)
    messages.success(request,'Succesfully logged out')
    return redirect('/')
    

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm password']

        if len(username)>10:
            messages.error(request,'should notbe more then 10 chararcters')
            return redirect('/')
        
        if not username.isalnum():
            messages.error(request,'must contain only alphabets and numbers')
            return redirect('/')
        
        if password != confirm_password :
            messages.error(request,'password not matched')
            return redirect('/')


        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,'your account has been created succesfully!')
        return redirect('/')
    else :
        return HttpResponse('404')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        return render(request,'shop/contact.html')
    else:
        return render(request,'shop/contact.html')

def products(request, myid):
    
    product = Product.objects.filter(product_id = myid)
    
    
    return render(request,'shop/products.html',{'product':product[0]})

def checkout(request):
    states = ['Andhra Pradesh','Arunachal Prades','Assam','Bihar','Chhatisgarh','Delhi','Goa','Gujarat','Hayana','Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Orissa','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttaranchal','Uttar Pradesh','West Bengal','Andaman & Nicobar islands','Chandigarh','Dadar and Nagar Haveli','Daman and Diu','Lakshdeep','Pondicherry']

    if request.method == "POST":
        items_json = request.POST.get('itemsJson','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        pincode = request.POST.get('pincode','')
        order = Orders(items_Json=items_json,name=name,email=email,phone=phone,address=address,city=city,state=state,pincode=pincode)
        order.save()
        thank = True
        return render(request,'shop/checkout.html',{'states':states,'thank':thank})

    
    return render(request,'shop/checkout.html',{'states':states})