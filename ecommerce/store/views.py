from django.contrib.auth import authenticate, login
from django.db.models.fields.related import ForeignKey
from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from .forms import RegisterForm, LoginForm
from .models import *
import json
from django.http.response import Http404
from django.http import JsonResponse
# Create your views here.

def login_request(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            form = LoginForm()
            return render(request,'registration/login.html',{'form':form})
     
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form':form})

def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            vartotojas= User.objects.get(username=request.POST.get('username'))
            kustomeris= Customer.objects.create(user=vartotojas,name=request.POST.get('username'), email=request.POST.get('email'))
            return redirect("/")
           
    else:
            form = RegisterForm()
    
    return render(request, "store/register.html", {"form":form})

def store(request):
    if request.user.is_authenticated:
        customer=Customer.objects.get(user =request.user)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order["get_cart_items"]
    products = Product.objects.all()
    context = {"products": products, "cartItems": cartItems}
    return render(request, "store/store.html", context)


def cart(request):
    if request.user.is_authenticated:
        customer=Customer.objects.get(user =request.user)
        order, created =Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0}
        cartItems = order["get_cart_items"]
    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer=Customer.objects.get(user =request.user)
        order, created =Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0}
        cartItems = order["get_cart_items"]
    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, 'store/checkout.html', context)

def search(request):
    try: 
        q=request.GET.get('q')
    except:
     q= None
    if q:
        products=Product.objects.filter(name__icontains=q)
        context = {'products':products}
        template='store/search.html'
    else:
        template='store/index.html'
        context={}
    return render(request,template,context)

def single(request,slug):
    try:
        product=Product.objects.get(slug=slug)
        context = {'product':product}
        return render(request, 'store/single.html', context)
    except:
        raise Http404

def updateItem(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    print("Action:", action)
    print("productId:", productId)
    customer=Customer.objects.get(user =request.user)
    
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderItem.quantity = orderItem.quantity + 1
    elif action == "remove":
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse("Item was added", safe=False)


def proccesOrder(request):
    print ('Data',request.body)
    return JsonResponse("Payment complete", safe=False)
