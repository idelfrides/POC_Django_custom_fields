from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    """ Template views """
    template_name='home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home Page | DCF'
        context['me'] = 'Hello! My name is Idelfrides Jorge'
        context['frase'] = 'Home page project: django custom fields'
        return context