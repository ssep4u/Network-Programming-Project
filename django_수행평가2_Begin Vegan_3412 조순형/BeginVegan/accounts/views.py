from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import RegisterForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'begin_vegan/index.html')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next') or 'begin_vegan:index')
        else:
            return render(request, 'accounts/login_fail.html')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def my_logout(request):
    logout(request)
    return redirect('begin_vegan:index')

