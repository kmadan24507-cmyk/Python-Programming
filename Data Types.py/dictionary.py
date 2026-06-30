# DICTIONARY = DICTIONARY STORES ITEMS OR DATA AS KEY : VALUE ----> IT IS MUTABLE BUT NOT KEY
person = dict(Name = "Madan",Age = 188,City = "Tirupati")
person = {"Name"  : "Madan", "Age" : 19,"City":"Tirupati"}
print(person["Name"])
print(person["Age"])
print(person["City"])
keys = ("a","b","c")
d = dict.fromkeys(keys,0)
print(d)
# GET  = returns Value
student = {"Name" : "Dilip","Age" : 26,"Gender":"Male"}
print(student.get("Name"))
print(student.get("Age"))
print(student.get("Gender"))
print(student.get("Grade")) # Gives NONE
# OR
print(student.get("Grade","Not Found")) # Not Found
# IT IS MUTABLE
student = {"Name" : "Dilip","Age" : 26,"Gender":"Male"}
student["Age"] = 27
print(student)
# POP
student = {"Name" : "Dilip","Age" : 26,"Gender":"Male"}
student.pop("Name")
print(student)
# CLEAR
student = {"Name" : "Dilip","Age" : 26,"Gender":"Male"}
student.clear()
print(student)
print(len(student))
# FOR LOOP
student = {"Name" : "Dilip","Age" : 26,"Gender":"Male"}
for i in student:
    print(i) # i = KEY
for j in student.values():
    print(j) # j = Value
for i,j in student.items():
    print(i,j) 
# UPDATE
student = {"Name" : "Dilip","Age" : 26,"Gender":"Male"}
student.update({"Age":19})
print(student)
# DICT COMPREHENSION
squares = {x:x*x for x in range(1,11)}
print(squares)
# COPY AND DEEEPCOPY
# DEEPCOPY = When nested dicts are exists
student = {"Name" : "Dilip","Age" : 26,"Gender":"Male"}
student1 = student.copy()
print(student1)
# PROBLEMS - 
# 1 . 
student = {"Name"   : "K.Madan Kumar",
           "Age"    : 19,
           "City"   : "Tirupati",
           "Course" : "Python",
           "Marks"  : 0.0}
print(student)
# 2 . KEY ---> VALUE
print(student["Name"])
print(student["Age"])
print(student["City"])
print(student["Course"])
print(student["Marks"])
# 3 . UPDATE
student["Gender"] = "Male"
student.update({"College" : "Sai University"})
print(student)
# 4 . DELETE
del student["College"]
student.pop("Gender")
student.popitem()   # LAST INSERTED ITEM WILL BE DELETED
#student.clear()
print(student)
# 5 . 
print(f"Length of dict = {len(student)}")
# 6 .
# A ---> KEY
if "Name" in student:
    print("Key exists")
else:
    print("Key does not exists")
# B ---> VALUE
if 19 in student.values():
    print("Value Exits")
else:
    print("Value does not exists")
# 7 . KEYS,VALUES,ITEMS
print(student.keys())
print(student.values())
print(student.items())
# 8 . LOOPS
for i in student:
    print(i)     # KEYS
for j in student.values():
    print(j)     # VALUES
for i,j in student.items():
    print(i,":",j) # ITEMS
# 9 . GET FUNCTION
print(student.get("Name"))
print(student.get("Age"))
print(student.get("Height","-"))
# 10 . MERGE TWO DICTS
d1 = {"A" : 10 , "B" : 20}
d2 = {"C" : 30 , "D" : 40}
d1.update(d2)
print(d1)
# 11 . MAX AND MIN KEY AND VALUE IN DICT
student_marks = {
    "John": 85,
    "Alice": 92,
    "Bob": 98,
    "David": 88
}
max_key = max(student_marks)
min_key = min(student_marks)
max_value = max(student_marks.values())
min_value = min(student_marks.values())
print(f"Maximum Key = {max_key}")
print(f"Minimum Key = {min_key}")
print(f"Maximum Value = {max_value}")
print(f"Minimum Value = {min_value}")
# 12 .  REVERSE KEYS AND VALUES
d = {"A" : 10 , "B" : 20 , "C" : 30}
reverse = {}
for i,j in d.items():
    reverse[j] = i
print(reverse)
# 13 . 
keys = ["A" , "B" , "C"]
values = [10,20,30]
d = dict(zip(keys,values))
print(d)
# 13 . 
# A ---> FROM LISTS
keys = ["A" , "B" , "C"]
values = [10,20,30]
d = dict(zip(keys,values))
print(d)
# B ---> FROM TUPLES
d = [("A",10),("B",20),("C",30)]
d1 = dict(d)
print(d1)
# C --->FROM STRING
s = "MADAN KUMAR"
d = {}
for i in s:
    d[i] = ord(i)
print(d)
# 14 . SORTING
# A ---> 
d = {"c": 30, "a": 10, "b": 20}
for i in sorted(d):
    print(i,d[i])
# B ---> KEYS
d = {"c": 30, "a": 10, "b": 20}
sorted_dict = dict(sorted(d.items()))
print(sorted_dict)
# C ---> VALUES
from  operator import itemgetter
d = {"c": 0, "a": 10, "b": 20}
sorted_dict1 = dict(sorted(d.items(),key = itemgetter(1)))
print(sorted_dict1)
# 15 . SUM OF ALL VALUES IN DICT
# A ---> USING SUM
d = {"A" : 10 , "B" : 20}
print(sum(d.values()))
# B ---> USING LOOP
d = {"A" : 10 , "B" : 20}
sum = 0
for i in d.values():
      sum+=i
print(sum)
# 16 . MULTIPLY ALL ITEMS IIN DICT
#  USING LOOP
d = {"a": 10, "b": 20, "c": 30}
product = 1
for i in d.values():
    product*=i
print(product)
# 17 . CHECK DICT IS EMPTY OR NOT
d = {}
if not d:
    print("Dictionary is Empty")
else:
    print("Dictionary is not empty")
# 18 . REMOVE KEYS
# A ---> ONE KEY
d = {"a": 10, "b": 20, "c": 30}
del d["a"]
print(d)
# B ---> MULTIPLE KEYS
d = {"a": 10, "b": 20, "c": 30}
keys = ["a","b"]
for i in keys:
    del d[i]
print(d)
# 19 . 
# A ---> CONVERTING TO LIST
d = {"a": 10, "b": 20, "c": 30}
print(list(d.values())[0])
print(list(d.values())[1])
print(list(d.values())[-1])
# B ---> USING LOOP
d = {"a": 10, "b": 20, "c": 30}
count = 0
for i in d.values():
    count+=1
    if count == 1:
        print(i)
        break
# 20 . REMOVE DUPLICATES
# A ---> VALUES
d = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 30,
    "E": 20
}
result = {}
for i,j in d.items():
    if j not in result.values():
        result[i] = j
print(result)
# B ---> KEYS
d = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 30,
    "A": 20
}
result1 = {}
for i,j in d.items():
   if i not in result1:
       result1[i] = j
print(result1)
# 21 . 
d1 = {'a': 100, 'b': 200, 'c': 600}
d2 = {'a': 300, 'b': 100, 'c': 400}
result = d1.copy()
for i,j in d2.items():
    if i in result:
        result[i]+=j
    else:
        result[i] = j

print(result)
# 22 . COUNT FREQUENCY OF CHARACTERS
# A ---> USING GET
s = "K.Madan Kumar"
freq = {}
for i in s:
    freq[i] = freq.get(i,0) + 1
print(freq)
# B ---> USING LOOP
s = "K.Madan Kumar"
freq = {}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1
print(freq)
# 23 . COUNT FREQUENCY OF WORDS
# A ---> USING GET
word = "Python is an most used programming language"
freq = {}
for i in word.split():
    freq[i] = freq.get(i,0) + 1
print(freq)
# B ---> USING LOOP
word = "Python is an most used programming language"
freq = {}
for i in word.split():
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1
print(freq)
# 24 . 
# A --->
words = ["Cat","Dog","Goat","Cow","Man","Lion","Tiger"]
result = {}
for i in words:
    l = len(i)
    if l not in result:
        result[l] = []
    result[l].append(i)
print(result)
# B --->
nums = [1,2,3,4,5]
result1 = {"Even": [] , "Odd" : []}
for i in nums:
    if i % 2 == 0:
        result1["Even"].append(i)
    else:
        result1["Odd"].append(i)
print(result1)
# 25 . REVERSE A DICT
d = {"A" : 10 , "B" : 20 , "C" : 30}
rev = {}
for i,j in d.items():
    rev[j] = i
print(rev)
# 26 . FIND COMMON KEYS AND VALUES
# A ---> KEYS
d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 100, "c": 200, "d": 300}
for i in d1:
    if i in d2:
        print(i)
# B ---> VALUES
d1 = {"a": 10, "b": 200, "c": 300}
d2 = {"b": 100, "c": 200, "d": 300}
for i in d1.values():
    if i in d2.values():
        print(i)
# 27 . FIND UNCOMMON KEYS AND VALUES
# A ---> KEYS
d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 100, "c": 200, "d": 300}
for i in d1:
    if i not in d2:
        print(i)
for i in d2:
    if i not in d1:
        print(i)
# B ---> VALUES
d1 = {"a": 100, "b": 200, "c": 30}
d2 = {"b": 100, "c": 200, "d": 300}
for j in d1.values():
    if j not in d2.values():
        print(j)
for j in d2.values():
    if j not in d1.values():
        print(j)
# 28 . FIND KEYS HAVING SAME VALUES
d = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 30
}
for i in d:
    for j in d:
        if i!=j and d[i] == d[j]:
            print(i,j)
# 29 . INTERSECTION
d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"a": 10, "b": 50, "d": 40}
result = {}
for i,j in d1.items():
    if i in d2 and d2[i] == j:
        result[i] = j
print(result)
# 30 . SQUARES OF DICT
# A ---> USING LOOP
d = {"A" : 1,
     "B" : 2,
     "C" : 3,
     "D" : 4}
for i,j in d.items():
    print(i,":",j*j)
# B ---> USING DICT COMPREHENSION
d = {x : x*x for x in range(1,6)}
print(d)
# C ---> USING LOOP
squares = {}
for i in range(1,6):
    squares[i] = i*i
print(squares)
# 30 . CUBE OF DICT
# A ---> USING LOOP
d = {"A" : 1,
     "B" : 2,
     "C" : 3,
     "D" : 4}
for i,j in d.items():
    print(i,":",j*j*j)
# B ---> USING DICT COMPREHENSION
d = {x : x*x*x for x in range(1,6)}
print(d)
# C ---> USING LOOP
squares = {}
for i in range(1,6):
    squares[i] = i*i*i
print(squares)
# 31 . MULTIPLICATION TABLE
# A ---> USING LOOP
n= int(input("Enter The Number  : "))
table = {}
for i in range(1,11):
    table[i]  = n * i
print(table)
#  B ---> USING DICT COMPREHENSION
n = 5
table = {x : n*x for x in range(1,11)}
print(table)
# C ---> TABLES 1-5
tables = {}
for i in range(1,6):
    tables[i] = {i : n*i for i in range(1,11)}
print(tables)
# 32 . COUNT VOWELS 
s = "Aadan Kumar"
vowels = "aeiouAEIOU"
count = {}
for i in s:
    if i in vowels:
        count[i] = count.get(i,0) + 1
print(count)
# 33 . COUNT CONSONANTS
s = "Madan Kumar"
vowels = "aeiouAEIOU"
count = {}
for i in s:
    if i.isalpha() and i not in vowels:
        count[i] = count.get(i,0) + 1
print(count)
# 34 . 
d = {}
n = int(input())
for i in range(n):
    key = input("Enter Key : ")
    value = input("Enter Value : ")
    d[key] = value
print(d)
#NESTED DICT
students = {"John":{"Age" : 20,
                    "Marks" : 90},
            "Motu" : {"Age" : 20,
                      "Marks" : 93}}
# 35 . 
print(students)
# 36 . 
print(students["John"]["Marks"])
print(students["John"]["Age"])
print(students["Motu"]["Age"])
print(students["Motu"]["Marks"])
# 37 . 
students["John"]["Gender"] = "Male"
students["Motu"]["Gender"] = "Female"
print(students)
# 38 . 
del students["John"]["Gender"]
del students["Motu"]["Gender"]
print(students)
# 39 . PRINT KEYS AND VALUES
# A ---> KEYS
for i in students:
    for j in students[i]:
        print(j)
# B ---> VALUES
for i in students:
    for j in students[i].values():
        print(j)
# 40 . LENGTH OF DICT
print(len(students))
count = 0
for i in students:
    count+=len(students[i])
print(count)
# 41 . MERGE TWO DICT
# A ---> USING UPDATE
d1 = {"Student" : {"Name" : "K.Madan Kumar"}}
d2 = {"Student" : {"Marks" : 90}}
d1["Student"].update(d2["Student"])
print(d1)
# 42 . FIND MAXIMUM NESTED VALUE
students = {"John" : {"Marks" : 100},
            "Motu" : {"Marks" : 99},
            "Patlu" : {"Marks" : 98}}
maximum = students["John"]["Marks"]
for i in students:
    if students[i]["Marks"] > maximum:
        maximum = students[i]["Marks"]
print(maximum)
# 43 . FIND MINIMUM NESTED VALUE
students = {"John" : {"Marks" : 100},
            "Motu" : {"Marks" : 99},
            "Patlu" : {"Marks" : 98}}
minimum = students["John"]["Marks"]
for i in students:
    if students[i]["Marks"] < minimum:
        minimum = students[i]["Marks"]
print(minimum)
# 44 . SUM OF NESTED DICTS
students = {"John" : {"Marks" : 100},
            "Motu" : {"Marks" : 99},
            "Patlu" : {"Marks" : 98}}
sum = 0
for i in students:
    sum+=students[i]["Marks"]
print(sum)
# 45 . FIND TOPPER
students = {"John" : {"Marks" : 100},
            "Motu" : {"Marks" : 99},
            "Patlu" : {"Marks" : 98}}
maximum = 0
topper = ""
for i in students:
    if students[i]["Marks"] > maximum:
        maximum = students[i]["Marks"]
        topper = i
print(topper,maximum)
# 46 . 
company = {
    "IT": {
        "John": 50000,
        "Alice": 60000
    },
    "HR": {
        "Bob": 45000
    }
}
highest = 0
employee = ""
for i in company:
    for j in company[i]:
        if company[i][j] > highest:
            highest = company[i][j]
            employee = j
print(employee,highest)
# DICTIONARY COMPREHENSION
# 47 . SQUARES
d = {i : i * i for i in range(1,11)}
print(d)
# CUBES
d = {i : i**3 for i in range(1,11)}
print(d)
# EVEN
# d = {i : i % 2 == 0 for i in range(1,11)} # IT RETURNS BOOLEAN
d = {i : i for i in range(1,11) if i % 2 == 0}
print(d)
# ODD
d = {i : i for i in range(1,11) if i % 2 != 0}
print(d)
# 48 .
d = {"A" : 10,
     "B" : 20,
     "C" : 30,
     "D" : 40}
result = {i : j for i,j in d.items() if j > 20}
print(result)
# 49 . PRINT VOWELS STARTED WORD
d = {"Apple" : 10,
     "Ball" : 20,
     "Cat" : 30,
     "Egg" : 40}
result = {i : j for i,j in d.items() if i[0].lower() in "aeiouAEIOU"}
print(result)
# 50 . CONVERT INTO UPPERCASE AND LOWERCASE
d = {"a" : "python",
     "b" : "java",
     "c" : "html"}
result = {i : j.upper() for i,j in d.items()}
print(result)
d = {"a" : "PYTHON",
     "b" : "JAVA",
     "c" : "HTML"}
result = {i : j.lower() for i,j in d.items()}
print(result)
# 51 . 
s = "Madan Kumar"
result = {i : ord(i) for i in s}
print(result)
result = {chr(i) : i for i in range(65,91)}
print(result)
# 52 . FACTORIAL , PRIME NUMBERS
d = {}
for i in range(1,6):
    fact = 1
    for j in range(1,i+1):
        fact*=j
    d[i] = fact
print(d)
d = {}
for i in range(2,21):
     prime = 0
     for j in range(2,i):
        if i % j == 0:
            prime+=1
     if prime == 0:
         d[i] = "Prime"
     else:
         d[i] = "Not Prime"
print(d)
# 53 . 
marks = {
    "John": 85,
    "Alice": 92,
    "Bob": 65,
    "David": 45
}
grade = {}
for i,j in marks.items():
     if j >= 90:
        grade[i] = "A"
     elif j >= 75:
        grade[i] = "B"
     elif j >= 50:
         grade[i] = "C"
     else:
         grade[i] = "F"
print(grade)