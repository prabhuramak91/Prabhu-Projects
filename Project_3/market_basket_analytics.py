
# coding: utf-8

# In[1]:

#Importing required packages
import pandas as pd
import numpy as np
import requests
from itertools import combinations


# In[2]:

#Link for downloading the training set
url = "http://kevincrook.com/utd/market_basket_training.txt"


# In[3]:

#Downloading the training set
p = requests.get(url)


# In[4]:

#Writing the set to a text file
r = open("Training.txt","wb")
r.write(p.content)
r.close()


# In[5]:

#List of products
items = ['P01', 'P02', 'P03', 'P04', 'P05', 'P06', 'P07', 'P08', 'P09', 'P10']


# In[6]:

#Creating a list of all transactions
f = open("Training.txt","r", encoding = 'utf-8')
products = []
for line in f:
    products.append((line.strip()).split(',') ) 
f.close()    


# In[7]:

#Creating a panda series for each product
j = 1
dic = {}
for i in items:
    Col = []
    for line in products:
        Col.append(int(i in line))  
    dic[i] = pd.Series(Col)
    j+=1


# In[8]:

#Creating a Dataframe
mba = pd.DataFrame(dic)


# In[9]:

#Function for getting the frequent itemset and its support
def get_support(df):
    """
    Getting the frequent itemset and its frequency
    """
    pp = []
    for cnum in range(1, 5):
        for cols in combinations(df, cnum):
            z=1
            st = [int(i in cols) for i in items]
            for i in range(len(items)):
                z = z & (df[items[i]] == st[i])
            tr = df[z]    
            s = tr[list(cols)].all(axis=1).sum()
            pp.append([",".join(cols), s])
    sdf = pd.DataFrame(pp, columns=["Pattern", "Support"])
    return sdf


# In[10]:

#Dataframe of itemset and its support
s = get_support(mba)


# In[11]:

#Link for Test dataset
rul = "http://kevincrook.com/utd/market_basket_test.txt"


# In[12]:

#Downloading the test set
q = requests.get(rul)


# In[13]:

#Writing the set to a atext file
t = open("Test.txt","wb")
t.write(q.content)
t.close()


# In[14]:

#Creating a recommendation for each transaction in test set
g = open("market_basket_recommendations.txt","w")
with open("Test.txt","r", encoding = 'utf-8') as h:
    for ln in h:
        sting = ln.strip()[4:]
        #Removing P04 and P08 for its zero support
        if 'P04' in sting.split(','):
            x = sting.split(',')
            x.remove('P04')
            if 'P08' in x: 
                x.remove('P08')
                string = ','.join(x)
            else:
                string = ','.join(x)
        elif 'P08' in sting.split(','):  
            x = sting.split(',')
            x.remove('P08')
            string = ','.join(x)
        else:
            string = sting
        #Applying the neccessary conditions    
        a = s[s["Pattern"].str.len() == len(string)+4]
        
        y = 1    
        for i in string.split(','):
            y = y & s["Pattern"].str.contains(i)
        b = a[y]  
        
        c = b['Pattern'][b['Support'].idxmax()]  
        d = set(c.split(','))-set(sting.split(','))
        #Writing the recommended products to a text file
        g.write((ln.strip()[0:4]+d.pop()+'\n'))
g.close()                

