import pickle
#from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


def predict():
    tweets = pickle.load(open('prep_tweets.p'))
    Cvectorizer = joblib.load('Vocabs.pk1')
    IDFTransform = joblib.load('IDF.pk1')
    X = Cvectorizer.transform(tweets)
    print "#### Vectors created from tweets ####"
    print "X.shape - {}".format(X.shape)
    #TODO - transform to tf-idf weights
    X_tf_idf = IDFTransform.transform(X)
    print "#### IDF Vectors created  ####"
    clf = joblib.load('SVMclf.pk1')
    
    print "#### Predicting .... ####"
    result = clf.predict(X_tf_idf)
    result = [int(r) for r in result]
    print "Results- {}".format(result)

    return result

if __name__ == "__main__":
    results = predict()
    for res in results:
        print "Positive" if res > 0 else "Negative"
