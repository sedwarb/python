#from django.conf.urls import urls
from django.urls import urls
from . import views

urlpatterns = [
    urls(r'^$', views.index, name="index")
]