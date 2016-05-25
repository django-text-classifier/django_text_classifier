from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from .models import TrainingSet


"""Objects should be saved to the table before running fit_data"""


def get_pipeline(name):
    x = TrainingSet.objects.filter(classifier=name).values_list('body',
                                                                flat=True)
    y = TrainingSet.objects.filter(classifier=name).values_list('target',
                                                                flat=True)
    print('-' * 30)
    print('X: ', x)
    print('y: ', y)
    print('-' * 30)
    pipeline = Pipeline([
         ('vector', CountVectorizer()),
         ('transform', TfidfTransformer()),
         ('bayes', MultinomialNB())
    ])

    pipeline.fit(x, y)

    return pipeline


def fit_predict(name, body):
    pipeline = get_pipeline(name)
    return pipeline.predict(body)
