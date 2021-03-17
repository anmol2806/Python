#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1 Write a program to input three nos and print the greatest.
a= eval(input("Enter first number a= "))
b=eval(input("Enter second number b= "))
c= eval(input("Enter third number c= "))
if a>b:
    if a>c:
        print("The greater number is a =",a)
    else:
        print("The greater number is c =",c)
else: 
    if b>c:
        print("The greater number is b",b)
    else:
        print("The greater number is c =",c)


# In[ ]:


#Q2 Write a program to input two numbers, add them, multiply them,
# divide them, find remainder
d= eval(input("Enter first number d = "))
e =eval(input("Enter second number e = "))
sum1=d+e
mult=d*e
div=d/e
rem=d%e
print("Sum of "+  str(d) + " and " + str(e) + " is ",sum1)
print("Multiplication of "+ str(d) + " and " + str(e) + " is ",mult)
print("Division of "+ str(d) + " by " + str(e) + " is ",div)
print("Remainder when "+ str(d) + " is divided by " + str(e) + " is ",rem)


# In[ ]:


#Q3 Write a program to input a figure like C , R, S
# (C for circle, r for rectange and s for square)
# Check the figure and appropriately ask the parameters for calculating the area.
# Give an error message if something else is # entered.
fig = input("Enter figure (C/R/T):")
area=0
if fig =='C' or fig =='c' :
    r =eval(input("enter the radius: "))
    area =22/7*r**2
  
elif fig=='R' or fig=='r':
    l =eval(input("enter the length: "))
    b =eval(input("enter the breadth: "))
    area=l*b
   
elif fig=='T' or fig=='t':
    h =eval(input("enter the height: "))
    b =eval(input("enter the base: "))
    area=1/2*b*h
    
else:
    print("invalid figure")
print(area) 


# In[ ]:


# Q4 Input Name and Bp of employee.
# calculate gross pay and net pay
# grosspay= bp + da + hra -Pf
# pf=12% of bp
# hra is 20% of bp but maximum can be 2000 only
# da is 20% of bp for bp < 3 lac
# otherwise
# da is 30% of bp
# netpay=grosspay - pf
Name= (input("Enter Name = "))
bp =eval(input("Enter basic pay = "))

pf = 12/100*bp

hra= 20/100*bp
if hra > 2000:
    hra=2000
else :
    hra =hra

if bp>300000:
    da =30/100*bp 
else:
    da =20/100*bp 

gp= bp+da+hra -pf

np= gp-pf

print("The grosspay is ", gp)
print("The netpay is ", np)


# In[ ]:


# Q5 Calculate the income tax of an employee
# input the income
# if income < 3 lac no tax
# if income between 3 and 5 , tax = 20%
# if income between 5 and 8 , tax = 30%
# else
# tax=40%
inc =eval(input("Enter income = "))
if inc< 300000:
    tax=0
elif 300000<=inc <500000:
    tax= 20/100*inc
elif 500000<=inc <800000:
    tax= 30/100*inc
else:
    tax=40/100*inc

print("The income tax is ", tax)


# In[ ]:


#Q6 Enter a four digit number, check whether its leap year.
ye =eval(input("Enter year = "))
if ye % 4 ==0 :
    if  ye %100 ==0:
        if ye % 400 ==0:
            print(str(ye)+ " is a leap year")
        else:
            print(str(ye)+ " is not a leap year")
    else:
        print(str(ye)+ " is a leap year")
else: 
    print(str(ye)+ " is not a leap year")


# In[ ]:


#Q7 print sum of first 10 numbers
n=int(input("Enter  number = "))
sum= n*(n+1)/2
print("Sum of first "+ str(n) + " numbers is ", sum)


# In[ ]:


#Q8 enter a no and print whether its prime
num=int(input("Enter  number = "))
if num>1:
    for i in range (2,num):
        if num % i ==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")


# In[1]:


#Q9 enter two ranges eg start 100 to stop 1000 and print all prime numbers between the two ranges.
lb=int(input("Enter lower bound = "))
ub=int(input("Enter upper bound = "))
num2=int(input("Enter  number = "))
if (num2 > lb) and (num2<ub):
    if num2>1:
        for i in range (2,num2):
            if num2 % i ==0:
                print(num2,"is not a prime number")
                break
        else:
            print(num2,"is a prime number")
    else:
        print(num2,"is not a prime number")
else:
    print("out of range")


# In[ ]:


# #Q10 enter a no print sum of its digits
# Eg 4567
# 22
# 4
n=eval(input("Enter  number  = "))
sum=0
while(n!=0):
    sum=sum+ int(n%10)
    n=int(n/10)
print(sum)


# In[ ]:


#Q11 print the sum of digits till you get a single number.


# In[ ]:


#Q12 Print Fibonicci series upto given terms


# In[ ]:


#Q13 Enter 8 numbers, print their average.
n1=eval(input("Enter  number 1 = "))
n2=eval(input("Enter  number 2 = "))
n3=eval(input("Enter  number 3 = "))
n4=eval(input("Enter  number 4 = "))
n5=eval(input("Enter  number 5 = "))
n6=eval(input("Enter  number 6 = "))
n7=eval(input("Enter  number 7 = "))
n8=eval(input("Enter  number 8 = "))
sum= n1+n2+n3+n4+n5+n6+n7+n8
avg=sum/8
print("Average of 8 numbers is ", avg)

