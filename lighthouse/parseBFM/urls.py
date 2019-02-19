from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'parseBFM'


urlpatterns = [
    #Parse BFMRQ
    path('CreateBFM_Parse', views.CreateBFM_Parse.as_view(), name='CreateBFM_Parse'),
    path('BFM_ParseDetail/<int:pk>/', views.BFM_ParseDetail.as_view(), name='BFM_ParseDetail'),


]
