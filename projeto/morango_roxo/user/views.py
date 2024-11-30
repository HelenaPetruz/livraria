from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import FormRegister, FormLogin

def register(request):
    if request.method == 'POST':
        form = FormRegister(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Usuário registrado com sucesso!')
            return redirect('livraria')
    else:
        form = FormRegister()
    return render(request, 'user/registro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = FormLogin(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Credenciais inválidas.')
    else:
        form = FormLogin()
    return render(request, 'user/login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('login')
