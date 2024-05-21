from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Resource
from django.contrib.auth import authenticate, login, logout
from .form import ContactForm
# Create your views here.

# login_required
from django.contrib.auth.decorators import login_required

@login_required(login_url='app:login')
def index(request):  
    form = ContactForm()
    resource = Resource.objects.all()
    user_name = request.user.email
    return render(request, 'index.html', {'form': form, 'resource': resource, 'user_name': user_name})

def login_page(request):
    print(User.objects.all())
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('app:index')

    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('app:login')