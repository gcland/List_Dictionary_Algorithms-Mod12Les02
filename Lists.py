import time
import random
# Advanced Operations on Python Lists

# 1.1 

# Implement a function to create a new list using list comprehension that contains squares of numbers from 1 to n, 
# where n is a parameter. Analyze the time and space complexity of this operation.

def squares(n):
    start_time = time.time()
    list = [(i**2)for i in range(1, n)]
    end_time = time.time()
    result_time = end_time - start_time
    formatted_time = f'{result_time:.10f}'
    # print(list)
    print(formatted_time)

# squares(100000000)

# Time complexity:
# n = 
# 10 -> ~ 0.0000009537s
# 1,000 -> ~ 0.0000371933s
# 100,000 -> ~ 0.0038070679s
# 100,000,000 -> ~ 3.7898328304s

# This is a lienar time complexity
# This matches the doucmentation which says list operation: Set Item is O(n) - (avg and worst-case)

# The space complexity of this function is O(1) because i and list are the only variables in the function. 
# i changes and is added to the end of the list



# 1.2 

# Implement a function to reverse a sublist within a list from index i to j (inclusive). 
# Analyze the time and space complexity of this operation


def reverse_sublist(list, i, j):
    start_time = time.time()
    j+=1 # because j needs to be inclusive per assignment requirements
    subList = list[i:j]
    print('Sublist (unsorted):', subList)
    subList.sort()
    print('Sublist (sorted):', subList)
    reverse_sublist = list[:i]+subList+list[j:]
    end_time = time.time()
    result_time = end_time - start_time
    formatted_time = f'{result_time:.10f}'
    print(reverse_sublist)
    print('Time to reverse sublist:',formatted_time)
    print(i, j)


i = random.randint(0,1000)
j = random.randint(0,1000)
if i > j:
    i = random.randint(0,j)

list = []
for n in range(100000):
    n = random.randint(0,1000)
    list.append(n)

# reverse_sublist(list, i, j)

# Time complexity
# This is a linear time complexity because the function has operations to slice (loop through and stop slice at index location)

# Space complexity 
# The space complexity appears linear because the larger the list the larger the independent sublists the system must hold. 
# However, this only appears linear because the three combined sublists will always equate to the size of the original list


# 1.3

# Implement a function to merge two sorted lists into a single sorted list. 
# Analyze the time and space complexity of this operation.

def merge_lists(list1, list2):
    combinedList = []
    start_time = time.time()
    combinedList.append(list1)
    combinedList.append(list2) # initially preserves order (list1) -> order (list2)
    # list1+list2 is O(n) time and space complexity because the + operator goes through every element in the list
    combinedList.sort() # .sort() uses Timsort
    end_time = time.time()
    result_time = end_time - start_time
    formatted_time = f'{result_time:.10f}'
    print(combinedList)
    print(formatted_time)


list1 = []
list2 = []
for n in range(100):
    n = random.randint(0,1000)
    list1.append(n)
    n = random.randint(0,1000)
    list2.append(n)

merge_lists(list1, list2) # approx time 0.0000020s

# Time complexity
# Python's sort method uses Timsort which uses both binary insertion sort and merge sort to sort a list in an 
# average time and worst case time of O(n logn). Best case the time is lienar O(n)

# Space complexity 
# The space complexity of this function is O(n) because a new list is created that is the sum of the two lists. 
