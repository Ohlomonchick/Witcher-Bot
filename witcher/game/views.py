from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView

from game.models import Profile


class Home(ListView):
    # paginate_by = 15
    model = Profile
    template_name = 'game/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список лидеров'
        return context

    def get_queryset(self):
        return Profile.objects.all()
