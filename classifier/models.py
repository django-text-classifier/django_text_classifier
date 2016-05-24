from django.db import models


class TrainingSet(models.Model):
    body = models.TextField()
    target = models.CharField(max_length=255)

    def __str__(self):
        return '{}: {}'.format(self.body[20], self.target)
