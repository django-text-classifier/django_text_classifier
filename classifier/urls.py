from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Index.as_view(), name="home"),
    url(r'^classifier/(?P<name>[a-zA-Z]+)/', views.Classifier.as_view(), name="classifier"),

]
