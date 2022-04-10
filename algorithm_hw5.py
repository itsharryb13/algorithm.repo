# ###############################################
# Selection Sort
# Implement the selection sort algorithm that is sorting in descending order.
#
# Bubble Sort
# Implement the bubble sort algorithm that is sorting in descending order.
#
# Insertion Sort
# Implement the insertion sort algorithm that is sorting in descending order.
#
# Merge Sort
# Implement the merge sort algorithm that is sorting in descending order.
#########################################################################

basic_case = [4,10,9,19,20,70,50,49,72,81,0]

##########################################################################
Selection Sort
def decend_selec(n):
    for i in range(0,len(n)-1):
        min = i
        for y in range(i+1,len(n)):
            if(n[y] > n[min]):
                min = y
        n[i], n[min] = n[min], n[i]
m = basic_case.copy()
decend_selec(m)
print(m)

####################################################################################
#Bubble Sort

def decend_bubble(n):
    for i in range(len(n)):
        for y in range(0, (len(n)-i)-1):
            if (n[y] < n[y+1]):
                n[y], n[y+1] = n[y+1], n[y]


m2 = basic_case.copy()
decend_bubble(m2)
print(m2)

####################################################################################
#Insertion Sort

def decend_insert(n):
    for i in range(1,len(n)):
        point = n[i]
        y = i - 1
        while y >= 0 and point > n[y]:
            n[y+1] = n[y]
            y = y - 1
            n[y+1] = point


m3 = basic_case.copy()
decend_insert(m3)
print(m3)

####################################################################################
#Merge Sort


def decend_merge(arr):
    if len(arr) > 1:
        q = len(arr) // 2
        L = arr[q:]
        R = arr[:q]

        decend_merge(L)
        decend_merge(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i > len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j > len(R):
            arr[k] = R[j]
            j += 1
            k += 1


m4 = basic_case.copy()
decend_merge(m4)
print(m4)
