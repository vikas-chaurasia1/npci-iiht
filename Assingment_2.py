#!/usr/bin/env python
# coding: utf-8

# In[7]:


print("vikas chaursasia")


# In[1]:


level=5
row=5
col=5+4
print(" ",col,row)


# In[38]:


mid=col//2
k=0
sum1=1
dist=int(input("enter the distance="))
sum_list=[1]
for x in range(1):
    for y in range(col):
        if(y>=mid-k and y<=mid+k):
            print("1",end =" ")
        else:
            print(" ",end =" ")
print()
for i in range(1,row):
    k=k+1
    sum1=sum1+dist
    j=0
    sum2=0
    while j < col:
        if(j>=mid-k and j<=mid+k):
            print(sum1,end =" ")
            j=j+2
            print(" ",end =" ")
            sum2=sum2 + sum1
        else:
            print(" ",end =" ")
            j=j+1
    sum_list.append(sum2)
    print()


# In[49]:


for i in range(len(sum_list)):
    print("sum of row",i," =",sum_list[i])


# In[ ]:





# In[ ]:




