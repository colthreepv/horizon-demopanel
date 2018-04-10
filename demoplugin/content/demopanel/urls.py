from django.conf.urls import url

from demoplugin.content.demopanel import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
