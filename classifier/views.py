from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework import viewsets
from .models import TrainingSet
from .serializers import TrainingSetSerializer


""" User views """


class Classifier(TemplateView):
    template_name = "classifier/classifier.html"

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['data'] = TrainingSet.objects.all()
    return context

def post(reqeust):
    pass


def index(request):
    context = {}
    return render(request, 'classifier/index.html', context)




"""API Endpoint"""


class TrainingSetViewSet(viewsets.ModelViewSet):
    queryset = TrainingSet.objects.all().order_by('body')
    serializer_class = TrainingSetSerializer
