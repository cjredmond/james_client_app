from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from user_auth.models import Account
from workout.models import Workout

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    def get_success_url(self):
        return reverse('login')

class AccountDetailView(DetailView):
    model = Account
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Account.objects.filter(client=True)
        return context

@login_required
def home(request):
    return HttpResponseRedirect(
            reverse('account_detail_view',
                args=[request.user.account.id]))

class AccountArchivedWorkoutView(TemplateView):
    template_name = "archive.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        target = Account.objects.get(id=self.kwargs['pk'])
        context['workouts'] = Workout.objects.filter(archive=True,account=target)
        return context



    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     target = Account.objects.get(id=self.kwargs['pk'])
    #     context['workouts'] = Workout.objects.filter(archive=True,account=target)
    #     return context
