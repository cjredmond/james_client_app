from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from workout.models import Workout
from user_auth.models import Account

class WorkoutCreateView(CreateView):
    model = Workout
    success_url = "/"
    fields = ('name', 'info')
    def form_valid(self,form,**kwargs):
        instance = form.save(commit=False)
        target = Account.objects.get(id=self.kwargs['pk'])
        instance.account = target
        return super().form_valid(form)

class WorkoutArchiveView(UpdateView):
    model = Workout
    success_url = "/"
    fields = []
    def form_valid(self,form,**kwargs):
        instance = form.save(commit=False)
        instance.archive = True
        instance.save()
        return super().form_valid(form)
