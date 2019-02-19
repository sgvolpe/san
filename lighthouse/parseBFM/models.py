import json

from django.db import models

from django.urls import reverse
# Create your models here.


class BFM_Parse(models.Model):
    bfm_rs_file = models.FileField(blank=False)
    #bfm_rs_df = pd.DataFrame()#models.CharField(max_length=255, blank=True)

    def parse(self):
        bfmrs_json = json.loads(self.bfm_rs_file.open().read())
        #self.bfm_rs_df = bfmrs_json# BargainFinderMaxRQ.bfm_rs_to_df(bfmrs_json, RET='ROCK')
        return bfmrs_json #BargainFinderMaxRQ.bfm_rs_to_df(bfmrs_json, RET='ROCK')


    def get_absolute_url(self):
        return reverse("parseBFM:BFM_ParseDetail",kwargs={"pk": self.pk})
