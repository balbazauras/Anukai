from django.http.response import Http404
from django.shortcuts import redirect, render
from .forms import RegisterForm, LoginForm
from .models import *

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
            return redirect("/")
    else:
            form = RegisterForm()
    
    return render(request, "store/register.html", {"form":form})

def store(request):
    products=Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created =Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created =Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'order':order}
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
    