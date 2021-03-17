#!/usr/bin/env python
# coding: utf-8

# # Asignment Dictionary/Lists

# 1. Below are the two lists convert it into the dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# In[1]:


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print(dict(zip(keys,values)))


# 2. Merge following two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# In[19]:



dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)



dict3= {**dict1,**dict2}
print(dict3)


# In[12]:


# 3. Access the value of key ‘history’
# sampleDict = { "class":{ "student":{ "name":"Mike", "marks":{ "physics":70, "history":80 } } } }

sampleDict = { "class":{ "student":{ "name":"Mike", "marks":{ "physics":70, "history":80 } } } }

sampleDict["class"]["student"]["marks"]["history"]


# In[21]:


# 4. Initialize dictionary with default values
# employees = ['Kelly', 'Emma', 'John']
# defaults = {"designation": 'Application Developer', "salary": 8000}
employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

resDict = dict.fromkeys(employees, defaults)
print(resDict)


# In[22]:


# 5. Create a new dictionary by extracting the following keys from a given dictionary
# sampleDict = {
#  "name": "Kelly",
#  "age":25,
#  "salary": 8000,
#  "city": "New york"}
# Keys to extract
# keys = ["name", "salary"]
# Expected output:
# {'name': 'Kelly', 'salary': 8000}

sampleDict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ["name", "salary"]


newd= {k: sampleDict[k] for k in keys}
print(newd)


# In[25]:


# 6. Delete set of keys from Python Dictionary using comprehension
# sampleDict = {
#  "name": "Kelly",
#  "age":25,
#  "salary": 8000,
#  "city": "New york"
#  }
# keysToRemove = ["name", "salary"]
# Expected output:
# {'city': 'New york', 'age': 25}

sampleDict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ["name", "salary"]


newd= {k: sampleDict[k] for k in sampleDict.keys() - keys}
print(newd)


# In[27]:


# 7. Rename key city to location in the following dictionary
# sampleDict = {
#  "name": "Kelly",
#  "age":25,
#  "salary": 8000,
#  "city": "New york"
# }
# Expected output: (Hint:use pop)
# {
#  "name": "Kelly",
#  "age":25,
#  "salary": 8000,
#  "location": "New york"
# }

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sampleDict["Location"]= sampleDict.pop('city')
print(sampleDict)


# In[28]:


# 8. Get the key corresponding to the minimum value from the following dictionary
# sampleDict = {
#  'Physics': 82,
#  'Math': 65,
#  'history': 75
# }
# Expected output: Math 
sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(min(sampleDict, key=sampleDict.get))


# In[30]:


# 9. Write code to flip a dictionary — that is, to exchange its keys and values.
inv_map = {v: k for k, v in sampleDict.items()}
inv_map


# In[16]:


# 10. Create a database in the following format 
# Values = Router  1 1.1.1.1    zframez    zframez 
# Keys = (name)       (IP)     (username)   (pwd)
dict={}
dict["name"]="Connect"
dict["IP"]="1 1.1.1.1 "
dict["username"]="zframez"
dict["pwd"]="zframez "
print(dict)


# In[31]:


# 11. Write a python program to print the value of a given key
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
    if x in d:
        print(d[x])
    else:
        print('Key is not present in the dictionary')
is_key_present(5)



# In[34]:


# 12. Write a python program to check whether the given key is present, if present print the value , else add a new key
# and value

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def iskeypresent(x):
    if x in d:
        print(d[x])
    else:
        d[x]=x
        
iskeypresent(7)
print(d)


# In[17]:


# <!-- 13. Create a database in the following format
# Interface IP       status 
# Ethernet0 1.1.1.1   up
# Ethernet1 2.2.2.2  down
# Serial0 3.3.3.3     up
# Serial1 4.4.4.4      up 
db={}
db["Interface"]=["Ethernet0","Ethernet1","Serial0","Serial1"]
db["IP"]=["1.1.1.1","2.2.2.2","3.3.3.3","4.4.4.4"]
db["status"]=["up","down","up","up"]

print(db)


# In[1]:


# 14. Write a python program to find status of a given interface

database = {'interface':['Ethernet0','Ethernet1','Serial0','Serial1'],'ip':['1.1.1.1','2.2.2.2','3.3.3.3','4.4.4.4'],'status':['up','down','up','up']}

n = input("Enter interface ")
l1 = database['interface']
c=0
for i in l1:
    c+=1
    if i == n:
        print(database['status'][c-1])
        break
else:
    print("not in database")


# In[ ]:


# 15. Write a python program to find interface and IP of all interfaces which are up


l1 = database['interface']
l2 = database['ip']
l3 = database['status']
l = list(zip(l1,l2,l3))
#print(l)
for i in l:
    if i[2] == 'up':
        print(i[:2])


# In[ ]:


# 16. Write a python program to count how many ethernet interfaces are there

l1 = database['interface']
l2 = database['ip']
l3 = database['status']
l = list(zip(l1,l2,l3))
c=0
for i in l:
    if i[0][:8] == 'Ethernet':
        c+=1
print(c)   


# In[ ]:


# 17. Write a python program to add a new entry to above database


database = {'interface':['Ethernet0','Ethernet1','Serial0','Serial1'],'ip':['1.1.1.1','2.2.2.2','3.3.3.3','4.4.4.4'],'status':['up','down','up','up']}

a = input("Enter interface")
b = input("Enter ip")
c = input("Enter status")
l1 = database['interface']
l2 = database['ip']
l3 = database['status']
#rint(l1)
l1.append(a)
l2.append(b)
l3.append(c)
#database['interface'] = l1
print(database)


# In[38]:


# 18. Write a Python script to concatenate following dictionaries to create a new one.
#  Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
ne={**dic1,**dic2,**dic3}
print(ne)


# In[42]:


# 19 Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
n=eval(input("Enter a number"))
square_dict = {num: num*num for num in range(1, n+1)}
print(square_dict)




# In[44]:


# 20. Write a Python program to multiply all the items in a dictionary

my_dict = {'data1':100,'data2':3,'data3':24}
result=1
for key in my_dict:    
    result=result * my_dict[key]

print(result)


# In[46]:


# 21. Write a Python program to map two lists into a dictionary.
keys = ['red', 'green', 'blue']
values = ['#FF0000','#00FF00', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)


# In[48]:


# 22. Write a Python program to get the maximum and minimum value in a dictionary using lambda function.
dict1 = {i:i**2 for i in range(1,6)}
l1 = list(filter(lambda x:x,dict1.values()))
print(min(l1))
print(max(l1)


# In[49]:


# 23. Write a Python program to remove duplicate v
student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)


# In[ ]:


# 24. Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

sample = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

d1 = list(sample[0].values())
d2 = list(sample[1].values())
d3 = list(sample[2].values())
d = list(zip(d1,d2,d3))
#print(d)
l1 = []
if d1[0]==d2[0]:
    l1.append(d1[0])
    l1.append(d1[1]+d2[1])
if d1[0]==d3[0]:
    l1.append(d1[0])
    l1.append(d1[1]+d3[1])
if d2[0]==d3[0]:
    l1.append(d2[0])
    l1.append(d2[1]+d3[1])
for j in d[0]:
    if j not in l1:
        l1.append(j)
        ind = d[0].index(j)
        l1.append(d[1][ind])
newli1 = l1[::2]
newli2 = l1[1::2]
newdict = dict(zip(newli1,newli2))
newdict


# In[58]:


# 25. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}alues from Dictionary.
str1 = 'w3resource' 
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)


# In[59]:


# 26. Write a Python program to get the top three items in a shop.
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

# sampleDict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# print(min(sampleDict, key=sampleDict.get))
# print(sampleDict[min(sampleDict, key=sampleDict.get)])

sampledata = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
s = sorted(sampledata.values(),reverse = True)
newdict1 = {k:v for (k,v) in sampledata.items() if v>=s[2]}
newdict2 = {k:v for (k,v) in sorted(newdict1.items(),key = lambda i:i[1],reverse = True)}
newdict2


# In[62]:


# 27. Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
for (key, value) in set(x.items()) & set(y.items()):
    print('%s: %s is present in both x and y' % (key, value))


# In[64]:


# 28. Write a Python program to store a given dictionary in a json file.
# Original dictionary:
# {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ',
# 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
# <class 'dict'>
# Json file to dictionary:
# {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ',
# 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
d={'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ',
'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}

print(d)



# In[77]:


# 29. Write a Python program to convert more than one list to nested dictionary.
# Original strings:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
def nested_dictionary(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result

student_id = ["S001", "S002", "S003", "S004"] 
student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
student_grade = [85, 98, 89, 92]
print("Original strings:")
print(student_id)
print(student_name)
print(student_grade)
print("\nNested dictionary:")
ch='a'
print(nested_dictionary(student_id, student_name, student_grade))


# In[13]:


# 30. Write a Python program to find the length of a given dictionary values.
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Length of dictionary values:
# {'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}
lst=[]
histo={}  #empty dictionary  or histogram
def hist(ab):
    for i in ab.values():
        lst.append(i)
        if i in histo:
            #this value is already present in dictionary
            histo[i]=len(i)
        else:
            #this value is  not already present in dictionary
            histo[i]=len(i)
# ab={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# hist(ab)
# print("Length of dictionary values are ",histo)
ab1={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
hist(ab1)
print("Length of dictionary values are ",histo)


# In[10]:


# 31. Write a Python program to convert a given dictionary into a list of lists. Go to the editor
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Convert the said dictionary into a list of lists:
# [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]

originaldictionary =  {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
newlist = [[k,v] for (k,v) in originaldictionary.items()]
newlist


# In[ ]:


# 32. Write a Python program to filter even numbers from a given dictionary values. Go to the editor
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}

originaldictionary = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
#newdict = {k:v for (k,v) in originaldictionary.items() for i in v if i%2==0}

newdict = {}
for k,v in originaldictionary.items():
    newlist = []
    for i in v:
        if i%2==0:
            newlist.append(i)
    newdict[k] = newlist
newdict


# In[7]:


# 33. Write a Python program to count the frequency in a given dictionary. Go to the editor
# Original Dictionary:
# {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
# Count the frequency of the said dictionary:
# Counter({10: 2, 40: 2, 20: 2, 70: 1, 80: 1})

lst=[]
histo={}  #empty dictionary  or histogram
def hist(ab):
    for i in ab.values():
        lst.append(i)
        if i in histo:
            #this value is already present in dictionary
            histo[i]=histo[i]+1
        else:
            #this value is  not already present in dictionary
            histo[i]=1
ab={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
hist(ab)
print("Count of each frequency is ",histo)


# In[ ]:




