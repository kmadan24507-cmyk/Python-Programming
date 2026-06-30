# TUPLE = A Tuple is a data structure that can store multiple elements in a single variable ----> IT IS IMMUTABLE
# Ex : 
t = (1,1,8,"Madan",True)
print(t)
t = tuple(map(int,input().split()))
print(t)
# IMMUTABLE
t = (1,2,3)
print(t[0])
print(t[1])
print(t[2])
# t[0] = 4
print(t)  # TypeError
# Alow Duplicates
t = (1,2,3,4,2,1)
print(t)
# Type
t = (10,)    # , is important
print(type(t))
# Slicing
t = (1,2,3,4,5,6)
print(t[1:])
print(t[2:])
print(t[-1])
print(t[1:3])
print(t[::-1])
print(t[::2])
# 
t = 1,2,3
print(t)
print(len(t))
# LOOP
t = (10,20,30)
for i in t:
    print(i)
# PROBLEMS
# 1 . CREATE TUPLE 
t = (1,1.5,1.55,"Madan",True)
print(t)
# 2 . FIND MAX AND MIN
# A ---> USING MAX AND MIN
t = (1,2,3,4,5)
print(f"Max Element = {max(t)}")
print(f"Min Element = {min(t)}")
# B ---> USING LOOP
t = (1,2,3,4,5)
maximum = t[0]
minimum = t[0]
for i in t:
    if i > maximum:
        maximum = i
for i in t:
    if i < minimum:
        minimum = i
print(f"Max Element = {maximum(t)}")
print(f"Min Element = {minimum(t)}")
# 3 . SUM OF ALL ELEMENTS IN A TUPLE
t = (1,2,3,4,5)
print(f"Sum of All Elements = {sum(t)}")
t = (1,2,3,4,5)
sum = 0
for i in t:
    sum+=i
print(sum)
# 4 . COUNT OCCURENCE OF AN ELEMENT
t = (1,2,3,1,3,4)
print(t.count(1))
print(t.count(2))
print(t.count(3))
print(t.count(4))
print(t.count(10))
# 5 . FIND INDEX
t = (1,2,3,4,5)
print(t.index(1))
print(t.index(2))
print(t.index(3))
print(t.index(4))
print(t.index(5))
# 6 . CHECK IF A ELEMENT EXITS
t = (1,2,3,4,5)
print(1 in t)
print(5 in t)
print(10 in t)
# 7 . CONVER TUPLE TO LIST AND LIST TO TUPLE
lst = [1,2,3,4,5]
t = tuple(lst)
print(t)
t = (1,2,3,4,5)
lst = list(t)
print(lst)
# 8 . COMBINE TWO TUPLES
t1 = (1,2,3)
t2 = (4,5,6)
result = t1+t2
print(result)
# 9 . SORTING
t1 = (4,1,2,5)
result1 = tuple(sorted(t1))
result2 = tuple(sorted(t1,reverse = True))
print(result1)
print(result2)
print(result1)
# 10 . SECOND LARGEST AND SMALLEST
t = (1,2,3,4,5)
result = tuple(sorted(t))
print(result[-2])
print(result[1])
# 11 . REMOVE DUPLICATES
t = (1,1,2,2,3,3,4)
result = tuple(set(t))
print(result)
# 12 . LOOP 
# A --->
t = (1,2,3,4)
for i in t:
    print(i)
# B ---> 
t = (1,2,3,4)
for i in range(len(t)):
    print(i,t[i])
# 13 . EVEN AND ODD NUMBERS
t = (1,2,3,4,5)
even = ()
odd = ()
even_count = 0
odd_count = 0
for i in t:
    if i % 2 == 0:
      even+=(i,)
      even_count+=1
    else:
        odd+=(i,)
        odd_count+=1
print(f"Even = {even} ")
print(f"Odd = {odd}")
print(f"No.of Evens = {even_count}")
print(f"No.of Odds = {odd_count}")
# 14 . DUPLICTAES
# A ---> FIND DUPLICATES
t = (1,2,1,3,2,4,5,6,5)
dup = []
for i in t:
    if t.count(i) > 1 and i not in dup:
        dup.append(i)
print(dup)
# B ---> REMOVE DUPLICATES
t = (1,2,2,1,3,4,1)
result = ()
for i in t:
    if i not in result:
        result+=(i,)
print(result)
# 15 . FIND MOST FREQUENT ELEMENT
# A ---> USING MAX
t = (1,2,1,1,2,3)
most_freq = max(t,key = t.count)
print(most_freq)
# B ---> USING LOOP
t = (1,2,3,1,1,5)
most = t[0]
count = t.count(most)
for i in t:
    if t.count(i) > count:
        most = i
        count = t.count(i)
print(most)
# 16 . SORT TUPLE IN ASCENDING AND DESCENDING ORDER
# A ---> ASCENDING
t = (3,5,1,2,4)
result = tuple(sorted(t))
print(result)
# B ---> DESCENDING
t = (3,4,1,2,3)
result = tuple(sorted(t,reverse=True))
print(result)
# 17 . FIND COMMON ELEMENTS
t1 = (1,2,3)
t2 = (3,4,5)
for i in t1:
    if i in t2:
        print(i)
# 18 . CONVERT TUPLE ----> STRING
# A ---> TUPLE ---> STRING
t = (1,2,3,"m")
result = ""
for i in t:
    result+=str(i)
print(result)
# B ---> STRING ---> TUPLE
s = "Madan kumar"
t = tuple(s)
print(t)
# C ---> JOIN 
t = ("M","A","D","A","N")
s = "".join(t)
print(s)
# 19 . SQUARES AND CUBES
# A ---> SQUARES
t = (1,2,3,4,5)
square = ()
for i in t:
    square+=(i*i,)
print(square)
# B ---> CUBES
t = (1,2,3,4,5)
cubes = ()
for i in t:
    cubes+=(i*i*i,)
print(cubes)
# 20 . 
s = "Madan Kumar"
s1 = tuple(s)
vowels = 0
consonants = 0
for i in s1:
    if i in "AEIOUaeiou":
        vowels+=1
    else:
        consonants+=1
print(f"No.of Vowels = {vowels}")
print(f"No.of Consonants = {consonants}")
# 21 . REVERSE A STRING
s = "Madan Kumar"
s1 = tuple(s)
rev = s1[::-1]
print(s1[::-1])
print("".join(rev))
# 22 . PALINDROME
s = "madam"
s1 = tuple(s)
if s1 == s1[::-1]:
    print("Palindrome")
else:
    print("Not A Palindrome")
# 23 . STAR PATTERN
t = (1,2,3,4,5)
for i in t:
    print("*"*i)
for j in t:
    for k in range(1,j+1):
        print(j,end = "")
    print()
# ------>  NESTED TUPLE  <------
# 24 . 
t = ((11,22),(1,4),(5,6))
print(t)
print(t[0][0])
print(t[0][1])
print(t[1][0])
print(t[1][1])
print(t[2][0])
print(t[2][1])
print(sorted(t))
for i in t:
    for j in i:
        print(j,end = "")
# 25 . SUM OF ALL ELEMENTS
t = ((10,20),(30,40),(50,60))
sum = 0
for i in t:
    for j in i:
        sum+=j
print(f"Sum Of All Elements = {sum}")
# 26 . LARGEST ELEMENT AND SMALLEST
# A ---> LARGEST
t = ((1,2),(3,4),(5,6))
largest = t[0][0]
for i in t:
    for j in i:
        if j > largest:
            largest = j
print(f"Largest Element = {largest}")
# B ---> SMALLEST
t = ((1,2),(3,4),(5,6))
smallest = t[0][0]
for i in t:
    for j in i:
        if j < smallest:
            smallest = j
print(f"Smallest Element = {smallest}")
# 27 . MATRIX AND SUM 
A = ((1,2),
     (3,4))
B = ((5,6),
     (7,8))
result = ()
for i in range(len(A)):
    row = ()
    for j in range(len(A[i])):
        row+=(A[i][j] + B[i][j],)
    result+=(row,)
print(result)
# 28 . SUM OF EACH ROW AND COLUMN IN A NESTED TUPLE
t = ((1,2,3),
     (4,5,6),
     (7,8,9))
for i in range(len(t[0])):
    total = 0
    for j in range(len(t)):
        total+=t[j][i]
    print(total)
# 29 . FIND LARGEST AND SMALLEST IN ROW
# A ---> LARGEST
t = ((1,2,3),
     (4,5,6),
     (7,8,9))
for i in t:
    print(max(i))
for j in t:
    print(min(j))
# 30 . DIAGONAL SUM
t = ((1,2,3),
     (4,5,6),
     (7,8,9))
total_1 = 0
for i in range(len(t)):
    total_1+=t[i][i]
total_2 = 0
for j in range(len(t)):
    total_2+=t[j][len(t)-1-j]
print(total_1)
print(total_2)
# 31 . CHECK SYMMETRIC
A = ((1,2,3),
     (4,5,6),
     (7,8,9))
symm = True
for i in range(len(A)):
    for j in range(len(A)):
        if A[i][j] != A[j][i]:
           symm = False
if symm:
    print("It Is A Symmetric")
else:
    print("It Is Not A Symmetric")
# 32 . COUNT ELEMENTS
A = ((1,2,3),
     (4,5,6),
     (7,8,9))
count = 0
for i in A:
    for j in i:
        count+=1
print(count)
# 33 . FIND MAXIMUM AND MINIMUM TUPLE IN ROW AND COLUMN
# A ---> ROW
A = ((1,2,3),
     (4,5,6),
     (7,8,9))
largest = A[0]
for i in A:
    if sum(i) > sum(largest):
        largest = i
smallest = A[0]
for i in A:
    if sum(i) < sum(smallest):
        smallest = i
print(f"Largest Row = {largest}")
print(f"Smallest Row = {smallest}")
# B ---> COLUMN
A = ((1,2,3),
     (4,5,6),
     (7,8,9))
column = list(zip(*A))
largest = column[0]
smallest = column[0]
for i in column:
    if sum(i) > sum(largest):
        largest = i
for j in column:
    if sum(j) < sum(smallest):
        smallest = j
print(f"Largest Column = {largest}")
print(f"Smallest Column = {smallest}")
#    -----> TUPLE COMPREHENSION <------
# 34 . PRINT NUMBERS,SQUARES,CUBES,EVEN,ODD
# A ---> NUMBERS
t = tuple(i for i in range(1,6))
print(t)
# B ---> SQUARES
t = tuple(i * i for i in range(1,6))
print(t)
# C ---> CUBES
t = tuple(i*i*i for i in range(1,6))
print(t)
# D ---> EVEN
t = tuple(i for i in range(1,6) if i % 2 == 0)
print(t)
# E ---> ODD
t = tuple(i for i in range(1,6) if i % 2 != 0)
print(t)
# 35 . SWAPPING
a = 10
b = 30
temp = a
a = b
b = temp
print(a,b)
# 36 . ZIP TWO TUPLES
t1 = (1,2,3,4)
t2 = ("A","B","C","D")
result = tuple(zip(t1,t2))
print(result)
t = ((1, 'A'), (2, 'B'), (3, 'C'))
a,b = zip(*t)
print(a)
print(b)
# 37 . FING 2ND LARGEST AND SMALLEST
# A ---> USING MAX AND MIN
t = (1,2,3,4,5)
temp = sorted(t)
print(f"First Largest = {max(t)}")
print(f"First Smallest = {min(t)}")
print(f"Second largest = {temp[-2]}")
print(f"Second Smallest = {temp[1]}")
# B ---> USING LOOP
t = (1,2,3,4,5)
largest = t[0]
smallest = t[0]
second_largest = t[1]
second_smallest = t[1]
for i in t:
    if i > largest:
        second_largest = largest
        largest = i
    elif largest > i  > second_largest:
        second_largest = i
for i in t:
    if i < smallest:
        second_smallest = smallest
        smallest = i
    elif smallest < i < second_smallest:
        second_smallest = i
print(f"First Largest = {largest}")
print(f"First Smallest = {smallest}")
print(f"Second largest = {second_largest}")
print(f"Second Smallest = {second_smallest}")
# 38 . FIND PAIR WITH GIVEN SUM
t = (1,2,3,4,5)
target = 5
for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[i] + t[j] == target:
            print(t[i],t[j])
# 39 . SET BASED PROBLEMS OF TWO TUPLES
# A ---> UNION
t1 = (1,2,3)
t2 = (3,4,5)
print(set(t1) | set(t2))
# B ---> INTERSECTION
t1 = (1,2,3)
t2 = (3,4,5)
print(set(t1) & set(t2))
# C ---> DIFFERENCE
t1 = (1,2,3)
t2 = (3,4,5)
print(set(t1) - set(t2))
# 40 . LONGEST AND SHORTEST TUPLE
t = (
    (1,),
    (1, 2, 3, 4),
    (1, 2, 3)
)
largest = t[0]
shortest = t[0]
for i in t:
    if len(i) > len(largest):
        largest = i
for j in t:
    if len(j) < len(shortest):
        shortest = j
print(largest)
print(shortest)