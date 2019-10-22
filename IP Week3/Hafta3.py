#!/usr/bin/env python
# coding: utf-8

# In[17]:


import matplotlib.pyplot as plt
import numpy as np 

im1=plt.imread('C:\\Users\\BorA\\Downloads\\Resimler\\mini.jpg')
im1.ndim
im1.shape

def histogram():
    
    m,n,p=im1.shape
    hist={}
    
    for i in range(m):
        for j in range(n):
            
            if im1[i,j,1] in hist.keys():
                
                hist[im1[i,j,1]]=hist[im1[i,j,1]]+1
            
            else:
                
                hist[im1[i,j,1]]=1
            
    return hist

def create_histogram(hist=histogram()):
    
    x=[]
    y=[]
    
    for key in hist.keys():
        
        x.append(key)
        y.append(hist[key])
        
    return x,y        

x,y=create_histogram()
plt.bar(x,y)
plt.show()


# In[ ]:




