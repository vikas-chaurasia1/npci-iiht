#!/usr/bin/env python
# coding: utf-8

# In[107]:


list1=[["name","emal","mob"],["vikash","vikas14011999@gmail.com","8539858948"],["aniket","ser14011999@gmail.com","234084"]
     ,["chaurasia","abc@gmail.com","34467","newdelhi",]]


# In[108]:


#appending empty list
l2=[]
list1.append(l2)
list1.append(["mausin","gogmail@com","23456"])

#entering duplicate value and handling
l3=["vikash","vikas14011999@gmail.com","8539858948"]
if l3 not in list1:
    list1.append(l3)


# In[109]:


print(list1)
x=len(list1)
print(x)


# In[110]:


file1=open("user.txt","r+")


# In[111]:


for li in list1:
    if len(li) > 0:
        count1=0
        for entry in li:
            file1.write(entry)
            file1.write(",")
            count1=count1+1
            if count1==3:
                break
    else:
        file1.write("data is not available")
    file1.write("\n")


# In[112]:


file1.close()

