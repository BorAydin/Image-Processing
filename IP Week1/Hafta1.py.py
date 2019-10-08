#!/usr/bin/env python
# coding: utf-8

# In[25]:


import os
import numpy as np
import matplotlib.pyplot as plt

os.getcwd()
os.listdir()

img_1 = plt.imread('C:\\Users\\BorA\\Downloads\\Resimler\\bsen.jpg')

img_1.ndim
img_1.shape
m,n,p = img_1.shape
m,n,p

plt.imshow(img_1)
plt.show()

img_1[100,100,:]

new_image=np.zeros((m,n),dtype=float)

for i in range(m):
    for j in range(n):
        s = (img_1[i,j,0] + img_1[i,j,1] + img_1[i,j,2])/3
        new_image [i,j] = s

plt.imshow(new_image,cmap='gray') 
plt.show()          

plt.imsave('bsen2.jpg',new_image,cmap='gray')

transpoze_image=np.zeros((n,m),dtype=float)

for i in range(m):
    for j in range(n):
        s = (img_1[i,j,0] + img_1[i,j,1] + img_1[i,j,2])/3
        transpoze_image [j,i] = s
        
plt.imshow(transpoze_image,cmap='gray') 
plt.show() 
plt.imsave('bsen90.jpg',transpoze_image,cmap='gray')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




