from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('index/', views.HomePage.as_view(), name='index'),
    path('parseBFM/', include('parseBFM.urls', namespace='parseBFM')),
    path('accounts/', include('accounts.urls', namespace='accounts')),

]
