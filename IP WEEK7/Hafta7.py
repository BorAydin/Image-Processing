#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import matplotlib.pyplot as plt
import random

v1=[5,0]
v2=[2,6]
v1,v2


# In[2]:


v1+v2


# In[6]:


def vec_add(vec1,vec2):
    
    v3=[0,0]
    v3[0]=vec1[0]+vec2[0]
    v3[1]=vec1[1]+vec2[1]
    
    return v3

def vec_add2(vec1,vec2):
    
    s=len(vec1)
    v4=[]
    
    for i in range (s):
       temp=vec1[i]+vec2[i]
       v4.append(temp)
    
    return v4

def create_vec(m=5,n=2):
    
    m,n=4,3
    v5=[]
    
    for i in range(m):
        v5.append([])
        
        for j in range(n):
            r=random.randint(0,10)
            v5[i].append(r)
            
    return v5        
    
    


# In[7]:


vec_add(v1,v2)


# In[8]:


vec_add2(v1,v2)


# In[9]:


create_vec()


# In[15]:


def center(vec1,vec2):
    
     s=len(vec1)
     v6=[]
     
     for i in range (s):
         temp=(vec1[i]+vec2[i])/2
         v6.append(temp)
    
     return v6


# In[16]:


center(v1,v2)


# In[17]:


def hipo(vec1,vec2):
    
     s=len(vec1)
     result=0
     
     for i in range (s):
         result+=(vec1[i]-vec2[i])**2
        
     return result**0.5


# In[18]:


v7=[3,0]
v8=[0,4]

hipo(v7,v8)


# In[ ]:




