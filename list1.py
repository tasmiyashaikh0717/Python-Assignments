# 1. Write a Python program to sum all the items in a list.

numbers = [10, 20, 30, 40]

total = 0

for n in numbers:
    total = total + n

print("Sum =", total)

#_______________________________________________________________________

# 2. Write a Python program to multiplies all the items in a list.

numbers = [2, 3, 4, 5]

product = 1

for n in numbers:
    product = product * n

print("Product =", product)

#_______________________________________________________________________

# 3. Write a Python program to get the largest number from a list.

numbers = [10, 25, 5, 40, 15]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("Largest =", largest)

# _____________________________________________________________________

# 4. Write a Python program to get the smallest number from a list. 

numbers = [10, 25, 5, 40, 15]

smallest = numbers[0]

for n in numbers:
    if n < smallest:
        smallest = n

print("Smallest =", smallest)

#_______________________________________________________________________

# 5. Write a Python program to count the number of strings where the string length
# is 2 or more and the first and last character are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

words = ['abc', 'xyz', 'aba', '1221']

count = 0

for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count = count + 1

print("Count =", count)

#_______________________________________________________________________

#6. Write a Python program to get a list, sorted in increasing order by the last 
# element in each tuple from a given list of non-empty tuples.  
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# numbers = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

result = sorted(numbers, key=lambda x: x[-1])

print(result)

#_______________________________________________________________________

# 7. Write a Python program to remove duplicates from a list. 

numbers = [1, 2, 2, 3, 1, 4]

new_list = []

for n in numbers:
    if n not in new_list:
        new_list.append(n)

print(new_list)

#_______________________________________________________________________

# 8. Write a Python program to check a list is empty or not. 
numbers = []

if len(numbers) == 0:
    print("List is empty")
else:
    print("List is not empty")


#_______________________________________________________________________

# 9. Write a Python program to clone or copy a list.

numbers = [10, 20, 30, 40]

new_list = numbers.copy()

print("Original list =", numbers)
print("Copied list =", new_list)

#_______________________________________________________________________

# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
words = ["apple", "cat", "banana", "dog", "elephant"]

n = 5

result = []

for word in words:
    if len(word) > n:
        result.append(word)

print(result)

#_______________________________________________________________________

# 11. Write a Python function that takes two lists and returns True if they have at least one common member. 

list1 = [1, 2, 3, 4]
list2 = [5, 6, 3, 8]

found = False

for x in list1:
    if x in list2:
        found = True
        break

print(found)

#_______________________________________________________________________

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

numbers = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

result = []

for i in range(len(numbers)):
    if i != 0 and i != 4 and i != 5:
        result.append(numbers[i])

print(result)

#_______________________________________________________________________

# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *. 

array = []

for i in range(3):
    layer = []

    for j in range(4):
        row = []

        for k in range(6):
            row.append('*')

        layer.append(row)

    array.append(layer)

print(array)

#_______________________________________________________________________

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it. 
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = []

for n in numbers:
    if n % 2 != 0:
        result.append(n)

print(result)

#_______________________________________________________________________

# 15. Write a Python program to shuffle and print a specified list. 
import random

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)

#_______________________________________________________________________

# 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). 

squares = []

for n in range(1, 31):
    squares.append(n * n)

result = squares[:5] + squares[-5:]

print(result)

#_______________________________________________________________________

# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).

squares = []

for n in range(1, 31):
    squares.append(n * n)

result = squares[5:]

print(result)

#_______________________________________________________________________

# 18. Write a Python program to generate all permutations of a list in Python. 

from itertools import permutations

numbers = [1, 2, 3]

result = permutations(numbers)

for item in result:
    print(item)

#_______________________________________________________________________

# 19. Write a Python program to get the difference between the two lists. 

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = []

for x in list1:
    if x not in list2:
        result.append(x)

for x in list2:
    if x not in list1:
        result.append(x)

print(result)

#_______________________________________________________________________

# 20. Write a Python program access the index of a list. 

numbers = [10, 20, 30, 40]

for i in range(len(numbers)):
    print("Index", i, "=", numbers[i])

#_______________________________________________________________________

# 21. Write a Python program to convert a list of characters into a string. 

characters = ['P', 'y', 't', 'h', 'o', 'n']

result = ""

for ch in characters:
    result = result + ch

print(result)

#_______________________________________________________________________

# 22. Write a Python program to find the index of an item in a specified list. 

numbers = [10, 20, 30, 40, 50]

item = 30

if item in numbers:
    index = numbers.index(item)
    print("Index =", index)
else:
    print("Item not found")

#_______________________________________________________________________

# 23. Write a Python program to flatten a shallow list. 

numbers = [[1, 2], [3, 4], [5, 6]]

result = []

for item in numbers:
    for x in item:
        result.append(x)

print(result)

#_______________________________________________________________________

# 24. Write a Python program to append a list to the second list. 

list1 = [1, 2, 3]
list2 = [4, 5, 6]

for x in list2:
    list1.append(x)

print(list1)

#_______________________________________________________________________

# 25. Write a Python program to select an item randomly from a list.

import random

numbers = [10, 20, 30, 40, 50]

item = random.choice(numbers)

print("Random item =", item)

#_______________________________________________________________________

# 26. Write a python program to check whether two lists are circularly identical. 

list1 = [1, 2, 3, 4]
list2 = [3, 4, 1, 2]

if len(list1) == len(list2) and list2 in list1 + list1:
    print("Circularly identical")
else:
    print("Not circularly identical")


#_______________________________________________________________________

# 27. Write a Python program to find the second smallest number in a list. 

numbers = [10, 5, 20, 3, 8]

numbers = list(set(numbers))
numbers.sort()

print("Second smallest =", numbers[1])

#_______________________________________________________________________

# 28. Write a Python program to find the second largest number in a list. 

numbers = [10, 5, 20, 3, 8]

numbers = list(set(numbers))
numbers.sort()

print("Second largest =", numbers[-2])

#_______________________________________________________________________

# 29. Write a Python program to get unique values from a list. 

numbers = [1, 2, 2, 3, 4, 4, 5]

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print(unique)

#_______________________________________________________________________

# 30. Write a Python program to get the frequency of the elements in a list. 

numbers = [1, 2, 2, 3, 3, 3]

frequency = {}

for n in numbers:
    if n in frequency:
        frequency[n] = frequency[n] + 1
    else:
        frequency[n] = 1

print(frequency)

#_______________________________________________________________________

# 31. Write a Python program to count the number of elements in a list within a specified range. 

numbers = [10, 15, 20, 25, 30, 35, 40]

start = 20
end = 35

count = 0

for n in numbers:
    if n >= start and n <= end:
        count = count + 1

print("Count =", count)

#_______________________________________________________________________

# 32. Write a Python program to check whether a list contains a sublist.

numbers = [1, 2, 3, 4, 5]

sublist = [2, 3, 4]

found = False

for i in range(len(numbers) - len(sublist) + 1):
    if numbers[i:i + len(sublist)] == sublist:
        found = True
        break

print(found)

#_______________________________________________________________________

# 33. Write a Python program to generate all sublists of a list. 

numbers = [1, 2, 3]

sublists = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers) + 1):
        sublists.append(numbers[i:j])

print(sublists)

#_______________________________________________________________________

# 34. Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number. 

n = 30

prime = [True] * (n + 1)

prime[0] = False
prime[1] = False

for i in range(2, n + 1):
    if prime[i]:
        for j in range(i * 2, n + 1, i):
            prime[j] = False

for i in range(2, n + 1):
    if prime[i]:
        print(i, end=" ")

#_______________________________________________________________________

# 35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n. 
letters = ['p', 'q']
n = 5

result = []

for i in range(1, n + 1):
    for letter in letters:
        result.append(letter + str(i))

print(result)

#_______________________________________________________________________

# 36. Write a Python program to get variable unique identification number or string. 
import uuid

unique_id = uuid.uuid4()

print(unique_id)

#_______________________________________________________________________

# 37. Write a Python program to find common items from two lists. 

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []

for x in list1:
    if x in list2:
        common.append(x)

print(common)

#_______________________________________________________________________

# 38. Write a Python program to change the position of every n-th value with the (n+1)th in a list. 

numbers = [0, 1, 2, 3, 4, 5]

for i in range(0, len(numbers) - 1, 2):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print(numbers)

#_______________________________________________________________________

# 39. Write a Python program to convert a list of multiple integers into a single integer. 

numbers = [11, 33, 50]

result = ""

for n in numbers:
    result = result + str(n)

result = int(result)

print(result)

#_______________________________________________________________________

# 40. Write a Python program to split a list based on first character of word.

words = ["apple", "banana", "ant", "ball", "cat", "car"]

result = {}

for word in words:
    first = word[0]

    if first not in result:
        result[first] = []

    result[first].append(word)

print(result)

#_______________________________________________________________________

# 41. Write a Python program to create multiple lists. 

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

print("List 1 =", list1)
print("List 2 =", list2)
print("List 3 =", list3)

#_______________________________________________________________________

# 42. Write a Python program to find missing and additional values in two lists. 

list1 = ['a', 'b', 'c', 'd', 'e']
list2 = ['d', 'e', 'g', 'h']

missing = []
additional = []

for x in list1:
    if x not in list2:
        missing.append(x)

for x in list2:
    if x not in list1:
        additional.append(x)

print("Missing values =", missing)
print("Additional values =", additional)

#_______________________________________________________________________

# 43. Write a Python program to split a list into different variables. 

numbers = [10, 20, 30]

a, b, c = numbers

print("a =", a)
print("b =", b)
print("c =", c)

#_______________________________________________________________________

# 44. Write a Python program to generate groups of five consecutive numbers in a list. 

numbers = list(range(1, 21))

groups = []

for i in range(0, len(numbers), 5):
    groups.append(numbers[i:i + 5])

print(groups)

#_______________________________________________________________________

# 45. Write a Python program to convert a pair of values into a sorted unique array.

numbers = [5, 2, 5, 3, 2, 1]

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

unique.sort()

print(unique)

#_______________________________________________________________________

# 46. Write a Python program to select the odd items of a list. 

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

odd_numbers = []

for n in numbers:
    if n % 2 != 0:
        odd_numbers.append(n)

print(odd_numbers)

#_______________________________________________________________________

# 47. Write a Python program to insert an element before each element of a list. 

numbers = [1, 2, 3, 4]
element = 0

result = []

for n in numbers:
    result.append(element)
    result.append(n)

print(result)

#_______________________________________________________________________

# 48. Write a Python program to print a nested lists (each list on a new line) using the print() function.

numbers = [[1, 2], [3, 4], [5, 6]]

for item in numbers:
    print(item)

#_______________________________________________________________________

# 49. Write a Python program to convert list to list of dictionaries. 

color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

result = []

for i in range(len(color_names)):
    data = {
        "color_name": color_names[i],
        "color_code": color_codes[i]
    }

    result.append(data)

print(result)

#_______________________________________________________________________

# 50. Write a Python program to sort a list of nested dictionaries. 
students = [
    {"name": "Amit", "marks": 70},
    {"name": "Riya", "marks": 90},
    {"name": "John", "marks": 80}
]

students.sort(key=lambda x: x["marks"])

print(students)

#_______________________________________________________________________

# 51. Write a Python program to split a list every Nth element. 

letters = ['a', 'b', 'c', 'd', 'e', 'f',
           'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

n = 3

result = []

for i in range(n):
    group = []

    for j in range(i, len(letters), n):
        group.append(letters[j])

    result.append(group)

print(result)

#_______________________________________________________________________

# 52. Write a Python program to compute the similarity between two lists. 

list1 = ["red", "orange", "green", "blue", "white"]
list2 = ["black", "yellow", "green", "blue"]

common = []

for x in list1:
    if x in list2:
        common.append(x)

list1_only = []

for x in list1:
    if x not in list2:
        list1_only.append(x)

list2_only = []

for x in list2:
    if x not in list1:
        list2_only.append(x)

print("Common =", common)
print("List1 - List2 =", list1_only)
print("List2 - List1 =", list2_only)

#_______________________________________________________________________

# 52. Write a Python program to compute the similarity between two lists. 

numbers = []

i = 1

while True:
    numbers.append(i)
    print(i)

    i = i + 1

#_______________________________________________________________________

# 54. Write a Python program to concatenate elements of a list. 

words = ["Hello", "Python", "World"]

result = ""

for word in words:
    result = result + word

print(result)

#_______________________________________________________________________

# 55. Write a Python program to remove key values pairs from a list of dictionaries.
students = [
    {"name": "Amit", "age": 20},
    {"name": "Riya", "age": 21},
    {"name": "John", "age": 19}
]

for student in students:
    del student["age"]

print(students)

#_______________________________________________________________________

# 56. Write a Python program to convert a string to a list. 

text = "Python"

result = list(text)

print(result)

#_______________________________________________________________________

# 57. Write a Python program to check if all items of a list is equal to a given string.

words = ["apple", "apple", "apple"]

given = "apple"

result = True

for word in words:
    if word != given:
        result = False
        break

print(result)


#_______________________________________________________________________

# 58. Write a Python program to replace the last element in a list with another list. 

list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]

list1[-1:] = list2

print(list1)

#_______________________________________________________________________

# 59. Write a Python program to check if the n-th element exists in a given list. 

numbers = [10, 20, 30, 40, 50]

n = 3

if n >= 0 and n < len(numbers):
    print("Element exists")
else:
    print("Element does not exist")


#_______________________________________________________________________

# 60. Write a Python program to find a tuple, the smallest second index value from a list of tuples. 
numbers = [(1, 5), (2, 3), (4, 1), (6, 4)]

smallest = numbers[0]

for item in numbers:
    if item[1] < smallest[1]:
        smallest = item

print(smallest)


#_______________________________________________________________________

# 61. Write a Python program to create a list of empty dictionaries. 
numbers = [{}, {}, {}, {}, {}]

print(numbers)

#_______________________________________________________________________

# 62. Write a Python program to print a list of space-separated elements. 

numbers = [10, 20, 30, 40, 50]

for n in numbers:
    print(n, end=" ")

#_______________________________________________________________________

# 63. Write a Python program to insert a given string at the beginning of all items in a list.  

numbers = [1, 2, 3, 4]
text = "emp"

result = []

for n in numbers:
    result.append(text + str(n))

print(result)

#_______________________________________________________________________

# 64. Write a Python program to iterate over two lists simultaneously. 

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

for i in range(len(list1)):
    print(list1[i], list2[i])

#_______________________________________________________________________

# 65. Write a Python program to access dictionary keys element by index. 

student = {
    "name": "Amit",
    "age": 20,
    "city": "Pune"
}

keys = list(student.keys())

print(keys[0])
print(keys[1])
print(keys[2])

#_______________________________________________________________________

# 66. Write a Python program to find the list in a list of lists whose sum of elements is the highest. 

lists = [
    [1, 2, 3],
    [4, 5, 6],
    [10, 11, 12],
    [7, 8, 9]
]

highest_list = lists[0]
highest_sum = sum(lists[0])

for item in lists:
    if sum(item) > highest_sum:
        highest_sum = sum(item)
        highest_list = item

print(highest_list)

#_______________________________________________________________________

#  66. Write a Python program to find the list in a list of lists whose sum of elements is the highest. 

numbers = [10, 20, 30, 40, 50]

given = 5

result = True

for n in numbers:
    if n <= given:
        result = False
        break

print(result)


#_______________________________________________________________________

# 68. Write a Python program to extend a list without append. 


list1 = [10, 20, 30]
list2 = [40, 50, 60]

result = list2 + list1

print(result)

#_______________________________________________________________________

# 69. Write a Python program to remove duplicates from a list of lists. 

numbers = [
    [10, 20],
    [40],
    [30, 56, 25],
    [10, 20],
    [33],
    [40]
]

result = []

for item in numbers:
    if item not in result:
        result.append(item)

print(result)

#_______________________________________________________________________

# 70. Write a Python program to get the depth of a dictionary. 

data = {
    "a": {
        "b": {
            "c": 10
        }
    }
}

def depth(dictionary):
    if not isinstance(dictionary, dict) or len(dictionary) == 0:
        return 0

    maximum = 0

    for value in dictionary.values():
        if isinstance(value, dict):
            d = depth(value)

            if d > maximum:
                maximum = d

    return maximum + 1


print("Depth =", depth(data))

#_______________________________________________________________________

# 71. Write a Python program to check if all dictionaries in a list are empty or not. 

data = [{}, {}, {}]

result = True

for item in data:
    if item != {}:
        result = False
        break

print(result)