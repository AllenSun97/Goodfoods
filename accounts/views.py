from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
import datetime
from django.views.generic import ListView

from .models import *
from .utils import cartData
from django.contrib.auth import *
from django.core.mail import send_mail

from django.contrib import messages

from .forms import CreateUserForm, OrderItemsForm

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
  
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def registerPage(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def home(request):
    data = cartData(request)
    cartItems = data['cartItems']

    context = {'cartItems':cartItems}
    return render(request, 'accounts/home.html', context)

def contact(request):
    data = cartData(request)
    cartItems = data['cartItems']

    if request.method == "POST":
        ContactForm_name = request.POST['contact[名稱]']
        ContactForm_email = request.POST['contact[email]']
        ContactForm_phone = request.POST['contact[電話號碼]']
        ContactForm_message = request.POST['contact[訊息]']

        send_mail(
            'message from' + ContactForm_name, # subject
            ContactForm_message, # message
            ContactForm_email, # from mail
            ['s25681880@gmail.com'], # to mail hihi
            )
        
        return render(request, 'accounts/contact.html', {'ContactForm_name':ContactForm_name, 'cartItems':cartItems})
    else:
        return render(request, 'accounts/contact.html', {'cartItems':cartItems})

def add_to_cart(request, pk):
    customer = request.user.customer
    order_id, created = Order.objects.get_or_create(customer=customer, complete=False)
    item_id = Dishes.objects.get(pk=pk)
    form = OrderItemsForm(request.POST or None,initial={'dishes':item_id, 'order':order_id})
  
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return render(request, 'accounts/menu.html')

    context = {'form':form, 'dish':item_id, 'order_id':order_id}
    return render(request,'accounts/add_to_cart.html', context)

class MenuView(ListView):
    model = Dishes
    form_class = OrderItemsForm
    template_name = 'accounts/menu.html'

# yt Django Ecommerce Website
def cart(request):
    # clear this by moving the code to utils.py 'cartData' function Pt4
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'accounts/cart.html', context)

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'accounts/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)#the body we sent thru fetch
    dishId = data['dishId']
    action = data['action']

    print('Action:', action)
    print('productId:', dishId)

    customer = request.user.customer
    dish = Dishes.objects.get(id=dishId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItems, created = OrderItems.objects.get_or_create(order=order, dishes=dish)
    
    if action == 'add':
        orderItems.quantity += 1
    elif action == 'remove':
        orderItems.quantity -= 1
    
    orderItems.save()

    if orderItems.quantity <= 0:
        orderItems.delete()
        
    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    # transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        ShippingAddress.objects.create(
            customer = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],
        )
    else:
        print('User is not logged in ')
    return JsonResponse('Payment complete', safe=False)