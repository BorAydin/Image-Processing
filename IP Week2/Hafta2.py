#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import matplotlib.pyplot as plt
import os

os.getcwd()

im_1 = plt.imread('C:\\Users\\BorA\\Downloads\\sessiz.jpg')
im_1.ndim 
im_1.shape

plt.imshow(im_1)
plt.show()

im_1 = im_1 + 10
plt.imshow(im_1)
plt.show()

im_1[:,:,0] = im_1[:,:,0]-25
plt.imshow(im_1)
plt.show()

im_1 = plt.imread('C:\\Users\\BorA\\Downloads\\sessiz.jpg')

def kızıl(im_1,s=5):
    
    m,n,p = im_1.shape
    im_2 = np.zeros((m,n,3),dtype=int)
    
    for m in range(im_1.shape[0]):
        for n in range(im_1.shape[1]):
            im_2[m,n,0] = im_1[m,n,0] + 100
            im_2[m,n,1] = im_1[m,n,1]
            im_2[m,n,2] = im_1[m,n,2]
    return im_2


im_3 = kızıl(im_1)
plt.imshow(im_3)
plt.show()  

im_1 = plt.imread('C:\\Users\\BorA\\Downloads\\sessiz.jpg')

def boyutlandır(im_1): 
    
    m,n,p=im_1.shape 
    new_m= int(m/2) 
    new_n= int(n/2) 
    im_4=np.zeros((new_m,new_n),dtype=int) 
    
    for m in range(new_m): 
        for n in range(new_n): 
            s=(im_1[m*2,n*2,0]+im_1[m*2,n*2,1]+im_1[m*2,n*2,2])/3 
            im_4[m,n]=int(s) 
    return im_4 
    
plt.imshow(im_1)
plt.show()
im_5=boyutlandır(im_1) 
plt.imshow(im_5,cmap='gray') 
plt.show() 

im_1=plt.imread('C:\\Users\\BorA\\Downloads\\sessiz.jpg') 

def bozulmadan_boyutlandır(im_1): 
    
    m,n,p=im_1.shape 
    new_m= int(m/2) 
    new_n= int(n/2) 
    im_6=np.zeros((new_m,new_n,3),dtype=int) 
    
    for m in range(new_m): 
        for n in range(new_n): 
            im_6[m,n,0] = im_1[m,n,0] 
            im_6[m,n,1] = im_1[m,n,1] 
            im_6[m,n,2] = im_1[m,n,2] 
    return im_6 

plt.imshow(im_1) 
plt.show() 
im_7=bozulmadan_boyutlandır(im_1) 
plt.imshow(im_7) 
plt.show() 
im_8=bozulmadan_boyutlandır(im_7) 
plt.imshow(im_8) 
plt.show() 
im_9=bozulmadan_boyutlandır(im_8) 
plt.imshow(im_9) 
plt.show()


# In[ ]:









