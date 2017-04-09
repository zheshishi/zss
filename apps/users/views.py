from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password

from common.form import invalid_msg
from .models import AuthUser
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm


# Create your views here.

@login_required
def index(request):
    '''后台首页'''
    return render(request, 'index.html')


@login_required
def logout(request):
    '''注销登录'''
    auth.logout(request)
    return redirect('login')


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if not form.is_valid():
            errors = {key: invalid_msg.format(value[0]) for key, value in form.errors.items()}
            return render(request, self.template_name, {'error': errors, 'form': form})

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = AuthUser()
        user.username = username
        user.password = make_password(password)
        user.is_active = False
        user.save()

        return redirect('login')


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if not form.is_valid():
            errors = {'username': invalid_msg.format(value[0]) for key, value in form.errors.items()}
            return render(request, self.template_name, {'error': errors, 'form': form})

        auth.login(request, form.user)
        return redirect('home')
