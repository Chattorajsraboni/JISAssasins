#!/usr/bin/env python
# coding: utf-8

# In[3]:


##1
n=int(input("Enter number:"))
count=0
while(n>0):
     digit=n% 10
     n/= 10
    if digit!==0 and digit%2==0:
        neven++
    else if digit==0:
        zero++
    else:
        nodd++
printf("the even numbers are",neven)
printf("the even numbers are",nodd)
printf("the even numbers are",zero)
    


# In[ ]:


##7
n=int(input("enter a number:"))
tot=0
while n>0:
    dig=n%10
    tot=tot+dig
    n=n//10
print("the total sum of digits:",tot)


# In[ ]:


##2
number_array=list()
number=int(input("enter the numbers of elements you want"))
print ('enter numbers in array:')
for i in range(int(number)):
     n=input("number :")
     number_array.append(int(n))
print('ARRAY:',number_array)
print("maximum value entered is :",max(number_array))
print("minimum value enterd is :",min(number_array))


# In[ ]:


##16
c=input("enter a character :")
print("the ASCII value of '"+ c +"' is",ord(c))


# In[ ]:


##18
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("enter base:"))
exp=int(input("enter exponential value:"))
print("result:",power(base,exp))


# In[5]:


##24
num=int(input("choose a number:"))
for i in range(1,11):
    print(num,'x',i,'=',num*i)


# In[ ]:


##25
ch = input("enter a character:")
if((ch>='a' and ch<= 'z') or (ch>='A' and ch<='Z')):
    print(ch,"is an alphabet")
else:
    print(ch,"is an digit")


# In[1]:


##26
salary=int(input("enter salary \n"))
if salary>=5000:
    print("the hra",(salary*15)/100)
    print("the da",(salary*150)/100)
else:
   print("the hra",(salary*10)/100)
   print("the da",(salary*110)/100)


# In[ ]:





# In[ ]:




