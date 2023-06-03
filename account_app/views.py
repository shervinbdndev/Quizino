from typing import (Self, Union)
from django.urls.base import reverse
from django.views.generic.base import View
from django.http.request import HttpRequest
from django.contrib.auth.models import User
from django.shortcuts import (render, redirect)
from django.contrib.auth import (authenticate, login, logout)
from django.http.response import (HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect)
from .forms import (LoginForm, RegisterForm)








class LoginView(View):
    def get(self: Self, request: HttpRequest) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponse]:
        if (request.user.is_authenticated):
            return redirect(to=reverse(viewname='quiz_page'))
        else:
            form = LoginForm()
            return render(request, 'account_app/login.html', {'form': form})

    def post(self: Self, request: HttpRequest) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect, HttpRequest]:
        form = LoginForm(request.POST)
        if (form.is_valid()):
            cd = form.cleaned_data
            user = authenticate(username=cd['fullname'], password=cd['password'])

            if (user is not None):
                login(request, user)
                return redirect(to=reverse(viewname='quiz_page'))
            else:
                form.add_error('fullname', 'کاربری با این مشخصات وجود ندارد')

        return render(request, 'account_app/login.html', {'form': form})








class RegisterView(View):
    def get(self: Self, request: HttpRequest) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponse]:
        if (request.user.is_superuser):
            form = RegisterForm()
            return render(request, 'account_app/register.html', {'form': form})
        elif (request.user.is_authenticated):
            return redirect(to=reverse(viewname='quiz_page'))
        else:
            return redirect(to=reverse(viewname='login_page'))

    def post(self: Self, request: HttpRequest) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect, HttpRequest]:
        form = RegisterForm(request.POST)
        if (form.is_valid()):
            cd = form.cleaned_data
            if (cd['password'] != cd['conf_pass']):
                form.add_error('password', 'کدملی شما با یکدیگر مطابقت ندارد')
            else:
                fullname = f"{cd['first_name']} {cd['last_name']}"
                user = User.objects.create_user(
                    username=fullname,
                    first_name=cd['first_name'],
                    last_name=cd['last_name'],
                    email=cd['email'],
                    password=cd['password'],
                )
                login(request, user)
                return redirect(to=reverse(viewname='quiz_page'))
        else:
            form.add_error('password', 'اطلاعات غلط وارد شده')

        return render(request, 'account_app/register.html', {'form': form})
    
    




class LogoutView(View):
    def get(self: Self, request: HttpRequest):
        logout(request=request)
        return redirect(to=reverse(viewname='login_page'))