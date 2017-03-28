import re
import sys
import pickle
input_file = open("POS_input.txt","rb")
tweets=[]
s=''
line_num=0
not_switch = 0
pos_fetched = ['N','V','^','A','R','!','&',',']
pos_avoid = ['@','U','D']
#p = porter.PorterStemmer()

for line in input_file:
	#line=line.strip()
	#print "[log]- Tweet no-%d"%line_num

	try:
	    line = unicode(line, "ascii")
  	except UnicodeError:
            line = unicode(line, "utf-8",errors='ignore')
	else:
            pass
	
	if line == '\n':
		tweets.append(s)
		s=''
		line_num = line_num+1
		continue

	m = re.split('\t',line)
	token = m[0]
	pos = m[1]
	conf = m[2]


	if pos not in pos_avoid:#or pos in pos_fetched whichever is better
		#s_token = p.stem(token,0,len(token)-1)#change if necessary
		s = s+' '+token
		s=s.strip()
		 

pickle.dump(tweets,open('prep_tweets.p','wb'))
input_file.close()

