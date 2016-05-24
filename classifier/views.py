from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework import viewsets
from .models import TrainingSet
from .serializers import TrainingSetSerializer


""" User views """


class Classifier(TemplateView):
    template_name = "classifier/classifier.html"


def index(request):
    context = {}
    return render(request, 'classifier/index.html', context)


"""API Endpoint"""


class TrainingSetViewSet(viewsets.ModelViewSet):
    queryset = TrainingSet.objects.all().order_by('body')
    serializer_class = TrainingSetSerializer
