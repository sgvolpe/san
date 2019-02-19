from django.views.generic import TemplateView
from django.template import Template
from django.shortcuts import render


class HomePage(TemplateView):
    template_name = 'index.html'
