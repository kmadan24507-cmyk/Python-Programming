# LIST ---> IT IS MUTABLE
names = ["Madan","Dilip","Ravi","Suresh"]
print(names)
print(names[0])
print(names[1])
print(names[0:2])
print(names[::-1])
print(names[::2])
print(names[1:4:2])
print(names[1:])
names[0] = "Madhan"
print(names)
names.append("Kumar")
print(names)
names.insert(1,"Kumar")
print(names)
names.remove("Kumar")
print(names)
names.pop()
print(names)
names.pop(1)
print(names)
names.clear()
print(names)
print(len(names))
print(names.count("Madan"))
print("Madan" in names)
for i in names:
    print(i)
name = ["hbsb","ugugu","mada"]         #  LIST IS MUTABLE
name[0] = "madan"
print(name)
# List Comprehension
numbers = [1,2,3,4,5]
squared = [x**2 for x in numbers]
print(squared)
# Nested List
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
# JOIN METHOD
s = ['a','b','c','d']
str1 = ''.join(s)
print(str1)
# PROBLEMS
# 1 . SUM OF A NUMBERS
# A ---> FOR LOOP
def sum(lst):
    sum = 0
    for i in lst:
       sum+=i
    return sum
lst = list(map(int,input("Enter The Numbers : ").split()))
print(f"The Sum of Elements In The List = {sum(lst)}")
# B ---> WHILE LOOP
def sum(lst):
    sum = 0
    i = 0
    while i < len(lst):
        sum+=lst[i]
        i+=1
    return sum
lst = list(map(int,input("Enter The Numbers : ").split()))
print(f"The Sum of Elements In The List = {sum(lst)}")
# 2 . MULTIPLY ITEMS IN LIST
# A ---> FOR LOOP
def mul(lst):
    product = 1
    for i in lst:
        product*=i
    return product
lst = list(map(int,input("Enter The Numbers In The List : ").split()))
print(f"The Product Of Numbers In The List = {mul(lst)}")
# B ---> WHILE LOOP
def mul(lst):
    product = 1
    i = 0
    while i < len(lst):          # if we take i = len(lst) - 1 we take i-=1 and if i = 0 then i+=1
        product*=lst[i]
        i+=1
    return product
lst = list(map(int,input("Enter The Numbers In The List : ").split()))
print(f"The Product Of Numbers In The List = {mul(lst)}")
# 3 . LARGEST NUMBER
# A --->  FOR LOOP
def largest(lst):
    largest = lst[0]
    for i in lst:
        if i > largest:
            largest = i
    return largest
lst = list(map(int,input("Enter the numbers : ").split()))
print(f"The Largest Number In The List = {largest(lst)}")
# B ---> WHILE LOOP
def largest(lst):
    largest = lst[0]
    i = 0
    while i < len(lst):
        if lst[i] > largest:
            largest = lst[i]
        i+=1
    return largest
lst = list(map(int,input("Enter the numbers : ").split()))
print(f"The Largest Number In The List = {largest(lst)}")
# 4 . SMALLEST NUMBER
# A --->  FOR LOOP
def smallest(lst):
    smallest = lst[0]
    for i in lst:
        if i < smallest:
            smallest = i
    return smallest
lst = list(map(int,input("Enter the numbers : ").split()))
print(f"The Smallest Number In The List = {smallest(lst)}")
# B ---> WHILE LOOP
def smallest(lst):
    smallest = lst[0]
    i = 0
    while i < len(lst):
        if lst[i] < smallest:
            smallest = lst[i]
        i+=1
    return smallest
lst = list(map(int,input("Enter the numbers : ").split()))
print(f"The Smallest Number In The List = {smallest(lst)}")
# 5 . REMOVE DUPLICATES FROM LIST
# A ---> FOR LOOP
def remove_duplicates(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list
lst = list(map(int,input("Enter the numbers : ").split()))
print(f"After Removing Duplicates = {remove_duplicates(lst)}")
# B ---> WHILE LOOP
def remove_duplicates(lst):
    new_list = []
    i = 0
    while i < len(lst):
        if lst[i] not in new_list:
            new_list.append(lst[i])
        i+=1
    return new_list
lst = list(map(int,input("Enter the numbers : ").split()))
print(f"After Removing Duplicates = {remove_duplicates(lst)}")
# 6 . 
# A ---> FOR LOOP
def long_word(n,str):
    word_len = []
    text = str.split()
    for i in text:
        if len(i) > n:
            word_len.append(i)
    return word_len
print(long_word(3,"The Quick Brown Fox"))
# B ---> WHILE LOOP
def long_word(n,s):
    word_len = []
    text = s.split()
    i = 0
    while i < len(text):
        if len(text[i]) > n:
            word_len.append(text[i])
        i+=1
    return word_len
print(long_word(3,"The Quick Brown Fox"))
# 7 . COMMON ELEMENTS IN TWO LISTS
# A ---> FOR LOOP
def common_elements(lst1,lst2):
    new_list = []
    for i in lst1:
        for j in lst2:
            if i == j:
                new_list.append(i)
    return new_list
lst1 = list(map(int,input("Enter the numbers : ").split()))
lst2= list(map(int,input("Enter the numbers : ").split()))
print(f"Common Elements In Two Lists = {common_elements(lst1,lst2)}")
# B ---> WHILE LOOP
def common_elements(lst1,lst2):
    new_list = []
    i = 0
    while i < len(lst1):
        j = 0
        while j < len(lst2):
            if lst1[i] == lst2[j]:
                new_list.append(lst1[i])
                break
            j+=1
        i+=1
    return new_list
lst1 = list(map(int,input("Enter the numbers : ").split()))
lst2= list(map(int,input("Enter the numbers : ").split()))
print(f"Common Elements In Two Lists = {common_elements(lst1,lst2)}")
# 8 . 
# A ---> FOR LOOP
def remove(new_list):
    new_list = [x for (i,x) in enumerate(new_list) if i not in (0,4,5)]
    return new_list
print(remove(["Red","Green","White","Black","Pink","Yellow"]))
# 9 . EVEN AND ODD
# A ---> FOR LOOP
def even_odd(lst):
    even = []
    odd = []
    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return print(f"Even =  {even}\nOdd = {odd}")
even_odd([1,2,3,4,5])
# B ---> WHILE LOOP
def even_odd(lst):
    even = []
    odd = []
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            even.append(lst[i])
        else:
            odd.append(lst[i])
        i+=1
    return print(f"Even =  {even}\nOdd = {odd}")
even_odd([1,2,3,4,5])
# LIST COMPREHENSION
def even_odd(lst):
    even = [i for i in lst if i % 2 == 0]
    odd = [i for i in lst if i % 2 != 0]
    return print(f"Even =  {even}\nOdd = {odd}")
even_odd([1,2,3,4,5])  
# 10 . SQUARED AND CUBID OF NUMBERS
# A ---> FOR LOOP
def square_cube():
    square = []
    cube = []
    for i in range(1,11):
        square.append(i**2)
        cube.append(i**3)
    return print(f"Squares = {square}\nCubid = {cube}")
square_cube()
# B ---> WHILE LOOP
def square_cube():
    square = []
    cube = []
    i = 0
    while i < 10:
        square.append(i**2)
        cube.append(i**3)
        i+=1
    return print(f"Squares = {square}\nCubid = {cube}")
square_cube()
# LIST COMPREHENSION
def square_cube():
    squares = [i**2 for i in range(1,11)]
    cubid = [i**3 for i in range(1,11)]
    return print(f"Squares = {squares}\nCubid = {cubid}")
square_cube()
# 11 . SECOND LARGEST NUMBER IN THE LIST
# A ---> FOR LOOP
def second_largest(lst):
    largest = lst[0]
    second_largest = lst[0]
    for i in lst:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i!=largest:
            second_largest = i
    return print(f"Largest Number = {largest}\nSecond Largest = {second_largest}")
lst = list(map(int,input("Enter The Numbers In The List : ").split()))
second_largest(lst)
# B ---> WHILE LOOP
def second_largest(lst):
    largest = lst[0]
    second_largest = lst[0]
    i = 0
    while i < len(lst):
        if lst[i] > largest:
            second_largest = largest
            largest = lst[i]
        elif lst[i] > second_largest and lst[i]!=largest:
            second_largest = lst[i]
        i+=1
    return print(f"Largest Number = {largest}\nSecond Largest = {second_largest}")
lst = list(map(int,input("Enter The Numbers In The List : ").split()))
second_largest(lst)
# 12 . SECOND SMALLEST NUMBER IN THE LIST
# A ---> FOR LOOP
def second_smallest(lst):
    smallest = lst[0]
    second_smallest = lst[0]
    for i in lst:
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif i < second_smallest and i!=smallest:
            second_smallest = i
    return print(f"Smallest Number = {smallest}\nSecond Smallest = {second_smallest}")
lst = list(map(int,input("Enter The Numbers In The List : ").split()))
second_smallest(lst)
# B ---> WHILE LOOP
def second_smallest(lst):
    smallest = lst[0]
    second_smallest = lst[0]
    i = 0
    while i < len(lst):
        if lst[i] < smallest:
            second_smallest = smallest
            smallest = lst[i]
        elif lst[i] < second_smallest and lst[i]!=smallest:
            second_smallest = lst[i]
        i+=1
    return print(f"Smallest Number = {smallest}\nSecond Smallest = {second_smallest}")
lst = list(map(int,input("Enter The Numbers In The List : ").split()))
second_smallest(lst)
# 13 . COUNT FREQUENCY OF ELEMENTS
# A ---> FOR LOOP
def count_freq(lst):
    new_list = []
    count = 0
    for i in lst:
        if i not in new_list:
            count = 0
            for j in lst:
              if i == j:
                count+=1
            print(i," : ",count)
            new_list.append(i)
lst = list(map(int,input("").split()))
count_freq(lst)
# B ---> WHILE LOOP
def count_freq(lst):
   new_list = []
   count = 0
   i = 0
   while i < len(lst):
      if lst[i] not in new_list:
        count = 0
        j = 0
        while j < len(lst):
            if lst[i] == lst[j]:
               count+=1
            j+=1
        print(lst[i]," : ",count)
        new_list.append(lst[i])
      i+=1
lst = list(map(int,input("").split()))
count_freq(lst)
# 14 . MOVE ZEROS TO END OF LIST
# A ---> FOR LOOP
def move_zeros(lst):
    new_list = []
    for i in lst:
        if i!=0:
            new_list.append(i)
    for i in lst:
        if i == 0:
            new_list.append(i)
    return new_list
lst = list(map(int,input("Enter the numbers : ").split()))
print(move_zeros(lst))
# B ---> WHILE LOOP
def move_zeros(lst):
    new_list = []
    i = 0
    while i < len(lst):
        if lst[i]!=0:
            new_list.append(lst[i])
        i+=1
    i = 0
    while i < len(lst):
        if lst[i] == 0:
            new_list.append(lst[i])
        i+=1
    return new_list
lst = list(map(int,input("Enter the numbers : ").split()))
print(move_zeros(lst))
# 15 . SORTING IN ASCENDING AND DESCENDING
# A ---> ASCENDING
lst = [7,6,3,2,1,5,4]
print(sorted(lst))
# B ---> DESCENDING
lst = [7,6,3,2,1,5,4]
lst.sort(reverse=True)
print(lst)
# 16 . 
# A ---> 
a = [1,2,3,4,5]
max_sum = a[0] + a[1]
num1 = a[0]
num2 = a[1]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] + a[j] > max_sum:
            max_sum = a[i] + a[j]
            num1 = a[i]
            num2 = a[j]
print(f"Numbers = {num1},{num2}")
print(f"Max Sum = {max_sum}")
# B ---> 
a = [1,2,3,4,5]
max_prod = a[0] * a[1]
num1 = a[0]
num2 = a[1]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] * a[j] > max_prod:
            max_prod = a[i] * a[j]
            num1 = a[i]
            num2 = a[j]
print(f"Numbers = {num1},{num2}")
print(f"Max Sum = {max_prod}")