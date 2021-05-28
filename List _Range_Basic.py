#!/usr/bin/env python
# coding: utf-8

# In[1]:


#List store sequence of data can be created using [] or using keyword list
l=[12,13,25] 
type(l)


# In[7]:


#list it hytrogenous can keep any type of data like list in list ,integer and string even boolean even tuple different type's of data
l=[12,True,[12,23,45],45.3,"abc"]
type(l)


# In[8]:


# Internally as index for forward index 0,1,2 and backward, -1,-2
# To access the value of list at paticular index
print(l[0])
print(l[2])
# To access the value of list inside a list mention the index of list and index within in the list 
#Trying to access the  value at index 1 in list of list (list starts with index 0)
print(l[2][1])


# In[12]:


# Data acces by backward index
print(l[-3])
# Access data backward index and even list in list backward
print(l[-3][-2])
# Trying to access list value at index where data not avaliable will give error
# print(l[20]) # Index Error : list out of range


# In[15]:


#string and operation's that can be perfomed on string
s ="hello how r you"
# Access the values of string through index
print(s[0])
print(s[1])
print(s[-3])
# print(s[50]) # String index out of range


# In[43]:


# List
l=[12,True,[12,23,45],45.3,"abc"]
# To Access the sequence of data out of list
print(l[0:3] )# colon : can be used to specify the reage of access it excludes the last number as the index start's with Zero

# Also Know as slicing
print(l[0:20])# here it will not give Error

# To Skip or Jump through data
print(l[0:10:2]) #starting index, End index, Jump value by defalut is one

#By defalut the jump is one
print(l[0:10:1]) 
print(" By Defalut it jumps by One",l[0:10])

# Here we are moving backward but by defalut jump is One then also we are getting [] becoz on scale if you see its going from back but jump is +1 so its empty
print(l[5:0])

# So if you mention -1 the you can get reverse data
# But if you see you weill see 12 is not there if you go reverse becoz always when me mention index it's always -1 (here its 0 so the upper bound)
print(l[5:0:-1]) 

# So you can use the upper bound :: Empty which by defualt takes as -1
print(l[10::-1])

# to aloways access list if confused using number line
#----------,-1,-2,0,1,2,3,4,5,6
print(l[-2:5]) # here starting point is -2 (that is [12,23,45] and upperbound  its positive so moves forward so 45.3,"abc", next value of the index right side)

print(l[-2:100 :-1]) # here if u see u are moving forward but the jump is -1 so if u are on 45.5 it goes forward but jumpp is -1 so again it goes backward so its Null


# In[44]:


s ="hello how r u today"
s[0:10]


# In[46]:


s[0:10:2] # skip's one 


# In[48]:


s[::-1] # for reverse string


# In[51]:


s[-1:0:-1] # here you need to mention -1 the third values so it goes in reverse otherwise it goves forward thats +1


# In[52]:


# Range function
range(10)
range(0,10)


# In[53]:


list(range(10)) # to create list for range of data


# In[55]:


list(range(3,10)) # can give range from where to start and end


# In[56]:


list(range(2,20,-1)) # we goving forward than backward so direction conflict


# In[57]:


list(range(20,2,-1)) # will print in reverse manner


# In[60]:


list(range(0,20,2)) # Even Numbers


# In[ ]:


# Input function always converts into string so here you can't take number

l= input()

#so  always type cast

l = int(input("Lower bound for data"))
a = int(input("Upper boud for data"))
s = int(input("step size"))
list(range(l,a,s))


# In[8]:


#To Access list of list
l =[[23,24,25,26],[23,78,79,88],[52,34,35]]

#To access at paticular index of list of list
print(l[0:4:1][0][1])
print(l[0:4][0:3])

# Mutablity : we can change the value of list at paticular index
l=[55,58,99]
l[0]=22
print(l)
