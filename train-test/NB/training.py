#import csv
import pickle
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
import numpy as np 
import sys
from sklearn import cross_validation

linenum = 0
tweet = []
sent = []

tweet = pickle.load(open(sys.argv[1]))
sent = pickle.load(open(sys.argv[2]))
print '[log]-Done loading data'

Cvectorizer = CountVectorizer(decode_error='ignore',stop_words='english',lowercase=False)

tfidfTransform = TfidfTransformer()
X = Cvectorizer.fit_transform(tweet)
Y = np.array(sent)

print '[log]-Done count transform'

#TODO - transform to tf-idf weights
X_tf_idf = tfidfTransform.fit_transform(X)
print '[log]-Done tfidf transform'

#train_X,test_X,train_Y,test_Y = cross_validation.train_test_split(X_tf_idf,Y,test_size=0.3,random_state=0)#simple cross validation
kf = cross_validation.StratifiedKFold(sent,n_folds=10)
print '[log]-Done cross validation'

for train_index, test_index in kf:
	#using NB classifier
	clf = MultinomialNB(alpha=0.08).fit(X_tf_idf[train_index], Y[train_index])
	#using SVM classifier
	#clf = svm.SVC(kernel = 'linear', C=1).fit(X_tf_idf[train_index],Y[train_index]) 
	print '[log]-Done training clf'

	#TODO - Test the classifier
	result = clf.predict(X_tf_idf[test_index])
	#print result
 	print "Total score-%s"%clf.score(X_tf_idf[test_index],Y[test_index])

#joblib.dump(clf,'NBclf.pk1')
#joblib.dump(Cvectorizer,'Vocabs.pk1')
#joblib.dump(tfidfTransform,'IDF.pk1')

#print '[log]- done with dumping'
