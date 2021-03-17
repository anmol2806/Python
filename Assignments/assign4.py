#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Q1. Write a function ends() that takes in a string from the user
# and prints just the first two and the last two characters of the
# string. You may assume that any input will be at least 2
# characters long.
# Enter a string >>> spring 3
# spng

def end():
    str=input("enter a string ")
    str=str.lstrip(" ")
    str=str.rstrip(" ")
    if len(str)<2:
        return ' '
    else:
        return str[0:2]+str[-2:]
end()


# In[19]:


# Q2 Write a function mix() that takes two strings a and b and prints
# the two strings concatenated, but with the first two characters of
# each word swapped with the other word’s first two characters.
# You may assume that any input will be at least two characters
# long.
# For example:
# String a >>> german
# String b >>> english
# Output -> enrman geglish
# Example 2 :
# String a >>> dog
# 3 String b >>> dinner
# 4 dig donner

def mix():
    s1=input("enter a string ")
    s2=input("enter a string ")
    s3=s1
    s1=s1.replace(s1[0:2],s2[0:2])
    s2=s2.replace(s2[0:2],s3[0:2])
    print(s1 +" " + s2)
mix()


# In[12]:


# Q3 Write a function split which divides a string into two halves. If
# the length is even, the front and back halves are the same length.
# If the length is odd, we’ll say that the extra character goes in the
# front. For example, in ’abcde’, the front half is ’abc’ and the back
# half is ’de’. Write a function that takes in two strings a and b and
# prints a-front + b-front + a-back + b-back.
# Eg1
# String a >>> abcd
# String b >>> efghi
# abefgcdhi
# Eg 2
# String a >>> this dinner is
# String b >>> what am i doing1
# this diwhat am nner isi doing1


def split(a,b):
    l1 = len(a)
    l2 = len(b)
    if l1%2 == 0:
        mid1 = l1//2
    else:
        mid1 = l1//2 + 1
    if l2%2 == 0:
        mid2 = l2//2
    else:
        mid2 = l2//2 + 1
    
    c = a[:mid1] + b[:mid2] + a[mid1:] + b[mid2:]
    return c

a = input("Enter string a : ")
b = input("Enter string b : ")
s = split(a,b)
print(s)


# In[13]:


# Q4. Any fraction can be written as the division of two integers.
# You could express this in Python as a tuple – (numerator,
# denominator). Write functions for each of the following. They must
# use the tuple representation to return fractions.
# 1. Given two fractions as tuples, multiply them.
# 2. Given two fractions as tuples, divide them.
# 3. Given a list of fractions as a tuple, return the one that is
# smallest in value.
# Also write a small command-line interface such that the user
# running your script sees something like this:
# == Multiplication and Division ==
# Enter a fraction >>> 5/3
# Enter a fraction >>> 10/3
# Multiplication of the fractions: 50/9
# Division of the first by the second: 5/10
# Smallest fraction
# Enter a fraction >>> 1/3
# Enter a fraction >>> 10/3
# Enter a fraction >>> 6/4
# Enter a fraction >>> stop
# Output Smallest fraction: 1/3

def multi(c1,c2,d1,d2):
    #print(c1,c2,d1,d2)
    return (c1/c2)*(d1/d2)
    
def div(c1,c2,d1,d2):
    return (c1/c2)/(d1/d2)
        
def smallest():
    a =[]
    b =[]
    while True:
        a.append(input("Enter a fraction : "))
        if a[len(a)-1] in ['stop' or 'STOP' or 'Stop']:
            break
    for i in range(len(a)-1):
        f = a[i].find("/")
        c = int(a[i][:f])
        d = int(a[i][f+1:])
        b.append(c/d)
        
        
    m = min(b)
    j = b.index(m)
    return a[j]
print("== Multiplication and Division ==")
a = input("Enter a fraction : ")
b = input("Enter a fraction : ")
f1 = a.find("/")
f2 = b.find("/")
c1 = int(a[:f1])
c2 = int(a[f1+1:])
d1 = int(b[:f2])
d2 = int(b[f2+1:])    
m = multi(c1,c2,d1,d2)
print("Multiplication of the fractions: ",m)
d = div(c1,c2,d1,d2)
print("Division of the first by the second: ",d)
print("Smallest Fraction")
s = smallest()
print("Smallest no is : ",s)


# In[ ]:


# Q5. Take in numbers as input until “stop” is entered. Then split
# the numbers into three lists: one containing all the numbers, one
# containing all even values, and one containing all odd. Print out all
# three lists, as well as each list’s sum and average. Assume all
# input values are integers.


#     b=int(input("Enter element:"))
#     l1.append(b)
# print("list is ",l1)
main1 = []
main2 = []
even = []
odd = []
while True:
    main1.append(input("Enter value or stop to end:"))
    if main1[len(main1)-1] in ['stop','STOP','Stop']:
        break
main1.pop()
main2 = [int(i) for i in main1]
print("All the numbers: ",main2)
for i in main2:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even elements are: ",even)
print("Odd elements are: ",odd)


# In[14]:


# Q6. Take in numbers as input until “stop” is entered. As you take
# in each number, insert it into a list so that the list is sorted in
# ascending order. That is, look through the list until you find the
# place where the new element belongs. If the number is 21 is
# already in the list, do not add it again. After “stop” is entered, print
# out the list. Do not use any of Python’s built-in sorting functions.
# Example :
# 1 Input a number >>> 12
# 2 List contains [12.0]
# 3 Input a number >>> 5.2
# 4 List contains [5.2, 12.0]
# 5 Input a number >>> 73
# 6 List contains [5.2, 12.0, 73.0]
# 7 Input a number >>> 45
# 8 List contains [5.2, 12.0, 45.0, 73.0]
# 9 Input a number >>> 100
# 10 List contains [5.2, 12.0, 45.0, 73.0, 100.0]
# 11 Input a number >>> -5
# 12 List contains [-5.0, 5.2, 12.0, 45.0, 73.0, 100.0]
# 13 Input a number >>> 2.3
# 14 List contains [-5.0, 2.3, 5.2, 12.0, 45.0, 73.0, 100.0]
# 15 Input a number >>> stop
# 16 [-5.0, 2.3, 5.2, 12.0, 45.0, 73.0, 100.0].
def mysort(list1):
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[j]<list1[i]:
                list1[i],list1[j] = list1[j],list1[i]
    return list1

main1 = []
main2 = []
while True:
    main1.append(input("Enter value or stop to end:"))
    if main1[len(main1)-1] in ['stop','STOP','Stop']:
        break

    main2 = [int(i) for i in main1]
    main2 = mysort(main2)
    print(main2)


# In[39]:


# Q7. Write the following functions:
# overlap() Given two lists, find a list of the elements common to
# both lists and return it.
# join() Given two lists, join them together to be one list without
# duplicate elements and return that list.
def overLap(a,b):
    as1=set(a)
    bs=set(b)
    if as1 & bs:
        print(as1 & bs)
    else:
        print("no common element")


def join(a, b, m, n): 
    i, j = 0, 0
    while i < m and j < n: 
        if a[i] < b[j]: 
            print(a[i]) 
            i += 1
        elif b[j] < a[i]: 
            print(b[j]) 
            j+= 1
        else: 
            print(b[j]) 
            j += 1
            i += 1
  
    # Print remaining elements of the larger array 
    while i < m: 
        print(a[i]) 
        i += 1
  
    while j < n: 
        print(b[j]) 
        j += 1
a = [1, 2, 3, 4, 5,6] 
b = [5, 6, 7, 8, 9] 
overLap(a,b)

m = len(a) 
n = len(b) 
join(a, b, m, n)


# In[45]:


# Q8. Create a list, squares, that consists of the squares of the
# numbers 1 to 10. A list comprehension could be useful here.
# ***Use filter() and a lambda expression to print out only the
# squares that are between 30 and 70 (inclusive).
list1=[i**2 for i in range(1,11) ]
print(list1)
r1=list(filter(lambda x: x<=70 and x>=30,list1))
print(r1)


# In[55]:


# Q9. Define a function called count that has two arguments called
# sequence and item. Return the number of times the item occurs in
# the list.For example: count([1,2,1,1], 1) should return 3 (because
# 1 appears 3 times in the list).
def count(lst, a):
    c=0
    for i in range(len(lst)):
        if lst[i]==a:
            c+=1
    return c


d=count([100,92,100,75,100,25, 100],100)
print(d)


# In[63]:


# Q10. Use a list comprehension to create a list, `cubes_by_four.
# The comprehension should consist of the cubes of the numbers 1
# through 10 only if the cube is evenly divisible by four. Finally, print
# that list to the console. Note that in this case, the cubed number
# should be evenly divisible by 4, not the original number.
lis21=[i**3 for i in range(1,11) if (i**3)%4==0]
print(lis21)


# In[73]:


# Q11. Create a list, to_21, that's just the numbers from 1 to 21,
# inclusive. Create a second list, odds, that contains only the odd
# numbers in the to_21 list (1, 3, 5, and so on). Use list slicing for
# this one instead of a list comprehension. Finally, create a third
# list, middle_third, that's equal to the middle third of `to_21, from 8
# to 14, inclusive.
l3=[i for i in range(1,22)]
odds=[]
odds =l3[0:21:2]
middle=l3[7:14]
print(l3)
print(odds)
print(middle)


# In[101]:


# Q12. The string
# garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"`
# is garbled in two ways:
# First, our message is backwards;
# Second, the letter we want is every alternate letter.
# Use lambda and filter to extract the message and save it to a
# variable called message. Use list slicing to extract the message
# and save it to a variable called message.

st="!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
# using slicing
# st=st[::-1]
# st=st[0::2]
# print(st)


#using filter and lambda function
rs=list(filter(lambda x : x!="X"  ,st))
rs.reverse()
mss=" "
for i in rs:
    mss+=i
print(mss)


# In[127]:


# Q13 Q Write a python program to read three numbers (a,b,c) and
# check how many numbers between ‘a’ and ‘b’ are divisible by ‘c’
a,b,c=int(input()),int(input()),int(input())
count=0
for i in range(a,b):
    if i%c==0:
        count+=1
print(count)


# In[15]:


# Q14. Q Pig Latin is a language game, where you move the first
# letter of the word to the end and add "ay." So "Python" becomes
# "ythonpay." To write a Pig Latin translator in Python, here are the
# steps we'll need to take:
# Ask the user to input a word in English.
# Make sure the user entered a valid word.
# Convert the word from English to Pig Latin.
# Display the translation result.


def piglatin(word: str) -> str:
    if word[0] in 'aeiou':
        complementary = 'way'
    else:
        complementary = f'{word[0]}ay'

    return f'{word[1:]}{complementary}'


if __name__ == '__main__':
    words = [
        'Dog',
        'Calender',
        'python'
    ]

    for word in words:
        print(f'{word} is {piglatin(word).title()} in piglatin Language')

        
        
        
str1 = input("Enter a string")
s = str1[0]
str2 = str1[1:] + s +'ay'
str2


# In[120]:


# Q15. Q Write a program that generates a random number (0-10)
# and ask you to guess it. You have three asserts.
# Define a random_number with randint between 0-10.
# Initialize guesses_left to 3.
# Use a while loop to let the user keep guessing so long as
# guesses_left is greater than zero.
# Ask the user for their guess.
# If they guess correctly, print 'You win!' and break. Decrement
# guesses_left by one.
# Use an else: case after your while loop to print:You lose.
import random
r=random.randint(0,10)
print(r)
guess_left=3
while guess_left!=0:
    n=int(input("enter a number betweeen 0 to 10:"))
    if n==r:
        print("You win")
        break
    else:
        guess_left=guess_left-1
else:
    print("you lose")

