
# coding: utf-8

# In[1]:

#importing packages
import requests
import json


# In[2]:

#link for downloading json file
url = "http://kevincrook.com/utd/tweets.json"


# In[3]:

#downloading json tweets
r = requests.get(url).json()


# In[4]:

#list of tweets
s = []
for i in range(len(r)):
    if 'text' not in r[i]:
        continue
    s.append(r[i])         


# In[5]:

#list of languages
t = []
for i in range(len(s)):
    t.append(s[i]['lang'])
u = set(t)    


# In[6]:

#frequency of each language 
def frequency(i):
    a = t.count(i)
    return(a)


# In[7]:

#sorting the languages
lafq = []
for i in u:
    lafq.append([i,frequency(i)])
defq = sorted(lafq, key = lambda x: x[1], reverse = True)


# In[8]:

#creating twitter analytics text file
x = open('twitter_analytics.txt', 'w', encoding = 'utf-8')
x.write('%d\n' %len(r))
x.write('%d\n' %len(s))
for i in defq:
    x.write('%s,%d\n' %(i[0],i[1]))
x.close()


# In[9]:

#creating tweets text file
y = open('tweets.txt', 'w')
for i in s:
    y.write((i['text'].encode('unicode-escape')).decode('utf-8')+'\n')
y.close()    

