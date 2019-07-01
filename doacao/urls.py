from django.conf.urls import url
from . import views

app_name = 'doacao'

urlpatterns = [
    url(r'^$', views.doacao_view, name='doacao'),
]
