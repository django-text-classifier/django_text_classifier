from django.shortcuts import render
from rest_framework import viewsets
from .models import TrainingSet
from .serializers import TrainingSetSerializer


def index(request):
    context = {}
    return render(request, 'classifier/index.html', context)


class TrainingSetViewSet(viewsets.ModelViewSet):
    queryset = TrainingSet.objects.all().order_by('body')
    serializer_class = TrainingSetSerializer
