#!/usr/bin/env python
# coding: utf-8

# In[45]:


print("vikas kumar chaurasia")


# # program start

# In[71]:


print("""step 1: create a list
step 2: create distionary
step 3: create sorted distionary
step 4:exit""")


# In[72]:


list1=[]
dist={}
sorted_dist={}
def create_dist(list1):
    for i in list1:
        dist[i]=i
def sort_dist(dist):
    global sorted_dist
    sorted_dist={k: v for k, v in sorted(dist.items(), key=lambda item: item[1])}
    #print(sorted_dist)
x=lambda x:list1.append(x)
def lambd_fun():
    step=int(input("enter your step: "))
    if step==1:
        x((int(input("enter the element: "))))
    if (step==2 or step==3) and (len(list1)==0):
        x((int(input("enter the element: "))))
    if step==2:
        create_dist(list1)
    if step==3:
        sort_dist(dist)
    if step!=4:
        lambd_fun()
lambd_fun()
print("created list: ",list1)
print("created distionary: ",dist)
print("sorted dictionary: ",sorted_dist)


# # program end

# In[69]:


d1={}
d1={k: v for k, v in sorted(dist.items(), key=lambda item: item[1])}
print(d1)


# In[3]:


l1=[]
print(len(l1))


# In[ ]:


while()


# In[12]:


def sum1(x):
    return(lambda x:fun(x))
def fun(x):
    print("its ok")
x1=sum1(34)


# In[29]:


l1=[]
x=lambda x:l1.append(x)
x(int(input()))
x(int(input()))
print(l1)


# In[ ]:




