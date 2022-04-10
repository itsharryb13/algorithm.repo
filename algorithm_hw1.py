####################################
# 1. Compute the sum of digits in all numbers from 1 to n. When a user enters a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
#
# 2.Find max number from 3 values, entered manually from a keyboard.
# Example: 124, 21, 32. Result = 124.
#
# 3. Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

###################################

#
# # Program 1
n = int(input("Please enter positive whole number = "))
sum = 0

for i in range(0,n):
    sum = sum +  i

print(f'Sum of digits in all numbers from 1 to n = {sum}')

############################################################

# Program 2
a = []
for i in range(0,3):
    a.append(int(input("Please enter positive whole number = ")))
    a.sort()

print(a[-1])

############################################################

# Program 3
c = int(input("please enter a number"))
b =[]
even = []
odd = []

while c > 0:
    b.append(c % 10)
    c = int(c/10)

for m in range(0,len(b)):
    if (int(b[m]%2)==0): even.append(b[m])
    else: odd.append(b[m])

print(f'Even numbers = {even} and Odd numbers = {odd}')