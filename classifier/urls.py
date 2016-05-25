from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    # url(r'^$', RedirectView.as_view(url='/home/', permanent=False),
    #     name='redirect'),
    url(r'^$', views.index, name="home"),
    url(r'^classifier/(?P<name>[a-zA-Z]+)/', views.Classifier.as_view(), name="classifier"),

]
