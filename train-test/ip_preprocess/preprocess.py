import csv
import porter
import pickle
import re

url ='http:\\/\\/[a-zA-Z0-9\/\.&?=:%]+|https:\\/\\/[a-zA-Z0-9\/\.&?=:%]+' 
username ='@\w+'
hashtags = '#\w+'

input_file  = open("","rb")
reader = csv.reader(input_file)

linenum = 0
tweet = []
sent = []

#for row in reader:
#	sent.append(row[0])
#	tweet.append(row[1])

#print '[log]-Done reading csv'

for line in f
input_file.close()

#use porter to stem english words 
stemmed_tweets = []
p = porter.PorterStemmer()
for t in tweet:
    t_n = re.sub(url+'|'+username,'', t, flags=re.MULTILINE)
    t_n.strip()
    tweet_list = t_n.split()
    s =''
    for w in tweet_list:
            s_w = p.stem(w,0,len(w)-1)
            s = s +' '+s_w
    
    s = s.strip()
    stemmed_tweets.append(s)

print '[log]- stemming done'

pickle.dump(stemmed_tweets,open('prep_tweets.p','wb'))
pickle.dump(sent,open('prep_labels.p','wb'))

