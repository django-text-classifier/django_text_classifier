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
        return context

    def post(self, request, name):
        context = self.get_context_data()
        if request.POST.get('body'):
            body = request.POST.get('body')
            target = request.POST.get('target')
            classifier = name
            data = TrainingSet.objects.create(classifier=classifier,
                                              target=target, body=body)
            data.save()
        elif request.POST.get('correct'):
            body = request.POST.get('correctBody')
            target = request.POST.get('correctTarget')
            classifier = name
            data = TrainingSet.objects.create(classifier=classifier,
                                              target=target, body=body)
            data.save()
        else:
            print('File')
            handle_uploaded_file(request.FILES['csvfile'], name)
        context['data_size'] = len(TrainingSet.objects.filter(classifier=name).values_list('body', flat=True))
        return render(request, self.template_name,
                      context)

    def get(self, request, name):
        context = self.get_context_data(name=name)
        context['name'] = name
        context['data_size'] = len(TrainingSet.objects.filter(classifier=name).values_list('body', flat=True))
        if request.GET.get('text'):
            context['text'] = request.GET.get('text')
            data_size = len(TrainingSet.objects.filter(classifier=name).values_list('body', flat=True))
            pipeline = get_pipeline(name)
            prediction = fit_predict(pipeline, (request.GET.get('text'), ))
            context['predicted'] = prediction[0]
            context['data_size'] = data_size

        return render(request, self.template_name, context)


class Index(TemplateView):
    classifiers = TrainingSet.objects.values('classifier').distinct()
    context = {'classifiers': classifiers}
    template_name = "classifier/index.html"

    def get(self, request):
        if request.GET.get('classifier'):
            classifier = request.GET.get('classifier')
            for ch in [".", "-", ",", "_", "/", "%", " "]:
                if ch in classifier:
                    classifier = classifier.replace(ch, "")
            url = '/classifier/{}/'.format(classifier)
            return redirect(url)
        else:
            return render(request, self.template_name, self.context)


"""API Endpoint"""


class TrainingSetViewSet(viewsets.ModelViewSet):
    queryset = TrainingSet.objects.all().order_by('body')
    serializer_class = TrainingSetSerializer
