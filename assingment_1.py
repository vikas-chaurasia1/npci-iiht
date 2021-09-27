#!/usr/bin/env python
# coding: utf-8

# In[118]:


student_marks=[[89,43,39],[56,79,90],[87,65,68],[56,34,89],[87,89,72]];
print("marks of student in maths,physics,chemestry:")
print(student_marks)

total_student=5
print("total_student=",total_student)
final_grade=[]


# In[119]:


count1=0
sum1=0
passed_student=0
failed_student=0
reappear_student=0
count1=0
sum1=student_marks[0][0] + student_marks[0][1] + student_marks[0][2]
final_grade.append(sum1);
if(student_marks[0][0]> 50):
    count1=count1+1
if(student_marks[0][1]> 50):
    count1=count1+1
if(student_marks[0][2]> 50):
    count1=count1+1
if(count1==1):
    failed_student=failed_student+1
if(count1==2):
     reappear_student=reappear_student+1
if(count1==3):
    passed_student=passed_student+1
    


# In[120]:


count1=0
sum1=student_marks[1][0] + student_marks[1][1] + student_marks[1][2]
final_grade.append(sum1);
if(student_marks[1][0]> 50):
    count1=count1+1
if(student_marks[1][1]> 50):
    count1=count1+1 
if(student_marks[1][2]> 50):
    count1=count1+1
if(count1==1):
    failed_student=failed_student+1
if(count1==2):
     reappear_student=reappear_student+1
if(count1==3):
    passed_student=passed_student+1


# In[121]:


count1=0
sum1=student_marks[2][0] + student_marks[2][1] + student_marks[2][2]
final_grade.append(sum1);
if(student_marks[2][0]> 50):
    count1=count1+1
    sum1=sum1+1
if(student_marks[2][1]> 50):
    count1=count1+1
    sum1=sum1+1
if(student_marks[2][2]> 50):
    count1=count1+1
    sum1=sum1+1
if(count1==1):
    failed_student=failed_student+1
if(count1==2):
     reappear_student=reappear_student+1
if(count1==3):
    passed_student=passed_student+1


# In[122]:


count1=0
sum1=student_marks[3][0] + student_marks[3][1] + student_marks[3][2]
final_grade.append(sum1);
if(student_marks[3][0]> 50):
    count1=count1+1
if(student_marks[3][1]> 50):
    count1=count1+1
if(student_marks[3][2]> 50):
    count1=count1+1
if(count1==1):
    failed_student=failed_student+1
if(count1==2):
     reappear_student=reappear_student+1
if(count1==3):
    passed_student=passed_student+1


# In[123]:


count1=0
sum1=student_marks[4][0] + student_marks[4][1] + student_marks[4][2]
final_grade.append(sum1);
if(student_marks[4][0]> 50):
    count1=count1+1
if(student_marks[4][1]> 50):
    count1=count1+1
if(student_marks[4][2]> 50):
    count1=count1+1
if(count1==1):
    failed_student=failed_student+1
if(count1==2):
     reappear_student=reappear_student+1
if(count1==3):
    passed_student=passed_student+1


# In[124]:


print("total student passed=",passed_student)
print("total_student failed=",failed_student)
print("total studeent reappear",reappear_student)


# In[125]:


dist=0
first=0
second=0
if(final_grade[0] >= 240):
    dist=dist+1
elif(final_grade[0]>=180 and final_grade[0]<=237):
    second=second + 1
elif(final_grade[0]>=150 and final_grade[0]<=177):
    first=first+1


# In[126]:


if(final_grade[1] >= 240):
    dist=dist+1
elif(final_grade[1]>=180 and final_grade[0]<=237):
    second=second + 1
elif(final_grade[1]>=150 and final_grade[0]<=177):
    first=first+1


# In[127]:


if(final_grade[2] >= 240):
    dist=dist+1
elif(final_grade[2]>=180 and final_grade[0]<=237):
    second=second + 1
elif(final_grade[2]>=150 and final_grade[0]<=177):
    first=first+1


# In[128]:


if(final_grade[3] >= 240):
    dist=dist+1
elif(final_grade[3]>=180 and final_grade[0]<=237):
    second=second + 1
elif(final_grade[3]>=150 and final_grade[0]<=177):
    first=first+1


# In[129]:


if(final_grade[4] >= 240):
    dist=dist+1
elif(final_grade[4]>=180 and final_grade[0]<=237):
    second=second + 1
elif (final_grade[4]>=150 and final_grade[0]<=234):
    first=first+1


# In[130]:


print("total student with distinction=",dist)
print("total student with first_class=",first)
print("total student with second class=",second)


# In[ ]:





# In[ ]:




