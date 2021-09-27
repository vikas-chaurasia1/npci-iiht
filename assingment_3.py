#!/usr/bin/env python
# coding: utf-8

# In[60]:


print("Er. Vikas kumar chaurasia")
print("National payment Corporation Of India")


# In[61]:


level=5
row=5
col=5+4
print(" ",col,row)
sum_list=[1]
matrix=[]
squared_matrix=[]


# In[62]:


mid=col//2
k=0
sum1=1
dist=int(input("enter the distance="))

for x in range(1):
    temp_list=[]
    for y in range(col):
        if(y>=mid-k and y<=mid+k):
            temp_list.append(1)
            print("1",end =" ")
        else:
            temp_list.append(0)
            print(" ",end =" ")
    sq=[num**2 for num in temp_list]
    squared_matrix.append(sq)
    matrix.append(temp_list)
print()
for i in range(1,row):
    k=k+1
    sum1=sum1+dist
    j=0
    sum2=0
    row_dist=0
    temp_list=[]
    while j < col:
        if(j>=mid-k and j<=mid+k):
            print(sum1+row_dist,end =" ")
            temp_list.append(sum1+row_dist)
            temp_list.append(0)
            j=j+2
            print(" ",end =" ")
            sum2=sum2 + sum1
            row_dist=row_dist+1
        else:
            temp_list.append(0)
            print(" ",end =" ")
            j=j+1
    sum_list.append(sum2)
    matrix.append(temp_list)
    sq=[num**2 for num in temp_list]
    squared_matrix.append(sq)
    print()


# In[63]:


for i in range(len(sum_list)):
    print("sum of row",i," =",sum_list[i])


# In[64]:


print("matrix lenth=",len(matrix))
print("inverse of above hanoi tree")
for li in range(len(matrix)-1,-1,-1):
    print(matrix[li])


# In[66]:


print("squared inverse of above hanoi tree")
for li in range(len(matrix)-1,-1,-1):
    print(squared_matrix[li])


# In[55]:





# In[ ]:




