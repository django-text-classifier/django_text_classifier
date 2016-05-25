from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from rest_framework import viewsets
from .models import TrainingSet
from .serializers import TrainingSetSerializer
from .classifier import *
from .utilities import handle_uploaded_file


""" User views """


class Classifier(TemplateView):
    template_name = "classifier/classifier.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = TrainingSet.objects.all()
        return context

    def post(self, request, name):
        if request.POST.get('body'):
            body = request.POST.get('body')
            target = request.POST.get('target')
            classifier = name
            data = TrainingSet.objects.create(classifier=classifier,
                                              target=target, body=body)
            data.save()
        else:
            print('File')
            handle_uploaded_file(request.FILES['csvfile'], name)
        return render(request, self.template_name,
                      context=self.get_context_data())

    def get(self, request, name):
        context = self.get_context_data()
        context['name'] = name
        if request.GET.get('test'):
            prediction = fit_predict(name, (request.GET.get('test'), ))
            context['predicted'] = prediction[0]

        return render(request, self.template_name, context)


class Index(TemplateView):
    classifiers = TrainingSet.objects.values('classifier').distinct()
    context = {'classifiers': classifiers}
    template_name = "classifier/index.html"

    def get(self, request):
        if request.GET.get('classifier'):
            url = '/classifier/{}/'.format(request.GET.get('classifier'))
            return redirect(url)
        else:
            return render(request, self.template_name, self.context)


"""API Endpoint"""


class TrainingSetViewSet(viewsets.ModelViewSet):
    queryset = TrainingSet.objects.all().order_by('body')
    serializer_class = TrainingSetSerializer
