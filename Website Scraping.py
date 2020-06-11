#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests


# In[2]:


pip install beautifulsoup4


# In[3]:


pip install requests


# In[4]:


pip install --user pipenv


# In[5]:


import requests


# In[6]:


import pandas as pd
from bs4 import BeautifulSoup
import lxml.html as lh


# In[7]:


#Eventually make this a function
response = requests.get('https://www.ncwater.org/Drought_Monitoring/statusReport.php/')
stored_contents = lh.fromstring(response.content)
table_elements = stored_contents.xpath('//tr')
[len(T) for T in table_elements[:12]]


# In[8]:


#Create empty list
col=[]
i=0

#For each row, store each first element (header) and an empty list
for t in table_elements[0]:
    i+=1
    name=t.text_content()
    print (i,name)
    col.append((name,[]))


# In[9]:


#Since out first row is the header, data is stored on the second row onwards
for j in range(1,len(table_elements)):
    #T is our j'th row
    T=table_elements[j]
    
    #If row is not of size 10, the //tr data is not from our table 
    if len(T)!=7:
        break
    #i is the index of our column
    i=0
    
    #Iterate through each element of the row
    for t in T.iterchildren():
        data=t.text_content() 
        #Check if row is empty
        if i>0:
        #Convert any numerical value to integers
            try:
                data=int(data)
            except:
                pass
        #Append the data to the empty list of the i'th column
        col[i][1].append(data)
        #Increment i for the next column
        i+=1


# In[10]:


[len(C) for (title,C) in col]


# In[11]:


Dict ={title:column for (title,column) in col}
Newest_Updates =pd.DataFrame(Dict)


# In[12]:


Newest_Updates


# In[ ]:





# In[ ]:





# In[ ]:




