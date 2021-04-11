#!/usr/bin/env python
# coding: utf-8

# # Agriculture Crop Recommendation
# Precision agriculture is in trend nowadays. It helps the farmers to get informed decision about the farming strategy. Here, I present you a dataset which would allow the users to build a predictive model to recommend the most suitable crops to grow in a particular farm based on various parameters.
# 
# Context
# This dataset was build by augmenting datasets of rainfall, climate and fertilizer data available for India.
# 
# Data fields
# N - ratio of Nitrogen content in soil
# P - ratio of Phosphorous content in soil
# K - ratio of Potassium content in soil
# temperature - temperature in degree Celsius
# humidity - relative humidity in %
# ph - ph value of the soil
# rainfall - rainfall in mm

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# In[6]:


df=pd.read_csv("crop_rec.csv") #2200 values and 22 unique crops
df.head()


# In[5]:


df.describe()


# In[7]:


cor1=df.corr()


# In[12]:


sns.heatmap(cor1,annot=True)


# In[13]:


x=df.drop(['label'],axis=1)
y=df['label']
xtr,xts,ytr,yts=train_test_split(x,y,test_size=0.33)


# In[14]:


model=RandomForestClassifier(n_estimators=50)
model.fit(xtr,ytr)
print(model.score(xts,yts))
yp=model.predict(xts)


# In[15]:


yp


# In[17]:


model.predict([[74,35,40,26.491096,80.158363,6.980401,242.864034]])


# #Data fields
# N - ratio of Nitrogen content in soil
# P - ratio of Phosphorous content in soil
# K - ratio of Potassium content in soil
# temperature - temperature in degree Celsius
# humidity - relative humidity in %
# ph - ph value of the soil
# rainfall - rainfall in mm 
# 
# if check button valueis tick means 1 else its 0

# In[38]:


from tkinter import *
#import tkSimpleDialog
from tkinter import messagebox
root=Tk()
def getvals():
    print("Submiting form")
    
    s=model.predict([[nitval.get(),phoval.get(),potval.get(),tempval.get(),humval.get(),phvalval.get(),rainval.get()]])
    print(f"{nitval.get(),phoval.get(),potval.get(),tempval.get(),humval.get(),phvalval.get(),rainval.get(),s[0]}")
    messagebox.showinfo("Crop Recommended",s[0])
    with open("records.txt","a") as f:
        f.write(f"{nitval.get(),phoval.get(),potval.get(),tempval.get(),humval.get(),phvalval.get(),rainval.get(),s[0]}\n")
    # instead of always rewrite using w use command a that will add values to same file also try to use \n to get values in next line


root.geometry("644x344")
root.title("CROP RECOMMENDATION BY DHURV")
#heading
Label(root,text="Welcome To Crop Recommendation By Dhruv", font="comicsansms 13 bold",pady=15).grid(row=0,column=3)

#text for our form
name=Label(root,text="Name")
st=Label(root,text="State")
nit=Label(root,text="Nitrogen")
pho=Label(root,text="Phosphorous")
pot=Label(root,text="Potassium")
temp=Label(root,text="Temperature")
hum=Label(root,text="Humidity")
phval=Label(root,text="PH Value")
rain=Label(root,text="RainFall")

#pack text for our form
name.grid(row=1,column=2)
nit.grid(row=2,column=2)
pho.grid(row=3,column=2)
pot.grid(row=4,column=2)
temp.grid(row=5,column=2)
hum.grid(row=6,column=2)
phval.grid(row=7,column=2)
rain.grid(row=8,column=2)
st.grid(row=9,column=2)

#checkbox if u want
#service=Checkbutton(text="Want this serivce",variable=servicevalue)
#foodservice.grid(row=x,column=y) #any row and column u like

#Tkinter variable for storing entries
nameval=StringVar()
nitval=IntVar()
phoval=IntVar()
potval=IntVar()
tempval=IntVar()
humval=IntVar()
phvalval=IntVar()
rainval=IntVar()
stval=StringVar()

#entries to form
nameentry=Entry(root,textvariable=nameval)
nitrogenentry=Entry(root,textvariable=nitval)
phosphorousentry=Entry(root,textvariable=phoval)
potassiumentry=Entry(root,textvariable=potval)
temperatureentry=Entry(root,textvariable=tempval)
humidityentry=Entry(root,textvariable=humval)
phvalueentry=Entry(root,textvariable=phvalval)
rainfallentry=Entry(root,textvariable=rainval)
stateentry=Entry(root,textvariable=stval)

#packing entries
nameentry.grid(row=1,column=3)
nitrogenentry.grid(row=2,column=3)
phosphorousentry.grid(row=3,column=3)
potassiumentry.grid(row=4,column=3)
temperatureentry.grid(row=5,column=3)
humidityentry.grid(row=6,column=3)
phvalueentry.grid(row=7,column=3)
rainfallentry.grid(row=8,column=3)
stateentry.grid(row=9,column=3)

#button &packing it and assigning its a command
Button(text="Submit To Crop Rec",command=getvals).grid(row=10,column=3)

root.mainloop()





