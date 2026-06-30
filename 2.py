# PROBLEMS
# 1 . CREATE DICTIONARY
details = {"Name" : "K.Madan Kumar",
           "Age" : 19,
           "Gender" : "Male",
           "City" : "Tirupati",
           "College" : "Sai University"}
print(details)
print(details.keys())
print(details.values())
print(details["Age"])      # If there is no key = keyerror
print(details.get("Age"))  # if there is no key = None
details["Course"] = "Python"
print(details)
details.update({"Grade" : 8.9})
print(details)
del details["Grade"]
print(details)
details.pop("Course")
print(details)
if "Age" in details:
    print("Key Exists")
else:
    print("Key Does Not Exists")
if details.get("Age") is not None:
    print("Key Exists")
else:
    print("Key Does Not Exists")
# 2 . Count keys,values and items in a dictionary
product = {
    "name": "Laptop",
    "price": 50000,
    "stock": 10,
    "brand": "Dell",
    "ram": "16GB"
}
print(f"No.of Keys = {len(product.keys())}")
print(f"No.of Values = {len(product.values())}")
print(f"No.of Items = {len(product)}")
# 3 . SORT DICT
def sort_dict(d):
    sorted_dict = dict(sorted(d.items()))
    return sorted_dict
d = {"C" : 30 , "A" : 10 , "B" : 20}
print(sort_dict(d))
# 4 . ADD KEY
# A ---> USING []
student = {"Name" : "Madan Kumar","Age" : 19}
print(student)
student["Gender"] = "Male"
print(student)
# B ---> USING UPDATE
student = {"Name" : "K.Madan Kumar" , "Age" : 19}
student.update({"Course" : "Python"})
print(student)
# 4 . MERGE DICT
# A ---> USING UPDATE
d1 = {"A" : 10 , "B" : 20}
d2 = {"C" : 30 , "D" : 40}
d1.update(d2)
print(d1)
# B ---> USING | OPERATOR
d1 = {"A" : 10 , "B" : 20}
d2 = {"C" : 30 , "D" : 40}
d3 = d1 | d2
print(d3)
# C ---> USING **
d1 = {"A" : 10 , "B" : 20}
d2 = {"C" : 30 , "D" : 40}
d3 = {**d1,**d2}
print(d3)
# 5 . CHECK IF KEY EXISTS
# A ---> USING IN
d1 = {"A" : 10 , "Name" : "Madan Kumar"}
if "A" in d1:
    print("Exists")
else:
    print("Does not exists")
# B ---> USING GET
d = {"A": 10, "B": 20, "C": 30}
if d.get("B") is not None:
    print("Key exists")
else:
    print("Key does not exist")
# 6 . ITERATE OVER A DICT USING LOOPS
# A ---> KEY , VALUE , ITEMS
d1 = {"Name" : "Madan Kumar",
      "Age"  :  19,
      "CGPA" : 8.9}
for i in d1:
    print(i)
for j in d1.values():
    print(j)
for i,j in d1.items():
    print(i,  ':', j)
# 7 . SQUARES
# A ---> 
d1 = {"1" : 1,
      "2" : 2,
      "3" : 3,
      "4" : 4}
for i,j in d1.items():
    print(i,":",j*j)
# B --->
n = int(input())
d = {}
for i in range(1,n+1):
    d[i] = i*i
print(d)
# C ---> DICT COMPREHENSION
n = int(input(''))
d = {x : x*x for x in range(1,n+1)}
print(d)
# 8 . SUM OF ALL ITEMS IN DICT
# A ---> USING SUM()
d1 = {"A" : 10,"B" : 20,"C" : 30}
total = sum(d1.values())
print(f"Sum = {total}")
# B ---> USING FOR LOOP
d1 = {"A" : 10,"B" : 120,"C" : 30}
sum = 0
for i in d1.values():
     sum+=i
print(f"Sum = {sum}")
# 8 . MULTIPLICATION OF ALL ITEMS IN DICT
# A ---> FOR LOOP
d1 = {"A" : 10,"B" : 120,"C" : 30}
prod = 1
for i in d1.values():
     prod*=i
print(f"Product = {prod}")
# B ---> USING math.prod
import math
d1 = {"A" : 10,"B" : 120,"C" : 30}
print(math.prod(d1.values()))
# 9 . REMOVE A KEY
# A ---> USING DEL
d1 = {"A" : 10 , "B" : 20 , "C" : 30}
del d1["C"]
print(d1)
# B ---> USING POP
d1 = {"A" : 10 , "B" : 20 , "C" : 30}
d1.pop("C")
print(d1)
# 10 . MAPING
keys = ["Red","Blue","Yellow"]
values = ["RCB","MI","CSK"]
dictionary = dict(zip(keys,values))
print(dictionary)
# 11 . SORT DICT BY KEY
d1 = {"Name" : "K.Madan Kumar",
      "Age"  : 19,
      "CDS"  : 1392}
sorted_dict = dict(sorted(d1.items()))
print(sorted_dict)
# 12 . MAX AND MIN IN DICT
# A ---> ONLY VALUE
student_marks = {
    "John": 85,
    "Alice": 92,
    "Bob": 78,
    "David": 88
}
max_value = max(student_marks.values())
min_value = min(student_marks.values())
print("Maximum value:", max_value)
print("Minimum value:", min_value)
# B ---> KEY AND VALUE
student_marks = {
    "John": 85,
    "Alice": 32,
    "Bob": 98,
    "David": 88
}
max_key = max(student_marks,key=student_marks.get)
min_key = min(student_marks,key=student_marks.get)
print("Maximum Item:", max_key,student_marks[max_key])
print("Minimum Item:", min_key,student_marks[min_key])
# 13 . REMOVE DUPLICATES
d = {"A" : 10,
     "B" : 20,
     "C" : 30,
     "D" : 40,
     "A" : 50,
     "E" : 20}
result = {}
for i,j in d.items():
    if j not in result.values():
        result[i] = j
print(result)
# 14 . 
# A --->
d = {}
if not d:
    print("Dictionary is Empty")
else:
    print("Dictionary is not empty")
# B ---> USING LEN()
d = {}
if len(d) == 0:
    print("Dictionary is Empty")
else:
    print("Dictionary is not empty")
# 15 . 
d1 = {"A" : 10 , "B" : 20 , "C" : 30}
d2 = {"A" : 30 , "B" : 20 , "C" : 10}
result = d1.copy()
for i,j in d2.items():
    if i in result:
        result[i]+=j
    else:
        result[i] = j
print(result)