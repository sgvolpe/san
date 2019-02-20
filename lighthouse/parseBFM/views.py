from django.shortcuts import render

# Create your views here.

from . import models

from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from .models import BFM_Parse
from django.views.generic import (TemplateView, ListView)


class Createsendbfm(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    model = models.sendbfm
    template_name = "BFM_Parse/sendbfm_form.html"
    fields = ('bfm_rq_file','token')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        bfmp = BFM_Parse()

        bfmp.bfm_rs_json =self.object.send_rq()
        bfmp.save()
        self.object.parsebfm = bfmp
        self.object.save()
        return super().form_valid(form)

class CreateBFM_Parse(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    model = models.BFM_Parse
    template_name = "BFM_parse/BFM_Parse_form.html"
    fields = ('bfm_rs_file',)



class BFM_ParseDetail(SelectRelatedMixin, generic.DetailView):
    model = models.BFM_Parse
    select_related = ()
    template_name = "BFM_parse/BFM_Parse_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bfm_rs'] =self.object.parse()
        return context


class BFM_ParseListView(ListView):
    model = models.BFM_Parse
    template_name = "BFM_parse/BFM_Parse_list.html"
    select_related = ()
    
    def get_queryset(self):
        return BFM_Parse.objects.all()
