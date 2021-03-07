from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# from .forms import InputForm
from .models import Emp, Man

from .forms import ContactForm


# Views
@login_required
def home(request):
    return render(request, "registration/success.html", {})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def maker(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            emp = form.cleaned_data['empid']
            name = form.cleaned_data['name']
            mail = form.cleaned_data['email']
            # man = form.cleaned_data['man']
            p = Emp.objects.create(emp=emp, name=name, mail=mail)
            # q = Man.objects.create(man=man, emp=emp)
            # messages.success(request, 'Form submission successful')
            return HttpResponseRedirect(request.path_info)
    return render(request, 'registration/form.html', {'form': form})


def index(request):
    student = Emp.objects.all()
    return render(request, 'registration/database.html', {'emp': student})
