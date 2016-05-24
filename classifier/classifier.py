from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
from sklearn.pipeline import Pipeline
from .models import TrainingSet


pipeline = Pipeline([
     ('vector', CountVectorizer()),
     ('transform', TfidfTransformer()),
     ('bayes', MultinomialNB())
])


x = TrainingSet.objects.filter(classifier=url).value_list('body', flat=True)
y = TrainingSet.objects.filter(classifier=url).value_list('target', flat=True)
