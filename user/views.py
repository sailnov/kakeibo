from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView

from .forms import LoginForm, SignUpForm


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = 'index'
    template_name = "user/signup.html"


class Login(LoginView):
    form_class = LoginForm
    success_url = 'index'
    template_name = "user/login.html"


class Logout(LogoutView):
    template_name = "user/logout.html"

'''
このviewsはログアウト及びログイン処理をしています。
DjangoのテンプレートであるLoginViewとLogoutView、CreateViewを継承して一部変更しています。
'''