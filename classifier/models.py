from django.db import models


class TrainingSet(models.Model):
    body = models.TextField()
    target = models.CharField(max_length=255)
    classifier = models.CharField(max_length=100)

    def __str__(self):
        return 'Classifier {} --> {}: {}'.format(self.classifier,
                                                 self.body[20], self.target)
