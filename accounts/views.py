from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail

from django.contrib import messages

from .forms import CreateUserForm, OrderForm

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
    
  context = {}
  return render(request, 'accounts/home.html', context)

def contact(request):

  if request.method == "POST":
    ContactForm_name = request.POST['contact[名稱]']
    ContactForm_email = request.POST['contact[email]']
    ContactForm_phone = request.POST['contact[電話號碼]']
    ContactForm_message = request.POST['contact[訊息]']

    send_mail(
			'message from' + ContactForm_name, # subject
			ContactForm_message, # message
			ContactForm_email, # from mail
			['s25681880@gmail.com'], # to mail

			)
      
    return render(request, 'accounts/contact.html', {'ContactForm_name':ContactForm_name})
  else:
    return render(request, 'accounts/contact.html', {})


class MenuView(ListView):
    model = Dishes
    form_class = OrderForm
    template_name = 'accounts/menu.html'

    
    