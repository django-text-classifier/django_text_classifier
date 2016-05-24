from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from classifier import views

router = routers.DefaultRouter()
router.register(r'texts', views.TrainingSetViewSet)


urlpatterns = [
    url(r'^', include('classifier.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
