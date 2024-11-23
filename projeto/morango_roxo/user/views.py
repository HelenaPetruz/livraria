from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method=='POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.get('username')
			messages.success(request, "Usuário cadastrado!")
			#return render(request, 'user/login.html')
	else:
		form = UserRegisterForm()
		return render(request, 'user/registro.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            messages.success(request, f'Conta atualizada com sucesso!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)

    context = {
        'u_form': u_form
    }
    return render (request, 'use/profile.html', context)
