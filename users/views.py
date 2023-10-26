from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser


#class AdminLogoutView(LogoutView):
#    template_name = 'admin/login.html'

def customer(request):
  return render(request, "users/customer_login.html")


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        passwd = request.POST.get('passwd')
        if not email or not passwd:
            messages.warning(request, "Please enter email and password both for login!")
            return redirect('customer')
        user = authenticate(
            username=email,
            password=passwd,
        )
        if user is not None:
            login(request, user)
            messages.success(request, "Welocome to the mobile finanace management! You have been logged in successfully!")
            return redirect('home')
        else:
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                user = None
            if user is None:
                messages.error(request, "This user does not exist!")
                return redirect('customer')
            else:
                messages.error(request, "Invalid login credentials!")
                return redirect('customer')
    messages.info(request, "Please enter email and password for login!")
    return redirect('customer')

def home(request):
  return render(request, "users/home.html")
