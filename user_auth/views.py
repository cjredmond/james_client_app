from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from user_auth.models import Account

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    def get_success_url(self):
        return reverse('login')

class AccountDetailView(DetailView):
    model = Account
