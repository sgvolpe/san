from django.shortcuts import render

# Create your views here.

from . import models

from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic

class CreateBFM_Parse(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    model = models.BFM_Parse
    template_name = "BFM_Parse/BFM_Parse_form.html"
    fields = ('bfm_rs_file',)

    #def form_valid(self, form):

    #    self.object = form.save(commit=False)
    #    self.object.save()
    #    self.object.bfm_rs_df = parse()
    #    self.object.save()
    #    return super().form_valid(form)



class BFM_ParseDetail(SelectRelatedMixin, generic.DetailView):
    model = models.BFM_Parse
    select_related = ()
    template_name = "BFM_Parse/BFM_Parse_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print ('----')

        #context['app'] = dashboard_app.getapp(df_path)
        bfm_rs_json = self.object.parse()        
        context['bfm_rs'] =bfm_rs_json
        return context
