#!/usr/bin/env python
# coding: utf-8

# In[157]:


print("vikas kumar chaursia")


# In[158]:


class user:
    def get_user(self,u_id,u_name,u_salary):
        self.u_id=u_id
        self.u_name=u_name
        self.u_salary=u_salary
        return [u_id,u_name,u_salary]


# In[159]:


class project(user):
    def get_project(self,p_id,p_name):
        self.p_id=p_id
        self.p_name=p_name
    def get_user_list(self,list1):
        print(self.p_id,self.p_name,list1)
    def get_sorted(self,list1):
        self.list1=list1
        list1.sort(key=lambda x:x[2])
        print(self.p_id,self.p_name,list1)
        


# In[160]:


proj1=[]
p1=project()
p1.get_project(1,"mission_Allout")
proj1.append(p1.get_user(23156,"vikas",39600))


# In[161]:


proj1.append(p1.get_user(23451,"aniket",39450))
proj1.append(p1.get_user(45234,"sherya",45234))


# In[162]:


p1.get_user_list(proj1)


# In[163]:


p1.get_sorted(proj1)


# In[164]:


proj2=[]
p2=project()
p2.get_project(3,"operation vijay")
proj2.append(p2.get_user(34123,"chaurasia",39650))
proj2.append(p2.get_user(56783,"sharma",30856))
proj2.append(p2.get_user(45234,"gupta",34527))


# In[165]:


p2.get_user_list(proj2)


# In[166]:


p2.get_sorted(proj2)


# In[167]:


print(p2.p_id)
print(p2.p_name)


# In[168]:


project_list1=[[p1.p_id,p1.p_name,proj1],[p2.p_id,p2.p_name,proj2]]


# In[169]:


print(project_list1)


# In[170]:


sorted_list=[]
for i in project_list1:
    temp=[]
    temp.append(i[0])
    temp.append(i[1])
    i[2].sort(key=lambda x:x[2])
    temp.append(i[2])
    sorted_list.append(temp)


# In[171]:


print("sorting according to salary within particular project: ","\n",sorted_list)


# In[172]:


sort2_list=[]
for i in project_list1:
    for j in i[2]:
        temp=[]
        temp.append(i[0])
        temp.append(i[1])
        temp.append(j)
        sort2_list.append(temp)


# In[173]:


print(sort2_list)


# In[174]:


sort2_list.sort(key=lambda x:x[2][2])


# In[175]:


print("sorting on basis of salary irresepctive of project","\n",sort2_list)


# In[187]:


dist={}
for i in sorted_list:
    dist[i[0]]=i[2]


# In[189]:


print("project id and corresponding user in sorted manner: ","\n",dist)


# In[ ]:




