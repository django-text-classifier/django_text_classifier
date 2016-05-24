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

    def get(request):
        context['classified_data'] = classsifier.classify(request.GET.get('train'), request.GET.get('target'))

        return render(request, '/classifier/books', context)

    def post(request):
        pass


def index(request):
    context = {}
    return render(request, 'classifier/index.html', context)


"""API Endpoint"""


class TrainingSetViewSet(viewsets.ModelViewSet):
    queryset = TrainingSet.objects.all().order_by('body')
    serializer_class = TrainingSetSerializer
