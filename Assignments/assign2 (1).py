#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Q1. Write a Python program to convert temperatures to and from celsius,
# fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in
# fahrenheit ]
tem=eval(input("Enter the temperature: "))
tem1=input("Enter unit (C/F):")
if tem1 == 'C':
    temf=(9/5)*tem +32
    print("Temperature in F is ", temf)
elif tem1 == 'F':
    temc=(5/9)*(tem-32)
    print("Temperature in C is ", temc)
else:
    print("Temperature Unit entered is incorrect")
    


# In[10]:


# Q2. Write a Python program to construct the following pattern, using a nested for
# loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[3]:


# Q3. Write a Python program to get the Fibonacci series between 0 to 50.
n2=eval(input("Enter the number of terms: "))
sum=0
a=1
b=1
count=1
print("Fibonacci Series: ", end = " ")
while sum<50:
    print(sum)
    count=count+1
    a=b
    b=sum
    sum=a+b
else:
    print("out of range")


# In[23]:


# Q4. Write a Python program which takes two digits m (row) and n (column) as
# input and generates a two-dimensional array. The element value in the i-th row
# and j-th column of the array should be i*j.
m=int(input("Enter number of rows: "))
n=int(input("Enter number of columns: "))
for i in range(m):
    for j in range(n):
        ij=i*j
        print("a[",i,"][",j,"] =",ij)


# In[ ]:


# Q5. Write a Python program which accepts a sequence of comma separated 4
# digit binary numbers as its input and print the numbers that are divisible by 5 in a
# comma separated sequence. Go to the editor
# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010
l2="0100,0011,1010,1001,1100,1001,1111"
l2=l2.split(",")
for i in range(7):
    if l2[i]=='0101' or l2[i]=='1010' or l2[i]=='1111':
        print(l2[i] ,end=" , ")
    else:
        pass


# In[28]:


# Q6. Write a Python program that accepts a string and calculate the number of
# digits and letters.
s=input("Enter a string: ")
di=le=0
for c in s:
    if c.isdigit():
        di+=1
    elif c.isalpha():
        le+=1
    else:
        pass
print("Digits are :", di)
print("Letters are : ",le)


# In[3]:


# Q7. Write a Python program to check the validity of password input by users.
# Validation :
#  At least 1 letter between [a-z] and 1 letter between [A-Z].
#  At least 1 number between [0-9].
#  At least 1 character from [$#@].
#  Minimum length 6 characters.
#  Maximum length 16 characters.

s1="1234567890"
s2="abcdefghijklmnopqrstuvwxyz"
s3="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s4="#@$%"
print("Enter a Password which contains at least 1 letter between [a-z] , 1 letter between [A-Z],at least 1 number between [0-9]\n and at least 1 character from [#@$%] and is of minimum length 6 and maximum length 16")
password=input()
i=0
f1=f2=f3=f4=f5=0
t=len(password)

if t<=16 and t>=6:
    for i in range(len(password)):
            while True:
                if password[i]  in s1:
                    f1 = -1

                    break
                elif password[i]  in s2:
                    f2 = -1

                    break
                elif password[i]  in s3:
                    f3 = -1

                    break
                elif password[i]  in s4:
                    f4 = -1

                    break
    if (f1!=0 and f2!=0 and f3!=0 and f4!=0):
        print("Valid Password")
    else:
        print("Invalid Password")
else:
    print("Invalid Password")

    
    
# import re 
# password = "R@m@_f0rtu9e$"
# flag = 0
# while True:   
#     if (len(password)<8): 
#         flag = -1
#         break
#     elif not re.search("[a-z]", password): 
#         flag = -1
#         break
#     elif not re.search("[A-Z]", password): 
#         flag = -1
#         break
#     elif not re.search("[0-9]", password): 
#         flag = -1
#         break
#     elif not re.search("[_@$]", password): 
#         flag = -1
#         break
#     elif re.search("\s", password): 
#         flag = -1
#         break
#     else: 
#         flag = 0
#         print("Valid Password") 
#         break
  
# if flag ==-1: 
#     print("Not a Valid Password") 


# In[1]:


# Q8. Write a Python program to find numbers between 100 and 400 (both
# included) where each digit of a number is an even number. The numbers
# obtained should be printed in a comma-separated sequence.
for i in range(100,401):
    sq=str(i)
    if (int(sq[0])%2==0) and (int(sq[1])%2==0) and (int(sq[2])%2==0):
        print(sq,end=",")


# In[13]:


# Q11. Write a Python program to check whether an alphabet is a vowel or
# consonant.
ch = input("Enter a character: ")

if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")


# In[14]:


#Q12. Write a Python program to convert month name to a number of days
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")

if month_name == "February":
    print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
    print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print("No. of days: 31 days")
else:
    print("Wrong month name") 


# In[27]:


# Q13. Write a Python program to check a triangle is equilateral, isosceles or
# scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.

print("Enter the length of sides ")

ab=eval(input("AB ="))
bc=eval(input("BC ="))
ca=eval(input("CA ="))
if (ab==bc==ca):
    print("Triangle is Equilateral")
elif (ab==bc) or (ab==ca) or (bc==ca):
    print("Triangle is Isosceles")
else:
    print("Triangle is Scalene")
   


# In[2]:


# Q14. Write a Python program to get next day of a given date
year = int(input("Input a year: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))


# date=input("Enter the date dd/mm/yyyy")
# date
# dd,mm,yy = date.split("/")
# dd=int(dd)
# mm=int(mm)
# yy=int(yy)
 
# if (mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
#       max1=31
# elif (mm==4 or mm==6 or mm==9 or mm==11):
#       max1=30
# elif (yy%4 ==0 and yy%100 !=0 or yy%400 ==0):
#       max1=29
# else:
#       max1=28
 
# if mm <1 or mm>12:
#       print("Date is invalid")
 
# elif (dd<1 or dd> max1):
#       print("Date is invalid")
 
# elif dd==max1 and mm !=12:
#       dd=1
#       mm=mm+1
#       print("the incremented date is :", dd,mm, yy)
# elif dd==31 and mm==12:
#       dd=1
#       mm=1
#       yy=yy+1
#       print("the incremented date is :", dd,mm, yy)
# else:
#       dd=dd+1
#       print("the incremented date is :", dd,mm, yy)


# In[ ]:


# Q15. Write a Python program to create the multiplication table of a number.
num = int(input("Enter the number: "))

print("Multiplication Table of", num)
for i in range(1, 11):
   print(num,"X",i,"=",num * i)


# In[ ]:


# Q16. Write a Python program to construct the following pattern, using a nested
# loop number.
# Expected Output:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

for i in range(10):
    print(str(i)*i)

