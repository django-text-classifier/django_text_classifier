from rest_framework import serializers
from .models import TrainingSet


class TrainingSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrainingSet
        fields = '__all__'
