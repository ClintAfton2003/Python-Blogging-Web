# Create your views here.
from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request): 
  return render(request,'page/home.html')

def contact(request):
  return render(request,'page/contact.html')

def register(request):
  form = RegistrationForm()
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/login')
  return render(request, 'page/register.html', {'form': form})

def Login(request):
  if request.method=="POST":
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
      login(request, user)
      messages.success(request, "Successfully Logged In")
      return HttpResponseRedirect("/")
    else:
      messages.error(request, "Invalid Credentials")
    return render(request, 'page/login.html') 
  return render(request, "page/login.html")

def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return HttpResponseRedirect('/login')

