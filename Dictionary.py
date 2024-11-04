import time
# Dictionary Manipulation and Optimization

# 2.1

# Implement a function to merge two dictionaries, preserving the values of common keys from the second dictionary. 
# Analyze the time and space complexity of this operation.

def merge_dictionaries(dict1, dict2):
    for key in dict2:
        if key in dict1:
            dict1[key]+=dict2[key]
        else:
            dict1[key]=dict2[key]
    print(dict1)

def merge_dictionariesB(dict3, dict4):
    dict5 = {}
    for key in dict3:
        dict5[key] = dict3[key]
    for key in dict4:
        if key in dict5:
            dict5[key]+=dict4[key]
        else:
            dict5[key]=dict4[key]
    print(dict5)


dict1 = {
    'A': 1,
    'B': 0,
    'C': '123',
    'D': '098'
}

dict2 = {
    'A': 4,
    'E': 0,
    'C': '456',
    'F': '098'
}

merge_dictionaries(dict1, dict2) # does not perserve both dictionaries

# time complexity

# The space complexity 

dict3 = {
    'A': 1,
    'B': 0,
    'C': '123',
    'D': '098'
}

dict4 = {
    'A': 4,
    'E': 0,
    'C': '456',
    'F': '098'
}

merge_dictionariesB(dict3, dict4) # preserves both dictionaries, creates new dictionary

# Time complexity
# The time complexity of this function is O(n^2) because we are required to loop through dict1 for a key in dict2.
# This requires looping though dict2 to find (or not find) the key in the first loop (through dict1)
# Note: in the 'merge_dictionariesB' function where the original dictionaries are preserved and a new dictionary is created,
# the time complexity is still O(n^2) but since there are two foor loops to check each dictionary, the time complexity is 2*O(n^2)

# Space complexity 
# If we do not preserve the original dictionaries, this is a constant space complexity
# If we do preserve the original dictionary, this is a linear space complexity because we are adding a new dictionary 
# with key-value pairs




# 2.2 

# Implement a function to find the intersection of two dictionaries, i.e., 
# keys common to both dictionaries along with their values. Analyze the time and space complexity of this operation.

def intersection(dict1, dict2):
    dict3 = {}
    for key in dict1:
        if key in dict2:
            dict3[key] = {'dict1':dict1[key]}, {'dict2':dict2[key]}
    print(dict3)

dict1 = {
    'A': 1,
    'B': 0,
    'C': '123',
    'D': '098'
}

dict2 = {
    'A': 4,
    'E': 0,
    'C': '456',
    'F': '098'
}

# intersection(dict1, dict2)

# Time complexity
# The time complexity of this function is O(n^2) because we are required to loop through dict1 for a key in dict2.
# This requires looping though dict2 to find (or not find) the key in the first loop (through dict1)

# Space complexity 
# This is a linear space complexity because we are adding a new dictionary with key-value pairs



# 2.3 

# Implement a function to count the frequency of each unique word in a list using a dictionary. 
# Analyze the time and space complexity of this operation.

def word_frequency(wordsList):
    print('Initial words list:', wordsList)
    uniqueWords = {}
    for word in wordsList:
        if word in uniqueWords:
            uniqueWords[word] += 1
        else:
            uniqueWords[word] = 1

    print('Unique words dictionary:',uniqueWords)


# words = 'She sells sea shells by the sea shore'
words = 'hi hi hi hi yes yes yes no okay'
words = 'a a a b b b z z z 1 2 3 4 1 2 3 4'
wordsList = words.split()

# word_frequency(wordsList)

# Time complexity
# This is a linear time complexity because the for loop must check every word within the list which grows linearly 
# as the list grows.

# Space complexity 
# This is a linear space complexity because a dictionary is generated and a new key or a new value is generated with 
# every list word. As the list grows the dictionary grows linearly.