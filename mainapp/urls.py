from django.conf.urls import url
from django.urls import path
from mainapp import views


urlpatterns = [
    url(r'^$', views.Main, name='Main'),
    url(r'^(?P<sith_slug>[-\w]+)$', views.SithPage, name='SithPage'),
    path('<int:id>/<recruit_email>', views.RecruitPage, name='RecruitPage'),
]
