from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView


#class AdminLogoutView(LogoutView):
#    template_name = 'admin/login.html'

def customer(request):
  return render(request, "users/customer_login.html")

def home(request):
  return render(request, "users/home.html")
