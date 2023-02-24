from django.shortcuts import render, redirect
from django.contrib import auth
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse

from .forms import LoginForm, RegForm

User = get_user_model()

# Create your views here.
def login(request):
    ''''
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(request, username=username, password=password)
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    if user is not None:
        auth.login(request, user)
        # Redirect to a success page
        return redirect(referer)
    else:
        # Return an 'invalid login' error message
        return render(request, 'error.html', {'message':'用户名或密码不正确'})
    '''
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # form.cleaned_data:normalizing it to a consistent format
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            # if true: 'from'; if false: reverse('home')
            return redirect(request.GET.get('from', reverse('home')))
    else:
        login_form = LoginForm()

    context = {}
    context['login_form'] = login_form
    return render(request, 'login.html', context)

def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # create a new account
            user = User.objects.create_user(username, email, password)
            user.save()
            # login
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        reg_form = RegForm()
    context = {}
    context['reg_form'] = reg_form
    return render(request, 'register.html', context)


def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from', reverse('home')))

def user_info(request):
    context = {}
    return render(request, 'user_info.html', context)
