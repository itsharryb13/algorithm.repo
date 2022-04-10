##############################################
# Reverse a Statement
# Build an algorithm that will print the given statement in reverse.
# Example: Initial string = Everything is hard before it is easy
# Reversed string = easy is it before hard is Everything
#
# Permutations
# Write a solution that will print all permutations of a string.
# A permutation is an act of changing the arrangement of characters.
# Example: String = ABC, Return {ABC, ACB, BAC, BCA, CBA, CAB}
#
# Count Characters
# Create a program that will count vowels and consonants in a string.
# Example: String = “hello world”, Return {Vowels: 3, Consonants: 7}
##################################################################
#problem 1

def intial_string(n):
    reverse = n.split(" ")
    final = " ".join(reversed(reverse))
    return  final.title()

test_case= "Everything is hard before it is easy"
print(intial_string(test_case))

#############################################################
#problem 2
from itertools import permutations
def premutation_string(n):
    final= permutations(n)
    for i in list(final):
        print("".join(i),end=" ")

test_case2 = input("Enter A string: ")
premutation_string(test_case2)

##############################################################
#problem 3

def count_char(n):
    vowels = "aeiouAEIOU"
    m = n.replace(" ", "")
    count=0
    for i in m:
        for y in vowels:
            if(i == y):
                print(i,y)
                count= count+1

    print(f'Vowels = {count} and Consonats = {len(m)-count}')


test_case3 = "Hello World"
count_char(test_case3)