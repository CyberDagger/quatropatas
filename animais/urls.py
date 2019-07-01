from django.conf.urls import url
from . import views

app_name = 'animais'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w-]+)/$', views.animal_details, name='animal'),
    url(r'^(?P<slug>[\w-]+)/adocao/$', views.adocao, name='adocao'),
]
