#!/usr/bin/env python
# coding: utf-8

# In[1]:



import matplotlib.pyplot as plt
import numpy as np
import cv2
import os.path


# In[18]:


os.listdir()


# In[3]:


os.getcwd()


# In[11]:


data_main_folder="C:\\Users\\BorA\\Desktop\\IP Week8\\main_folder"


# In[12]:


dirs=[d for d in os.listdir(data_main_folder) if os.path.isdir(os.path.join(data_main_folder))]


# In[13]:


print(dirs)


# In[15]:


data_faces_of_class = np.zeros((1000,100*100+1))
folder_counter = -1
s = -1
for directory in dirs:
    folder_counter = folder_counter +1
    new_folder = data_main_folder+"/"+directory
    
    files= [d for d in os.listdir(new_folder) if os.path.isfile(os.path.join(new_folder))]
    for file_ in files:
        s=s+1
        file_name_with_folder=new_folder+"/"+file_
        print(file_name_with_folder)
        ori_image=cv2.imread(file_name_with_folder)
        print(ori_image.shape)
        resized_img=cv2.resize(ori_image,(100,100))
        print(resized_img.shape)

        image_gray=cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)
        print(image_gray.shape)
        plt.imshow(image_gray)
        plt.show()

        image_gray_one_dim=image_gray.reshape(1,100*100)
        print(image_gray_one_dim.shape)
        data_faces_of_class[s,0]=folder_counter
        data_faces_of_class[s,1:100*100+1]=image_gray_one_dim

        cv2.imshow("original image",resized_img)


# In[16]:


print(data_faces_of_class.shape)


# In[17]:


print(data_faces_of_class[3])


# In[ ]:




