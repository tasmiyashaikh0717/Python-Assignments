# 1.  Write a Python program to create a list and display all its elements.

list = [10,20,30,40]
print(list)

#__________________________________________________________________________________

# 2.  Write a Python program to find the sum and average of list elements.

list = [10,20,30,40]
total = sum(list)
average = total / len(list)

print("Sum =", total)
print("Average =", average)
#__________________________________________________________________________________

# 3.  Write a Python program to find the largest and smallest element in a list

list =[8, 3, 15, 1, 9]

print("Largest:",max(list))
print("Smallest:",min(list))

#__________________________________________________________________________________

# 4.  Write a Python program to count even and odd numbers in a list.

list = [1, 2, 3, 4, 5, 6]

even = 0
odd = 0

for n in list:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even count:",even)
print("Odd count:",odd)

#__________________________________________________________________________________

# 5.  Write a Python program to remove duplicate elements from a list.

list = [1, 2, 2, 3, 1, 4]

new_list = []

for n in list:
    if n not in new_list:
        new_list.append(n)

print(new_list)

#__________________________________________________________________________________

# 6.  Write a Python program to reverse a list without using the reverse() method.

list = [10, 20, 30, 40]

new_list = []

for i in range(len(list) - 1, -1, -1):
    new_list.append(list[i])

print(new_list)

#__________________________________________________________________________________

# 7.  Write a Python program to merge two lists into a single list.

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

print(list_1 + list_2)

#__________________________________________________________________________________

# 8.  Write a Python program to find the second largest number in a list.

numbers = [10, 40, 20, 30, 50]

numbers = list(set(numbers))
numbers.sort()

print("Second largest =", numbers[-2])

#__________________________________________________________________________________

#9.  Write a Python program to sort a list in ascending and descending order.

list =  [5, 2, 8, 1, 4]

print("Ascending order:",sorted(list))
print("Descending Order:",sorted(list , reverse= True))

#__________________________________________________________________________________

# 10.  Write a Python program to search for an element in a list.

list = [10, 20, 30, 40]
search = 30

if search in list:
    print(search, "found at index :", list.index(search))
else:
    print("Element not found")    


#__________________________________________________________________________________

# 11.  Write a Python program to insert an element at a specific position in a list.

list = [10, 20, 40]
list.insert(2,30)
print(list)

#__________________________________________________________________________________

# 12.  Write a Python program to delete all occurrences of a given element from a list.

numbers = [1, 2, 3, 2, 4, 2]

delete = 2

new_list = []

for n in numbers:
    if n != delete:
        new_list.append(n)

print(new_list)

#__________________________________________________________________________________

# 13.  Write a Python program to separate positive and negative numbers from a list.

numbers = [-5, 3, -2, 7, 0, -1]

positive = []
negative = []

for n in numbers:
    if n > 0:
        positive.append(n)
    elif n < 0:
        negative.append(n)

print("Positive =", positive)
print("Negative =", negative)

#__________________________________________________________________________________

# 14.  Write a Python program to find common elements between two lists.

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = []

for n in list1:
    if n in list2:
        common.append(n)

print("Common elements =", common)

#__________________________________________________________________________________

# 15.  Write a Python program to create a new list containing squares of all elements of a list.

numbers = [1, 2, 3, 4, 5]

squares = []

for n in numbers:
    squares.append(n * n)

print(squares)

#__________________________________________________________________________________

# 16.  Write a Python program to rotate a list by n positions.

numbers = [1, 2, 3, 4, 5]
n = 2

result = numbers[n:] + numbers[:n]

print(result)
#__________________________________________________________________________________

# 1.  Write a Python program to remove duplicate values from a list while preserving their first occurrence

numbers = [3, 1, 3, 2, 1, 4]

result = []

for n in numbers:
    if n not in result:
        result.append(n)

print(result)
#__________________________________________________________________________________

# 2.  Write a Python program to split a list into chunks of a given size.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
size = 3

result = []

for i in range(0, len(numbers), size):
    result.append(numbers[i:i + size])

print(result)

#__________________________________________________________________________________

# 3.  Write a Python program to move all zeros to the end of a list without changing the order of non-zero elements.

numbers = [0, 1, 0, 3, 12]

result = []

for n in numbers:
    if n != 0:
        result.append(n)

for n in numbers:
    if n == 0:
        result.append(n)

print(result)

#__________________________________________________________________________________

# 4.  Write a Python program to find the missing number from a list containing values from 1 to n.

numbers = [1, 2, 4, 5, 6]
n = 6

for i in range(1, n + 1):
    if i not in numbers:
        print("Missing number =", i)

#__________________________________________________________________________________

# 5.  Write a Python program to find a pair of numbers whose sum is equal to a given target.

numbers = [2, 7, 11, 15]
target = 9

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print("Pair =", (numbers[i], numbers[j]))

#__________________________________________________________________________________

# 6.  Write a Python program to calculate the element-wise sum of two lists of equal length.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = []

for i in range(len(list1)):
    result.append(list1[i] + list2[i])

print(result)

#__________________________________________________________________________________

# 7.  Write a Python program to count the frequency of each distinct element in a list.

numbers = [1, 2, 2, 3, 3, 3]

frequency = {}

for n in numbers:
    if n in frequency:
        frequency[n] += 1
    else:
        frequency[n] = 1

for n in frequency:
    print(n, "->", frequency[n])

#__________________________________________________________________________________

# 8.  Write a Python program to rotate a list to the left by n positions.

numbers = [1, 2, 3, 4, 5]
n = 3

result = numbers[n:] + numbers[:n]

print(result)

#__________________________________________________________________________________

# 9.  Write a Python program to find common elements between two lists while preserving duplicate occurrences.

list1 = [1, 2, 2, 3]
list2 = [2, 2, 4]

result = []

for n in list1:
    if n in list2:
        result.append(n)
        list2.remove(n)

print(result)

#__________________________________________________________________________________

# 10.  Write a Python program to transpose a two-dimensional list.

matrix = [[1, 2, 3], [4, 5, 6]]

result = []

for i in range(3):
    row = []

    for j in range(2):
        row.append(matrix[j][i])

    result.append(row)

print(result)

#__________________________________________________________________________________

# 1.  Write a Python program to flatten a nested list of any depth into a single list.

numbers = [1, [2, [3, 4], 5], 6]

result = []

def flatten(data):
    for item in data:
        if isinstance(item, list):
            flatten(item)
        else:
            result.append(item)

flatten(numbers)

print(result)

#__________________________________________________________________________________

# 2.  Write a Python program to find the contiguous subarray having the maximum sum.

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum = numbers[0]
current_sum = numbers[0]

for i in range(1, len(numbers)):
    current_sum = max(numbers[i], current_sum + numbers[i])
    max_sum = max(max_sum, current_sum)

print("Maximum sum =", max_sum)

#__________________________________________________________________________________

# 3.  Write a Python program to build a list where each element is the product of all other elements, without using division.

numbers = [1, 2, 3, 4]

result = []

for i in range(len(numbers)):
    product = 1

    for j in range(len(numbers)):
        if i != j:
            product *= numbers[j]

    result.append(product)

print(result)

#__________________________________________________________________________________

# 4.  Write a Python program to find the maximum value in every sliding window of size k.

numbers = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

result = []

for i in range(len(numbers) - k + 1):
    window = numbers[i:i + k]
    result.append(max(window))

print(result)

#__________________________________________________________________________________

# 5.  Write a Python program to merge overlapping intervals represented as a list of [start, end] pairs.

intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]

intervals.sort()

result = [intervals[0]]

for current in intervals[1:]:
    last = result[-1]

    if current[0] <= last[1]:
        last[1] = max(last[1], current[1])
    else:
        result.append(current)

print(result)

#__________________________________________________________________________________

# 6.  Write a Python program to rotate a square matrix represented as a nested list by 90 degrees clockwise.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = []

for i in range(len(matrix)):
    row = []

    for j in range(len(matrix) - 1, -1, -1):
        row.append(matrix[j][i])

    result.append(row)

print(result)

#__________________________________________________________________________________

# 7.  Write a Python program to print the elements of a matrix in spiral order.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = []

while matrix:
    result += matrix.pop(0)

    if matrix and matrix[0]:
        for row in matrix:
            result.append(row.pop())

    if matrix:
        result += matrix.pop()[::-1]

    if matrix and matrix[0]:
        for row in matrix[::-1]:
            result.append(row.pop(0))

print(result)

#__________________________________________________________________________________

# 8.  Write a Python program to find the longest sequence of consecutive integers in an unsorted list.

numbers = [100, 4, 200, 1, 3, 2]

numbers = set(numbers)

longest = []

for n in numbers:
    if n - 1 not in numbers:
        current = []
        x = n

        while x in numbers:
            current.append(x)
            x += 1

        if len(current) > len(longest):
            longest = current

print("Sequence =", longest)
print("Length =", len(longest))

#__________________________________________________________________________________

# 9.  Write a Python program to merge two already sorted lists into one sorted list without calling sort().

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

result = []
i = 0
j = 0

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        result.append(list1[i])
        i += 1
    else:
        result.append(list2[j])
        j += 1

result += list1[i:]
result += list2[j:]

print(result)

#__________________________________________________________________________________

# 10.  Write a Python program to find all contiguous subarrays whose sum equals a target value.

numbers = [1, 2, 3, 2, 1]
target = 5

result = []

for i in range(len(numbers)):
    total = 0

    for j in range(i, len(numbers)):
        total += numbers[j]

        if total == target:
            result.append(numbers[i:j + 1])

print(result)





