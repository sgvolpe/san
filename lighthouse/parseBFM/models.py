import json, requests

from django.db import models

from django.urls import reverse
# Create your models here.

PROXY_USER='sg0216333'
PROXY_PASSWORD='Santito!!!'
PROXY_URL='www-ad-proxy.sabre.com:80'


class BFM_Parse(models.Model):
    bfm_rs_file = models.FileField(blank=False,upload_to='static/folder/')
    bfm_rs_json = models.TextField(null=True, blank=True)

    def parse(self):
        if self.bfm_rs_json is None:
            return json.loads(self.bfm_rs_file.open().read())
        else: return json.loads(self.bfm_rs_json)

    def get_absolute_url(self):
        return reverse("parseBFM:BFM_ParseDetail",kwargs={"pk": self.pk})


class sendbfm(models.Model):
    bfm_rq_file = models.FileField(blank=False)
    token = models.CharField(max_length=300, blank=False)
    parsebfm = models.ForeignKey('BFM_Parse',on_delete=models.CASCADE, null=True, blank=True)


    def send_rq(self):
        payload = json.loads(self.bfm_rq_file.open().read())
        url = 'https://api.sabre.com/v4.3.0/shop/flights?mode=live'
        headers = {'content-type': 'application/json','Authorization': 'Bearer ' + str(self.token)}
        proxies = {"https": f"https://{PROXY_USER}:{PROXY_PASSWORD}@{PROXY_URL}",}
        print (f'Sending: {url} {self.token}')
        response = requests.post(url, headers=headers,data=json.dumps(payload), proxies=proxies)

        return response.text



    def get_absolute_url(self):
        return reverse("parseBFM:BFM_ParseDetail",kwargs={"pk": self.parsebfm.pk})
