from django.shortcuts import render, redirect
from .forms import RegisterUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signupPage_view(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            messages.success(request, f"You have successfully registered as {username} ")
            form = RegisterUser()
            
    else:
        form = RegisterUser()
    params = {'form': form, 'title': 'SignUp'}
    return render(request, 'signup.html', params)


def signin_view(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
        else:

            messages.error(
                request, 'Username and Password didnot match. Try again ')
    return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('home')
