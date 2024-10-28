# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 09:39:46 2023

@author: user
"""
import pandas as pd
import numpy as np
import random as rd
import cv2


#-----Image Upload
image=cv2.imread('image.jfif')
image = cv2.resize(image, (200,90)) 
pixel_values=image.reshape((-1, 3))
pixel_data=pd.DataFrame(pixel_values)


def selection_center(data,list1):
    new_center=[]
    data1=pd.DataFrame(list1,columns=['Center'])
    for i in list(set(list1)):
        new_center.append(np.mean(data.iloc[data1[data1['Center']==i].index,:],axis=0).values)
    return new_center
def find_center(array,index1):
    new_data=pd.DataFrame(array,index=index1).sort_values(by=0,ascending=True)
    return new_data.index[0]
def euclidean(x_data,x_data2):
    distance=[np.sum(np.power(i.reshape(1,-1)-np.array(x_data),2),axis=1) for i in np.array(x_data2)]
    return distance   
def assignment(distance,center_original,data):
    center_list=[]
    for i in range(0,len(data)):
        center_list.append(find_center(distance[i],center_original))
    return center_list
def k_means(data,k,sayac_1):
    sayac=0
    rand_center=[rd.choice(np.arange(len(data))) for i in range(0,k)]
    distance_list=euclidean(data.iloc[rand_center,:],data)
    center_list_1=assignment(distance_list,rand_center,data)
    
    while True:
        new_center_1=selection_center(data,center_list_1)
        distance_list=euclidean(new_center_1,data)
        center_list_1=assignment(distance_list,list(range(0,len(new_center_1))),data)
        
        sayac+=1
        if sayac>sayac_1:
            print(new_center_1)
            return center_list_1,new_center_1
            break
        
center_list,new_center=k_means(pixel_data,3,10)

new_image=[]
for i in center_list:
    for j in range(0,len(new_center)):
        if i==j:
            new_image.append(new_center[j])
            

# Displaying the picture
new_image = np.array(new_image).reshape(200,90,3)
cv2.imshow('The new picture', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

       



