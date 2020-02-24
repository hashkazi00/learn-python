
# coding: utf-8

# # Basics of Python

# In[1]:


print("Hello World!")


# In[ ]:


print(4)
print(2.5)
print('a')


# In[ ]:


print(type("Hello World!"))
print(type(4))
print(type(2.5))
print(type('a'))


# ## Arithmetic Operations

# In[ ]:


print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3//2)


# In[ ]:


print(5.5/2)
print(5.5/2.5)

print(2.5*3)
print(2.5*3.5)

print(4/3.0)


# ## Lists

# In[ ]:


list1 = [1,2,3,4]
print(list1)
print(type(list1))

list2 = [5, 2.5, "sahil", 's']
print(list2)


# List Indexing

# In[ ]:


print(list2[0])
print(list2[1])
print(list2[2])
print(list2[3])


# List Updating

# In[ ]:


print(list2)
list2[1] = 3.5
print(list2)


# In[ ]:


print(list2)
list2[0] = 'hello'
print(list2)


# In[ ]:


print(type(list2[1]))


# List operations

# In[ ]:


list1 = [1,2,3,4]
list2 = [5,6,7,8]
print(list1+list2)
# print(list1-list2)
# print(list1*list2)
print(list1*3)
#print(list1/list2)
#print(list1/1)


# List Slicing

# In[ ]:


list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1[0:8])
print(list1[0:2])
print(list1[7:10])

print(list1[0:10:2])
print(list1[1:10:2])

print(list1[:8])
print(list1[2:])

print(list1[0:10:4])
list2 = list1[0:10:4]
print(list2)


# In[ ]:


list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1[-1])
print(list1[-2])

print(list1[-4:])
print(list1[-4::2])
print(list1[:-1])


# In[ ]:


list1 = [1,2,3,4,5,6,7,8,9,10]
print(len(list1))

alphabet='a'
list1.append(alphabet)
print(list1)
list1.append('b')
print(list1)
list1.append('c')
print(list1)


# In[ ]:


list1 = [1,2,3,4,5,6,7,8,9,10]
list1.insert(5,'a')
print(list1)
list1.append(4)
print(list1)
list1.remove(4)
print(list1)

list2=["hello","world"]
list1.extend(list2)
print(list1)

list2 = [5,2,3,4]
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)
list2.clear()
print(list2)


# # String

# String Indexing

# In[ ]:


str1 = "Hello World!"

print(str1[0])
print(str1[1])
print(str1[-1])
print(str1[-3])


# String Slicing

# In[ ]:


str1 = "Hello World!"

print(str1[:5])
print(str1[6:11])
print(str1[5])


# String Operations

# In[ ]:


str1 = "First String"
str2 = "Second String"

print(str1+str2)
#print(str1-str2)
#print(str1*str2)
print(str1*3)
#print(str1/str2)
#print(str1/2)


# String Formatting

# In[1]:


num1 = 10
num2 = 2.5

#first method
print("Value of number is %d" %(num1) )
print("Value of number1 is %d and number is %3.3f" %(num1,num2) )

#second method
print("Value of number1 is {0}".format(num1))
print("Value of number1 is {0} and number2 is {1}".format(num1,num2))
print("Value of number1 is {1} and number2 is {0}".format(num1,num2))

print("Value of number1 is {n1} and number2 is {n2}".format(n1=num1,n2=num2))


# ## User Input

# In[ ]:


userinput = input("Type your name")
print(userinput)


# In[ ]:


userinput = input("Type a number")
print(userinput)
print(type(userinput))


# In[ ]:


userinput = int(input("Type a number"))
print(userinput)
print(type(userinput))


# ## Conditional statements

# if else

# In[ ]:


value = 30
if value>25:
    print("Hello")


# In[ ]:


value = 30
if value>40:
    print("Hello 1")    
else:
    print("Hello 2")


# In[ ]:


value = 30
if value>30:
    print("Hello 1")
elif value>25:
    print("Hello 2")
else:
    print("Hello 3")


# Single line if else conditions

# In[1]:


fruit = "Mango"

isApple = True if fruit == "Apple" else False
print(isApple)
print(type(isApple))

