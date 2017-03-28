import pickle
#from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

tweets = pickle.load(open('prep_tweets.p'))
Cvectorizer = joblib.load('Vocabs.pk1')
IDFTransform = joblib.load('IDF.pk1')

X = Cvectorizer.transform(tweets)
#TODO - transform to tf-idf weights
X_tf_idf = IDFTransform.transform(X)
 
clf = joblib.load('SVMclf.pk1')
result = clf.predict(X_tf_idf)

for r in result:
        print r

