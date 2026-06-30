# File ---> A File is a collection of data stored in a device.
# PROBLEMS
# 1 ---> CREATE A TEXT FILE
with open("1.txt","w") as f:
    pass
file = open("1,txt","w")
file.close()
# 2 ---> WRITE TEXT TO A FILE
# with open("1.txt","w") as f:
#     f.write("Hello, I am Madan Kumar")
file = open("1.txt","w")
file.write("Hi I Am Madan Kumar\n")
file.write("I Am Learning Python\n")
file.write("I Am learning File handling")
file.close()
# 3 ---> READ THE ENTIRE FILE
with open("1.txt","r") as f:
    data = f.read()
print(data)
file = open("1.txt","r")
data = file.read()
file.close()
print(data)
# 4 ---> READ THE FIRST LINE
with open("1.txt","r") as f:
    first_line = f.readline()
print(first_line)
# 5 ---> READ ALL LINES
with open("1.txt","r") as f:
    lines = f.readlines()
print(lines)
# 6 ---> APPEND TEXT TO A FILE
with open("1.txt","a") as f:
    f.write("\nThis is Appended text")
# 7 ---> COUNT CHARACTERS
with open("1.txt","r") as f:
    data = f.read()
print(data)
print(f"No.of Characters = {len(data)}")
# 8 ---> COUNT WORDS
with open("1.txt","r") as f:
    data = f.read()
words = data.split()
print(f"No.of Words = {len(words)}")
# 9 ---> COUNT LINES
with open("1.txt","r") as f:
    data = f.readlines()
print(f"No.of Lines = {len(data)}")
# 10 ---> READ THE FILE LINE BY LINE
with open("1.txt","r") as f:
    for i in f:
        print(i.strip())
# 11 ---> DISPLAY ALL LINES ONE BY ONE
with open("1.txt","r") as f:
    lines = f.readlines()
print(lines[0])
print(lines[1])
print(lines[-1])
# 12 ---> DISPLAY THE FIRST THREE LINES
with open("1.txt","r") as f:
    data = f.readlines()
for i in data[:3]:
    print(i.strip())
# 13 ---> COPYING
with open("1.txt","r") as f:
    data = f.read()
with open("copy.txt","w") as f1:
    f1.write(data)
# 14 ---> WRITE
lines = ["Python\n", "Java\n", "C++"]
with open("1.txt","w") as f:
    f.writelines(lines)
with open("1.txt","w") as f:
    f.write("New Content\n")
    f.write("12345")
# 15 ---> CHECK WHETHER FILE IS EMPTY
with open("1.txt","r") as f:
    data = f.read()
if data == " ":
    print("File Is Empty")
else:
    print("File Is Not Empty")
# 16 ---> FILE SIZE
import os
print(os.path.getsize("1.txt"),"bytes")
# 17 ---> READ ONLY FIRST 5 CHARACTERS
with open("1.txt","r") as f:
    data = f.read(5)
print(data)
# 18 ---> COUNT VOWELS AND CONSONANTS
with open("1.txt","r") as f:
    data = f.read()
vowel_count = 0
consonant_count = 0
for i in data:
    if i in "aeiouAEIOU":
        vowel_count+=1
    else:
        consonant_count+=1
print(f"No.of Vowels = {vowel_count}")
print(f"No.of Consonants = {consonant_count}")
# 19 ---> FIND VOWELS AND CONSONANTS
with open("1.txt","r") as f:
    data = f.read()
for i in data:
    if i in "aeiouAEIOU":
        print(f"Vowels = {i}")
    else:
        print(f"Consonants = {i}")
# 20 ---> COUNT DIGITS
with open("1.txt","r") as f:
    data = f.read()
count = 0
for i in data:
    if i.isdigit():
        count+=1
print(f"No.of digits = {count}")
# 21 ---> COUNT UPPERCASE AND LOWERCASE
with open("1.txt","r") as f:
    data = f.read()
upper_count = 0
lower_count = 0
for i in data:
    if i.isupper():
        upper_count+=1
    elif i.islower():
        lower_count+=1
print(f"No.of UpperCase Letters = {upper_count}")
print(f"No.of LowerCase Letters = {lower_count}")
# 22 ---> FIND LONGEST LINES
with open("1.txt","r") as f:
    data = f.readlines()
print(max(data,key=len))
# 23 ---> FIND SHORTEST LINES
with open("1.txt","r") as f:
    data = f.readlines()
print(min(data,key=len))
# 24 ---> REVERSE CONTENT IN A FILE
with open("1.txt","r") as f:
    data = f.read()
print(data[::-1])
# 25 ---> REVERSE EACH LINE
with open("1.txt" ,"r") as f:
    for i in f:
        print(i[::-1])
# 26 ---> CONVERT MATTER INTO UPPERCASE AND LOWERCASE
with open("1.txt","r") as f:
      data = f.read()
print(f"Uppercase = {data.upper()}")
print(f"Lowercase = {data.lower()}")
print(f"Swapcase = {data.swapcase()}")