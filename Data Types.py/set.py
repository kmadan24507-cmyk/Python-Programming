# SET ----> Unordered collection of unique elements
# It Is Mutable(can add/remove)
# Ex : 
s = {1,2,3,4,5}
print(s)
s = frozenset([1,2,3])
print(s)
# PROBLEMS ---> 
s = {1,2.9,"Madan"}  # boolean didn't take
# 1 . 
print(s)
# A . 
s1 = set()
print(type(s1))
print(s1)
# B . LENGTH
print(len(s))
# C ---> LOOP
for i in s:
    print(i)
# D ---> ADD
s.add(10)
print(s)
s.update([1,2,3])
print(s)
# E ---> REMOVE
s.remove(2.9)
print(s)
s.discard(10)
print(s)
value = s.pop()
print("Removed : ",value)
print(s)
# s.clear()
print(s)
s.difference_update(2,4)
print(s)
# F ---> COPY
s2 = s.copy()
print(s2)

# 2 . FIND MAXIMUM AND MINIMUM
# A ---> USING MAX AND MIN
s = {1,2,3,4,5}
print(max(s))
print(min(s))
# B ---> USING LOOP
s = {1,2,3,4,5}
first = next(iter(s))
maximum = first
minimum = first
for i in s:
    if i > maximum:
        maximum = i
for j in s:
    if j < minimum:
        minimum = j
print(maximum)
print(minimum)
# 3 . SUM
# A ---> USING SUM
s = {1,2,3,4,5}
print(sum(s))
# B ---> USING LOOP
s = {1,2,3,4,5}
sum = 0
for i in s:
    sum+=i
print(sum)
# 4 . PRODUCT
# ---> USING LOOP
s = {1,2,3,4,5}
prod = 1
for i in s:
    prod*=i
print(prod)
# 5 . UNION,INTERSECTION AND DIFFERENCE
# A ---> USING OPERATORS
s1 = {1,2,3}
s2 = {3,4,5}
print(f"Union = {s1 | s2}")
s1 = {1,2,3}
s2 = {3,4,5}
print(f"Intersection = {s1 & s2}")
s1 = {1,2,3}
s2 = {3,4,5}
print(f"Difference = {s1 - s2}")
# B ---> USING METHOD
s1 = {1,2,3}
s2 = {3,4,5}
print(s1.union(s2))
s1 = {1,2,3}
s2 = {3,4,5}
print(s1.intersection(s2))
s1 = {1,2,3}
s2 = {3,4,5}
print(s1.difference(s2))
# 6 . APPLICATIONS OF SETS
# A ---> CHECK SUBSET
s1 = {1,2}
s2 = {1,2,3}
print(s1.issubset(s2))
print(s2.issubset(s1))
# B ---> SUPERSET
s1 = {1,2,3}
s2 = {1,2}
print(s1.issuperset(s2))
print(s2.issuperset(s1))
# C ---> DISJOINT SETS
s1 = {1,2}
s2 = {3,4}
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s1))
# 7 . COUNT VOWELS IN A STRING
s = "Madan Kumar"
vowels = {"a","e","i","o","u","A","E","I","O","U"}
vowels_count = 0
consonants_count = 0
for i in s:
    if i in vowels:
        vowels_count+=1           # if i not in vowels
    else:
        consonants_count+=1
print(vowels_count)
print(consonants_count)
# 8 . EVEN AND ODD
# A ---> EVEN,ODD AND COUNT
s = {1,2,3,4,5}
even = set()
odd = set()
even_count = 0
odd_count = 0
for i in s:
    if i % 2 == 0:
        even.add(i)
        even_count+=1
    else:
        odd.add(i)
        odd_count+=1
print(f"Even = {even}")
print(f"Odd = {odd}")
print(f"No.of Evens = {even_count}")
print(f"No.of Odds = {odd_count}")
# B ---> FIND LARGEST AND SMALLEST EVEN AND ODD NUMBER
largest_even = next(iter(even))
smallest_even = next(iter(even))
largest_odd = next(iter(odd))
smallest_odd = next(iter(odd))
for i in s:
    if i % 2 == 0 and i > largest_even:
        largest_even = i
for j in s:
    if i % 2 == 0 and i < smallest_even:
        smallest_even = j
for k in s:
    if k % 2 != 0 and k > largest_odd:
        largest_odd = j
for l in s:
    if l % 2 != 0 and l < smallest_odd:
        smallest_odd = l
print(largest_even)
print(largest_odd)
print(smallest_even)
print(smallest_odd)
# 9 . SQUARES AND CUBES
# A ---> SQUARES
s = set()
for i in range(1,6):
    s.add(i*i)
print(s)
s = {1,2,3,4,5}
squares = set()
for i in s:
    squares.add(i*i)
print(squares)
# B ---> CUBES
s = set()
for i in range(1,6):
    s.add(i*i*i)
print(s)
s = {1,2,3,4,5}
cubes = set()
for i in s:
    cubes.add(i*i*i)
print(cubes)
#  -------> SET COMPREHENSIONS <-------
# 10 . 
# A ---> NUMBERS
s = {i for i in range(1,6)}
print(s)
# B ---> EVEN NUMBERS
s = {i for i in range(1,6) if i % 2 == 0}
print(s)
# C ---> ODD NUMBERS
s = {i for i in range(1,6) if i % 2 != 0}
print(s)
# D ---> SQUARES
s = {i**2 for i in range(1,6)}
print(s)
# E ---> CUBES
s = {i**3 for i in range(1,6)}
print(s)
# 11 . 
lst = [1,2,3,4,4,3]
for i in set(lst):
    print(i,lst.count(i))
# 12 . FIND MOST FREQUENT AND LOWEST ELEMENT
# A ---> MOST
lst = [1,2,2,2,3,4,1,2,4]
most = lst[0]
count = 0
for i in set(lst):
    if lst.count(i) > count:
        count = lst.count(i)
        most = i
print(most)
# B ---> LEAST
lst = [1,2,2,2,3,4,1,2,4]
least = lst[0]
count = len(lst)
for i in set(lst):
    if lst.count(i) < count:
        count = lst.count(i)
        least = i
print(least)
# 13 . 
s = {1,2,3,4,5}
target = 6
for i in s:
    for j in s:
        if i < j and i + j == target:
            print(i,j)
# 14 . FIND GCD,LCM
# A ---> GCD
a = 24
b = 36
s1 = set()
s2 = set()
for i in range(1,a+1):
    if a % i == 0:
        s1.add(i)
for j in range(1,b+1):
    if b % j == 0:
        s2.add(j)
print(max(s1 & s2))
# B ---> LCM
a = 12
b = 18
s1 = set()
s2 = set()
for i in range(1,50):
    s1.add(a*i)
    s2.add(b*i)
print(min(s1 & s2))
# 15 . PRIME NUMBERS
s = {1,2,3,4,5,6,7,8,9,10}
primes = set()
for i in s:
    if i > 1:
        for j in range(2,i):
            if i % j == 0 or i == 9:
                break
            else:
                primes.add(i)
print(primes)
n = 20
primes = set()
for i in range(1,n+1):
    if i > 1:
        for j in range(2,i):
            if i % j == 0 or i == 9:
                break
            else:
                primes.add(i)
print(primes)
# 16 . FIND FACTORS
n = int(input("Enter a number : "))
factors = set()
for i in range(1,n+1):
    if n % i == 0:
        factors.add(i)
print(factors)
# 17 . PERFECT,ARMSTRONG NUMBERS
# A ---> PERFECT
n = 28
factors = set()
for i in range(1,n):
    if n % i == 0:
        factors.add(i)
print(sum(factors) == n)
# B ---> ARMSTRONG
n = 153
digits = set(str(n))
print(digits)
# 18 . FIND MAXIMUM PRODUCT AND NUMBERS
s = set(list(map(int,input().split())))
lst = list(s)
maximum = lst[0] * lst[1]
num1 = lst[0]
num2 = lst[1]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] * lst[j] > maximum:
            maximum = lst[i] * lst[j]
            num1 = lst[i]
            num2 = lst[j]
print(f"Numbers = {num1},{num2}")
print(f"Max product = {maximum}")
# 19 . ANAGRAMS
words = input("").split()
d = {}
for i in words:
    key = str(sorted(i))
    if key in d:
        d[key].append(i)
    else:
        d[key] = [i]
for j in d.values():
    print(j)