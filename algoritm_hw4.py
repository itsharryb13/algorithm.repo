# Even First
# Your input is an array of integers, and you have to reorder its entries so that the even entries appear first. You are required to solve it without allocating additional storage (operate with the input array).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]
#
# Increment a Number
# Write a program that takes as input an array of digits encoding a nonnegative decimal integer D and updates the array to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

basic_test = [6,9,3,1,2,5]
second_test = [1, 2, 9]

####################################################################
def even_first(n):
    even, odd = 0, len(n)-1
    while even < odd:
        if n[even]%2 ==0:
            even = even + 1
        else:
            n[even],n[odd] = n[odd],n[even]
            odd = odd - 1

    print(n)

even_first(basic_test)
#################################################################
def increment_num(n):
    n[-1] = n[-1] + 1
    for i in reversed(range(1,len(n))):
        if n[i] != 10:
            break
        n[i] = 0
        n[i-1] += 1

    if n[0] == 10:
        n[0]= 1
        n.append(0)
    print(n)


increment_num(second_test)