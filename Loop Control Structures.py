
# Q1. Write a Python program to print all natural numbers from 1 to n using while loop.

n = int(input("Enter n: "))

i = 1

while i <= n:
    print(i)
    i = i + 1

#____________________________________________________________________________________________

# Q2. Write a Python program to print all natural numbers in reverse (from n to 1) using while loop.

n = int(input("Enter n: "))

while n >= 1:
    print(n)
    n = n - 1

 #____________________________________________________________________________________________

# Q3. Write a Python program to print all alphabets from a to z using while loop.

i = ord('a')

while i <= ord('z'):
    print(chr(i), end=" ")
    i = i + 1

#____________________________________________________________________________________________

# Q4. Write a Python program to print all even numbers between 1 to 100 using while loop.

i = 2

while i <= 100:
    print(i, end=" ")
    i = i + 2

#____________________________________________________________________________________________

# Q5. Write a Python program to print all odd number between 1 to 100.

i = 1

while i <= 100:
    print(i, end=" ")
    i = i + 2
#____________________________________________________________________________________________

# Q6. Write a Python program to find sum of all natural numbers between 1 to n.

n = int(input("Enter n: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum =", sum)
#____________________________________________________________________________________________

# Q7. Write a Python program to find sum of all even numbers between 1 to n.

n = int(input("Enter n: "))

i = 2
sum = 0

while i <= n:
    sum = sum + i
    i = i + 2

print("Sum of even numbers =", sum)

#____________________________________________________________________________________________

# Q8. Write a Python program to find sum of all odd numbers between 1 to n.

n = int(input("Enter n: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 2

print("Sum of odd numbers =", sum)
#____________________________________________________________________________________________

# Q10. Write a Python program to print multiplication table of any number. Take user input.

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
#____________________________________________________________________________________________

# Q11. Write a Python program to count number of digits in a number.

n = int(input("Enter a number: "))

count = 0

while n > 0:
    n = n // 10
    count = count + 1

print("Number of digits =", count)
#____________________________________________________________________________________________

# Q12. Write a Python program to find first and last digit of a number.

n = int(input("Enter a number: "))

last = n % 10

while n >= 10:
    n = n // 10

first = n

print("First digit =", first)
print("Last digit =", last)
#____________________________________________________________________________________________

# Q13. Write a Python program to find sum of first and last digit of a number.
  
n = int(input("Enter a number: "))

last = n % 10

while n >= 10:
    n = n // 10

first = n

sum = first + last

print("Sum of first and last digit =", sum)

#____________________________________________________________________________________________

# Q14. Write a Python program to swap first and last digits of a number.

n = int(input("Enter a number: "))

last = n % 10
temp = n

count = 0

while temp >= 10:
    temp = temp // 10
    count = count + 1

first = temp

middle = (n % (10 ** count)) // 10

result = last * (10 ** count) + middle * 10 + first

print("Number after swapping =", result)

#____________________________________________________________________________________________

# Q15. Write a Python program to calculate sum of digits of a number.

n = int(input("Enter a number: "))

sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("Sum of digits =", sum)

#____________________________________________________________________________________________

# Q16. Write a Python program to calculate product of digits of a number.

n = int(input("Enter a number: "))

product = 1

while n > 0:
    digit = n % 10
    product = product * digit
    n = n // 10

print("Product of digits =", product)
#____________________________________________________________________________________________

# Q17. Write a Python program to enter a number and print its reverse.

n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse =", reverse)
#____________________________________________________________________________________________

# Q18. Write a Python program to check whether a number is palindrome or not.

n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
#____________________________________________________________________________________________

# Q19. Write a Python program to find frequency of each digit in a given integer.

n = int(input("Enter a number: "))

for i in range(10):
    count = 0
    temp = n

    while temp > 0:
        digit = temp % 10

        if digit == i:
            count = count + 1

        temp = temp // 10

    if count > 0:
        print(i, "=", count)
#____________________________________________________________________________________________

# Q20. Write a Python program to enter a digit and print it in words.

digit = int(input("Enter a digit: "))

if digit == 0:
    print("Zero")
elif digit == 1:
    print("One")
elif digit == 2:
    print("Two")
elif digit == 3:
    print("Three")
elif digit == 4:
    print("Four")
elif digit == 5:
    print("Five")
elif digit == 6:
    print("Six")
elif digit == 7:
    print("Seven")
elif digit == 8:
    print("Eight")
elif digit == 9:
    print("Nine")
else:
    print("Invalid digit") 

#____________________________________________________________________________________________

# Q21. Write a Python program to find power of a number using for loop.

base = int(input("Enter base: "))
power = int(input("Enter power: "))

result = 1

for i in range(power):
    result = result * base

print("Power =", result)

#____________________________________________________________________________________________

# Q22. Write a Python program to calculate factorial of a number.

n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print("Factorial =", factorial)

#____________________________________________________________________________________________

# Q23. Write a Python program to find HCF (GCD) of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

hcf = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

print("HCF =", hcf)

#____________________________________________________________________________________________

# Q24. Write a Python program to find LCM of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    lcm = a
else:
    lcm = b

while True:
    if lcm % a == 0 and lcm % b == 0:
        break

    lcm = lcm + 1

print("LCM =", lcm)

#____________________________________________________________________________________________

# Q25. Write a Python program to check whether a number is Prime number or not.

n = int(input("Enter a number: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("Prime number")
else:
    print("Not a Prime number")

#____________________________________________________________________________________________

# Q26. Write a Python program to print all Prime numbers between 1 to n.

n = int(input("Enter n: "))

for number in range(2, n + 1):

    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count = count + 1

    if count == 2:
        print(number, end=" ")
#____________________________________________________________________________________________

# Q27. Write a Python program to find sum of all prime numbers between 1 to n.

n = int(input("Enter n: "))

sum = 0

for number in range(2, n + 1):

    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count = count + 1

    if count == 2:
        sum = sum + number

print("Sum of prime numbers =", sum)

#____________________________________________________________________________________________

# Q28. Write a Python program to check whether a number is Armstrong number or not.

n = int(input("Enter a number: "))

original = n
sum = 0
digits = len(str(n))

while n > 0:
    digit = n % 10
    sum = sum + digit ** digits
    n = n // 10

if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

#____________________________________________________________________________________________

# Q29. Write a Python program to print all Armstrong numbers between 1 to n.

n = int(input("Enter n: "))

for number in range(1, n + 1):

    original = number
    temp = number
    sum = 0

    digits = len(str(number))

    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** digits
        temp = temp // 10

    if sum == original:
        print(number, end=" ")
#____________________________________________________________________________________________

# Q30. Write a Python program to print Fibonacci series up to n terms.

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c
#____________________________________________________________________________________________

# Q31. Write a Python program to print the given star patterns.

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")

    print()

#____________________________________________________________________________________________

# Q32. Write a Python program to print the given number patterns.

for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")

    print()

