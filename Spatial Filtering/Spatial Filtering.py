#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math


img=plt.imread('C:\\Users\\BorA\\Downloads\\Resimler\\şer.jpg')

img.shape

img2=np.zeros((900,900),dtype=np.uint8)
img2=img[:,:,0] 

plt.imshow(img2,cmap='gray')
plt.show()


# In[2]:


def filter(img3):
    m,n=img3.shape
    img4=np.zeros((900,900),dtype=np.uint8)

    for i in range(1,m-1):
        for j in range (1,n-1):
            s = img3[i-1,j-1]/9 + img3[i-1,j]/9 + img3[i-1,j+1]/9 + img3[i,j-1]/9 + img3[i,j]/9 + img3[i,j+1]/9 + img3[i+1,j-1]/9 + img3[i+1,j]/9 + img3[i+1,j+1]/9
            s=int(s)
            img4[i,j]=s
    return img4            


# In[3]:


img5=filter(img2)

plt.imshow(img5,cmap='gray')
plt.show()


# In[4]:


def gaussian(img6):
    m,n=img6.shape
    img7=np.zeros((900,900),dtype=np.uint8)

    for i in range(1,m-1):
        for j in range (1,n-1):
            s = img6[i-1,j-1]/16 + (img6[i-1,j]*2)/16 + img6[i-1,j+1]/16 + (img6[i,j-1]*2)/16 + (img6[i,j]*4/16) + (img6[i,j+1]*2)/16 + img6[i+1,j-1]/16 + (img6[i+1,j]*2)/16 + img6[i+1,j+1]/16
            s=int(s)
            img7[i,j]=s
    return img7    


# In[5]:


img8=gaussian(img2)

plt.imshow(img8,cmap='gray')
plt.show()


# In[6]:


def edge(img9):
    m,n=img9.shape
    img10=np.zeros((900,900),dtype=np.uint8)

    for i in range(1,m-1):
        for j in range (1,n-1):
            x = img9[i-1,j-1]*-1 + img9[i-1,j]*0 + img9[i-1,j+1] + img9[i,j-1]*-2 + img9[i,j]*0 + img9[i,j+1]*2 + img9[i+1,j-1]*-1 + img9[i+1,j]*0 + img9[i+1,j+1]
            y = img9[i-1,j-1]*-1 + img9[i-1,j]*-2 + img9[i-1,j+1]*-1 + img9[i,j-1]*0 + img9[i,j]*0 + img9[i,j+1]*0 + img9[i+1,j-1] + img9[i+1,j]*2 + img9[i+1,j+1]
            s=math.sqrt(x*x+y*y)
            img10[i,j]=s
    return img10    


# In[7]:


img11=edge(img2)

plt.imshow(img11,cmap='gray')
plt.show()


# In[ ]:




