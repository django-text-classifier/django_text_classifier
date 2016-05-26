from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from .models import TrainingSet


"""Objects should be saved to the table before running fit_data"""


def get_pipeline(name):
    x = TrainingSet.objects.filter(classifier=name).values_list('body',
                                                                flat=True)
    y = TrainingSet.objects.filter(classifier=name).values_list('target',
                                                                flat=True)
    pipeline = Pipeline([
         ('vector', CountVectorizer()),
         ('transform', TfidfTransformer()),
         ('bayes', MultinomialNB())
    ])

    pipeline.fit(x, y)

    return pipeline


def fit_predict(pipeline, body):
    return pipeline.predict(body)


def get_score(pipeline, name):
    x = TrainingSet.objects.filter(classifier=name).values_list('body',
                                                                flat=True)
    y = TrainingSet.objects.filter(classifier=name).values_list('target',
                                                                flat=True)
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33)

    return pipeline.score(x, y)
