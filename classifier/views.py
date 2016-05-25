from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework import viewsets
from .models import TrainingSet
from .serializers import TrainingSetSerializer
from .classifier import *


""" User views """


class Classifier(TemplateView):
    template_name = "classifier/classifier.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = TrainingSet.objects.all()
        return context

    def post(self, request, name):
        body = request.POST.get('body')
        target = request.POST.get('target')
        classifier = name
        data = TrainingSet.objects.create(classifier=classifier,
                                          target=target, body=body)
        data.save()

        return render(request, self.template_name,
                      context=self.get_context_data())

    def get(self, request, name):
        context = self.get_context_data()
        context['name'] = name
        if request.GET.get('test'):
            context['predicted'] = fit_predict(name, request.GET.get('test'))

        return render(request, self.template_name, context)


def index(request):
    context = {}
    return render(request, 'classifier/index.html', context)


"""API Endpoint"""


class TrainingSetViewSet(viewsets.ModelViewSet):
    queryset = TrainingSet.objects.all().order_by('body')
    serializer_class = TrainingSetSerializer
