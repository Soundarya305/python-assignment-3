#!/usr/bin/env python
# coding: utf-8

# In[1]:


###1.1 write a python program to implement your own myreduce() function which works exactly like python's built-in function reduce()
def myreduce(add,list1):
    return a
def add(a,b):
    return a+b
list1=[10,20,30,40,50]
a=list1[0]
for i in range(1,len(list1)):
    b=list1[i]
    a=add(a,b)
print(myreduce(add,list1))


# In[3]:


###1.2 write a python program to implement your own myfilter() function which works exactly like python's built-in function filter()
def myfilter(is_even,lst2):
    return is_even(a)
lst2=[1,2,3,4,5,6,7,8,9,10]
lst3=[]
def is_even(a):
    for i in lst2:
        if i%2==0:
            lst3.append(i)
    print(lst3)
myfilter(is_even,lst2)


# In[14]:


###2. implement list comprehensions to produce the following lists. write list comprehensions to produce the following lists


###########
input_list = ['x', 'y','z']
result = [item*num for item in input_list for num in range(1,5)]
print("['x','y','z'] => " + str(result))


##########
input_list = ['x','y','z']
result = [item*num for num in range(1,5) for item in input_list]
print("['x','y','z'] => " +str(result))


###########
input_list = [2,3,4]
result = [ [item+num for item in input_list] for num in range(0,3)]
print("[(2),(3),(4)] =>" + str(result))



###########
input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)]
print("[2,3,4,5] =>" + str(result))


###########
input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print("[1,2,3] =>" + str(result))


# In[ ]:




