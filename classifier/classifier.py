from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
from sklearn.pipeline import Pipeline
from .models import TrainingSet


"""Objects should be saved to the table before running fit_data"""


def get_pipeline(name):
    x = TrainingSet.objects.filter(classifier=name).value_list('body',
                                                               flat=True)
    y = TrainingSet.objects.filter(classifier=name).value_list('target',
                                                               flat=True)
    pipeline = Pipeline([
         ('vector', CountVectorizer()),
         ('transform', TfidfTransformer()),
         ('bayes', MultinomialNB())
    ])

    pipeline.fit(x, y)

    return pipeline


def predict(pipeline, data):
    return pipeline.predict(data)


def fit_predict(name, data):
    pipeline = get_pipeline(name)
    return pipline.predict(data)
