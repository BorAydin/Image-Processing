#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import matplotlib.pyplot as plt


img1=plt.imread('C:\\Users\\BorA\\Downloads\\Resimler\\Marion.jpg')

img1.shape

img2=np.zeros((600,445),dtype=np.uint8)
img2=img1[:,:,0] 

plt.imshow(img2,cmap='gray')
plt.show()


# In[17]:


m,n=img2.shape
img3=np.zeros((600,445),dtype=np.uint8)

for i in range(1,m-1):
    for j in range (1,n-1):
        s = img2[i-1,j-1]/9 + img2[i-1,j]/9 + img2[i-1,j+1]/9 + img2[i,j-1]/9 + img2[i,j]/9 + img2[i,j+1]/9 + img2[i+1,j-1]/9 + img2[i+1,j]/9 + img2[i+1,j+1]/9
        s=int(s)
        img3[i,j]=s
        
        


# In[18]:


plt.subplot(1,2,1)
plt.imshow(img2,cmap='gray')

plt.subplot(1,2,2)
plt.imshow(img3,cmap='gray')


# In[ ]:




