from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth.models import Group

# Create your views here.

def signup(request):
    variables = {
        'form':CustomUserCreationForm
    }
    if request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='voluntario')
            user.groups.add(group)
            variables['mensaje'] = "Usuario registrado!"
        else:
            variables['mensaje'] = "No se ha podido registrar"
            variables['form'] = form
    return render(request,'registration/signup.html', variables)
