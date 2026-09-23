#1.  Write a Python program to find the length of a string.

s = input("Enter a string:")

length = len(s)

print("Length:",length)

#______________________________________________________________

#2.  Write a Python program to count vowels and consonants in a string.

s = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1

        else:
            consonants += 1

print("Vowels: ",vowels)            
print("Consonants:",consonants)

#______________________________________________________________

#3.  Write a Python program to check whether a string is a palindrome or not

s = input("Enter a string: ")

if s ==s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")    

#______________________________________________________________

#4.  Write a Python program to convert a string to uppercase and lowercase.

s = input("Enter a string:")

print("Uppercase:",s.upper())
print("LOwercase:",s.lower())

#______________________________________________________________

#5.  Write a Python program to count the number of words in a sentence.

s = input("Enter a sentence: ")

words = s.split()

print("Word count:",len(words))

#______________________________________________________________

# 6.  Write a Python program to reverse a given string.

s = input("Enter a string:")

reverse = s[::-1]

print("reversed string:",reverse)

#______________________________________________________________

# 7.  Write a Python program to check whether two strings are anagrams
s1 =input("Enter First String:")
s2 =input("Enter second String:")

if sorted(s1) == sorted(s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")    

#______________________________________________________________

# 8.  Write a Python program to remove all spaces from a string.
s = input("Enter a string")

result = s.replace(" ","")

print(result)
#______________________________________________________________

# 9.  Write a Python program to replace a word in a string with another word.
s = input("Enter a sentence: ")
old = input("Enter word to replace: ")
new = input("Enter new word: ")

result = s.replace(old, new)

print(result)

#______________________________________________________________

# 10.  Write a Python program to find the frequency of each character in a string

s = input("Enter a string: ")

for ch in s:
    if s.index(ch) == s.find(ch):
        print(ch, ":", s.count(ch))


#2nd Method

s = input("Enter a string: ")

frequency = {}

for ch in s:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

for ch in frequency:
    print(ch, ":", frequency[ch])

#______________________________________________________________

# 11.  Write a Python program to extract digits from a string.
s = input("Enter a string: ")

digits = ""

for ch in s:
    if ch.isdigit():
        digits += ch

print("Digits =", digits)

#______________________________________________________________


# 12.  Write a Python program to check whether a string starts and ends with a given substring
s = input("Enter string: ")
start = input("Enter starting substring: ")
end = input("Enter ending substring: ")

print("Starts with", start, "=", s.startswith(start))
print("Ends with", end, "=", s.endswith(end))
#______________________________________________________________

# 13.  Write a Python program to split a sentence into words and join them using a hyphen
s = input("Enter a sentence: ")

words = s.split()

result = "-".join(words)

print(result)
#______________________________________________________________

# 14.  Write a Python program to find the first non-repeating character in a string.
s = input("Enter a string: ")

for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating character =", ch)
        break
#______________________________________________________________

# 15.  Write a Python program to remove duplicate characters from a string while preserving order
s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch

print("Unique characters =", result)

#______________________________________________________________

# 16.  Write a Python program to count uppercase letters, lowercase letters, digits, and special characters in a
# string.
s = input("Enter a string: ")

uppercase = 0
lowercase = 0
digits = 0
special = 0

for ch in s:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Uppercase =", uppercase)
print("Lowercase =", lowercase)
print("Digits =", digits)
print("Special =", special)

#______________________________________________________________

# 1.  Write a Python program to count the frequency of each word in a sentence, ignoring letter case.
s = input("Enter a sentence: ")

words = s.lower().split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

for word in frequency:
    print(word, ":", frequency[word])

#______________________________________________________________

# 2.  Write a Python program to find the longest word in a sentence.
s = input("Enter a sentence: ")

words = s.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word =", longest)
print("Length =", len(longest))

#______________________________________________________________

# 3.  Write a Python program to remove punctuation marks from a string.

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch.isalnum() or ch == " ":
        result += ch

print(result)

#______________________________________________________________

# 4.  Write a Python program to find all starting positions of a substring, including overlapping occurrences.
s = input("Enter string: ")
sub = input("Enter substring: ")

positions = []

for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        positions.append(i)

print("Positions =", positions)

#______________________________________________________________

# 5.  Write a Python program to rotate a string to the left by n positions.
s = input("Enter string: ")
n = int(input("Enter number of positions: "))

result = s[n:] + s[:n]

print("Rotated string =", result)

#______________________________________________________________

# 6.  Write a Python program to compare two strings after ignoring spaces and letter case
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

if s1 == s2:
    print("Strings are equal after normalization = True")
else:
    print("Strings are equal after normalization = False")

#______________________________________________________________

# 7.  Write a Python program to find the first and last occurrence of a given character in a string
s = input("Enter string: ")
ch = input("Enter character: ")

first = s.find(ch)
last = s.rfind(ch)

print("First index =", first)
print("Last index =", last)

#______________________________________________________________

# 8.  Write a Python program to compress consecutive repeated characters using character counts.
s = input("Enter a string: ")

result = ""
count = 1

for i in range(len(s)):
    if i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

print("Compressed string =", result)


#______________________________________________________________

# 9.  Write a Python program to check whether a sentence is a pangram.
s = input("Enter a sentence: ")

s = s.lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"

is_pangram = True

for ch in alphabet:
    if ch not in s:
        is_pangram = False
        break

print("Pangram =", is_pangram)

#______________________________________________________________

# 10.  Write a Python program to extract unique words from a sentence while preserving their original order
s = input("Enter a sentence: ")

words = s.lower().split()

unique = []

for word in words:
    if word not in unique:
        unique.append(word)

print(unique)

#______________________________________________________________

# 1.  Write a Python program to find the longest substring that contains no repeated characters
s = input("Enter a string: ")

longest = ""

for i in range(len(s)):
    current = ""

    for j in range(i, len(s)):
        if s[j] in current:
            break

        current += s[j]

        if len(current) > len(longest):
            longest = current

print("Longest substring =", longest)
print("Length =", len(longest))

#______________________________________________________________

# 2.  Write a Python program to find the longest palindromic substring in a given strings
s = input("Enter a string: ")

longest = ""

for i in range(len(s)):
    for j in range(i, len(s)):
        part = s[i:j + 1]

        if part == part[::-1]:
            if len(part) > len(longest):
                longest = part

print("One longest palindromic substring =", longest)

#______________________________________________________________

# 3.  Write a Python program to encrypt a string using a Caesar cipher with a given shift.
s = input("Enter text: ")
shift = int(input("Enter shift: "))

result = ""

for ch in s:
    if ch.isupper():
        result += chr((ord(ch) - 65 + shift) % 26 + 65)
    elif ch.islower():
        result += chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        result += ch

print("Encrypted text =", result)

#______________________________________________________________

# 4.  Write a Python program to decode a run-length encoded string.

s = input("Enter encoded string: ")

result = ""
i = 0

while i < len(s):
    ch = s[i]
    i += 1

    number = ""

    while i < len(s) and s[i].isdigit():
        number += s[i]
        i += 1

    result += ch * int(number)

print("Decoded string =", result)

#______________________________________________________________

# 5.  Write a Python program to check whether brackets in an expression are balanced.
s = input("Enter expression: ")

stack = []

pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

balanced = True

for ch in s:
    if ch in "([{":
        stack.append(ch)

    elif ch in ")]}":
        if len(stack) == 0 or stack[-1] != pairs[ch]:
            balanced = False
            break

        stack.pop()

if len(stack) != 0:
    balanced = False

print("Balanced =", balanced)

#______________________________________________________________

# 6.  Write a Python program to find the longest common prefix among a list of strings.

words = ['flower', 'flow', 'flight']

prefix = words[0]

for word in words[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print("Longest common prefix =", prefix)

#______________________________________________________________

# 7.  Write a Python program to group a list of words into anagram groups.
words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

groups = {}

for word in words:
    key = ''.join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

result = list(groups.values())

print(result)
#______________________________________________________________

# 8.  Write a Python program to convert a snake_case identifier into camelCase.

s = input("Enter snake_case string: ")

words = s.split("_")

result = words[0]

for word in words[1:]:
    result += word[0].upper() + word[1:]

print(result)


#______________________________________________________________

# 9.  Write a Python program to determine whether a string is made by repeating a smaller substring
s = input("Enter a string: ")

pattern = ""

for i in range(1, len(s) + 1):
    if len(s) % i == 0:
        pattern = s[:i]

        if pattern * (len(s) // i) == s:
            print("Repeated pattern =", pattern)
            print("Repeat count =", len(s) // i)
            break


#______________________________________________________________

# 10.  Write a Python program to find the smallest substring that contains all characters of a given pattern.
s = input("Enter string: ")
pattern = input("Enter pattern: ")

best = ""

for i in range(len(s)):
    for j in range(i, len(s)):
        part = s[i:j + 1]

        found = True

        for ch in pattern:
            if ch not in part:
                found = False
                break

        if found:
            if best == "" or len(part) < len(best):
                best = part

print("Minimum window =", best)

#______________________________________________________________

