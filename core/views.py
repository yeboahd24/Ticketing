from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Profile
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Tictet

# Create your views here.


def index(request):
    ticket = Tictet()
    if request.method == "POST":
        ticket.fullname = request.POST.get('fullname', '')
        ticket.email = request.POST.get('email', '')
        ticket.number_of_person = request.POST.get('person', '')
        ticket.ticket_type = request.POST.get('position', '')
        ticket.date = request.POST.get('date', '')
        ticket.save()
    else:
        ticket = Tictet()

    return render(request, 'index.html', {'ticket': ticket})


def signup(request):

    if request.method == "POST":
        form = Profile(request.POST)
        form.username = request.POST.get('username', '')
        form.email = request.POST.get('email', '')
        form.password = request.POST.get('password', '')
        form.password2 = request.POST.get('password2', '')
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('index')
        else:
            return HttpResponse("Invalid form ")

    else:
        form = Profile()
    return render(request, 'login.html', {"form": form})


def user_login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        form.username = request.POST.get('username', '')
        form.password = request.POST.get('password', '')

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password']
            )
            if user is None:
                return HttpResponse('Invalid login')

            if not user.is_active:
                return HttpResponse('Disabled account')

            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Invalid form")
    else:
        form = LoginForm()
    return render(request, 'user_login.html', {'form': form})
