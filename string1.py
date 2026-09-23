
#1. Write a Python program to input a string and display it in uppercase and lowercase.

s=input("enter your string:")
print(s.upper())
print(s.lower())

#__________________________________________________________________________________

#2.Write a Python program to find the length of a string without using len().

s = "Tasmiya"
count = 0
for x in s:
    count += 1
print(count)   

#__________________________________________________________________________________

# 3.Write a Python program to count the number of vowels and consonants in a given string.
s = "Tasmiya"
vowels = 0
consonants = 0
for i in s:
    if i in "aeiou":
      vowels = vowels + 1
    else :  
      consonants = consonants + 1
print("vowles:",vowels)     
print("consonants:",consonants)   

#__________________________________________________________________________________

# 4.Write a Python program to count uppercase letters, lowercase letters, digits, and special characters in a
# string.

s = "T@$miYa0717"
uppercase = 0
lowercase = 0
digit = 0
special = 0

for i in s:
    if i.isupper():
        uppercase = uppercase + 1
    elif i.islower():
        lowercase = lowercase + 1
    elif i.isdigit():
        digit = digit + 1
    else:
        special = special + 1
print("Uppercase letters:",uppercase)  
print("Lowercase letters:",lowercase)  
print("Digits:",digit)
print("special characters:",special) 

#__________________________________________________________________________________
#5.Write a Python program to check whether a given string is a palindrome.

s = "madam"
if s == s[::-1]:
    print("palindrome")
else:
    print("Not palindrome")  


#__________________________________________________________________________________
#6.Write a Python program to reverse a string without using slicing.

s = "Tasmiya"
rev = ""
for i in s:
    rev = i + rev
print("Reverse:",rev)   


#__________________________________________________________________________________
# 7.Write a Python program to remove all spaces from a given string

#using built-in func

s = "ta s mi ya"
s = s.replace(" ","")
print(s)

# 2nd
s = "ta s mi ya"
new = ""
for i in s:
    if i != " ":
        new = new + i
print("string without spaces:",new)  

#__________________________________________________________________________________

# 8.Write a Python program to count the frequency of a given character in a string.

s = input(" enter a string:")

for i in s:
    count = 0
    for j in s:
        if i == j:
            count = count + 1
    print(i, "=", count)  

#__________________________________________________________________________________
#9.Write a Python program to find the first occurrence and last occurrence of a character in a string.

s = input("Enter a string:")
ch = input ("Enter a character: ")

first = -1
last = -1

for i in range(len(s)):
    if s[i] == ch:
        if first == -1:
            first = i
        last = i

print("First Occurence:", first)  
print("Last Occurence:",last)

# 2nd method

# using built-in func
s = input("Enter a string:")
ch = input ("Enter a character: ")   

first = s.find(ch)
last = s.rfind(ch)

print("First Occurence:", first)  
print("Last Occurence:",last)

#__________________________________________________________________________________

#10. Write a Python program to replace all occurrences of a specified word in a sentence with another word

# USING BUILT-IN FUNC
sentence = input("Enter a sentence:")
old = input("Enter old word to be replace:")
new = input("enter new word:")

sentence = sentence.replace(old, new)

print("New_sentence:", sentence)

# 2nd method

sentence = input("Enter a sentence: ")
old = input("Enter word to replace: ")
new = input("Enter new word: ")

words = sentence.split()
result = ""

for word in words:
    if word == old:
        result = result + new + " "
    else:
        result = result + word + " "

print("New sentence:", result)

#__________________________________________________________________________________

#11. Write a Python program to check whether two strings are anagrams of each other.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Not Anagrams")
else:
    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            print("Not Anagrams")
    else:
        print("Anagrams")  

#__________________________________________________________________________________

#12.Write a Python program to find the most frequently occurring character in a string.

s = input("Enter a string: ")

max_count = 0
max_char = ""

for ch in s:
    count = s.count(ch)

    if count > max_count:
        max_count = count
        max_char = ch

print("Most frequent character:", max_char)
print("Frequency:", max_count)
#__________________________________________________________________________________
#13.Write a Python program to remove duplicate characters from a string while preserving the original order.

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result = result + ch

print("String after removing duplicates:", result)

#__________________________________________________________________________________

#14. Write a Python program to count the number of words in a sentence.

sentence = input("Enter a sentence: ")

words = sentence.split()

count = 0

for word in words:
    count = count + 1

print("Number of words:", count)

#__________________________________________________________________________________

#15. Write a Python program to find the longest word in a sentence.

sentence = input("Enter a sentence: ")

words = sentence.split()
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)        

#__________________________________________________________________________________

#16. Write a Python program to capitalize the first letter of every word in a sentence without using title()

sentence = input("Enter a sentence: ")

words = sentence.split()
result = ""

for word in words:
    result = result + word[0].upper() + word[1:] + " "

print("Result:", result)

#__________________________________________________________________________________





