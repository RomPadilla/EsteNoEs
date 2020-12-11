from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.views import generic

from django.contrib.auth.models import User

from .forms import createUserForm

from django.contrib import messages

from django.contrib.auth import authenticate, login

from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required

# Create your views here.

def formularioRegistro(request):
	data = {
		'form':createUserForm()
	}
	if request.method == 'POST':
		formulario = createUserForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			user = formulario.save()
			username = formulario.cleaned_data.get('username')
			group = Group.objects.get(name='Usuario')
			user.groups.add(group)
			login(request, user)
			return redirect('User')
		data["form"] = formulario

	return render(request, 'FormularioRegistro.html', data)

@login_required
def user(request):

    return render(
        request,
        'User.html',
        context={},
        )

