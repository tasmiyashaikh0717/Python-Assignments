# 1. Write a Python program to find maximum between two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Maximum =", a)
else:
    print("Maximum =", b)

# ________________________________________________________________________


# 2. Write a Python program to find maximum among three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Maximum =", a)
elif b >= a and b >= c:
    print("Maximum =", b)
else:
    print("Maximum =", c)

# ________________________________________________________________________


# 3. Write a Python program to check whether a number is negative, positive or 
# zero.

n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# ________________________________________________________________________


# 4. Write a Python program to check whether a number is divisible by 5 and 11
# or not.

n = int(input("Enter a number: "))

if n % 5 == 0 and n % 11 == 0:
    print("Number is divisible by 5 and 11")
else:
    print("Number is not divisible by 5 and 11")

# ________________________________________________________________________


# 5. Write a Python program to check whether a number is even or odd.

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


# ________________________________________________________________________


# 6. Write a Python program to check whether a year is leap year or not.

year = int(input("Enter year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")


# ________________________________________________________________________


# 7. Write a Python program to check whether a character is alphabet or not.

ch = input("Enter a character: ")

if ch.isalpha():
    print("Alphabet")
else:
    print("Not an alphabet")

# ________________________________________________________________________


# 8. Write a Python program to input any alphabet and check whether it is 
# vowel or consonant.

ch = input("Enter an alphabet: ")

if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")

# ________________________________________________________________________


# 9. Write a Python program to check whether a character is uppercase or 
# lowercase alphabet.

ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase alphabet")
elif ch.islower():
    print("Lowercase alphabet")
else:
    print("Not an alphabet")

# ________________________________________________________________________


# 10. Write a Python program to count total number of notes in given amount

amount = int(input("Enter amount: "))

notes = [500, 200, 100, 50, 20, 10]

total = 0

for note in notes:
    count = amount // note
    amount = amount % note

    print(note, ":", count)
    total += count

print("Total notes =", total)

# ________________________________________________________________________


# 11. Write a Python program to input angles of a triangle and check whether 
# triangle is valid or not.

a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a > 0 and b > 0 and c > 0 and a + b + c == 180:
    print("Valid triangle")
else:
    print("Invalid triangle")

# ________________________________________________________________________


# 12. Write a Python program to input all sides of a triangle and check whether 
# triangle is valid or not.

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")

# ________________________________________________________________________


# 12. Write a Python program to input all sides of a triangle and check whether 
# triangle is valid or not.

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

# ________________________________________________________________________


# 14. Write a Python program to calculate profit or loss. Input is selling cost and 
# actual cost.

cost = float(input("Enter actual cost: "))
selling = float(input("Enter selling cost: "))

if selling > cost:
    profit = selling - cost
    print("Profit =", profit)
elif cost > selling:
    loss = cost - selling
    print("Loss =", loss)
else:
    print("No profit, no loss")

# ________________________________________________________________________


# 15. Write a Python program to input marks of five subjects Physics, Chemistry,
# Biology, Mathematics and Computer. Calculate percentage and grade 
# according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F



physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
biology = float(input("Enter Biology marks: "))
maths = float(input("Enter Mathematics marks: "))
computer = float(input("Enter Computer marks: "))

total = physics + chemistry + biology + maths + computer

percentage = total / 5

print("Percentage =", percentage)

if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
else:
    print("Grade F")


# ________________________________________________________________________


# 16. Write a Python program to input basiPython salary of an employee and 
# calculate its Gross salary according to following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 30%, DA = 90%
# Basic Salary > 20000 : HRA = 35%, DA = 95%


basic = float(input("Enter basic salary: "))

if basic <= 10000:
    hra = basic * 20 / 100
    da = basic * 80 / 100

elif basic <= 20000:
    hra = basic * 30 / 100
    da = basic * 90 / 100

else:
    hra = basic * 35 / 100
    da = basic * 95 / 100

gross = basic + hra + da

print("HRA =", hra)
print("DA =", da)
print("Gross Salary =", gross)

# ________________________________________________________________________


# 17. Write a Python program to input electricity unit charges and calculate total 
# electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.25/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 17% is added to the bill

units = float(input("Enter electricity units: "))

if units <= 50:
    bill = units * 0.50

elif units <= 150:
    bill = 50 * 0.50
    bill += (units - 50) * 0.75

elif units <= 250:
    bill = 50 * 0.50
    bill += 100 * 0.75
    bill += (units - 150) * 1.25

else:
    bill = 50 * 0.50
    bill += 100 * 0.75
    bill += 100 * 1.25
    bill += (units - 250) * 1.50

surcharge = bill * 17 / 100

total_bill = bill + surcharge

print("Electricity Bill =", bill)
print("Surcharge =", surcharge)
print("Total Bill =", total_bill)

