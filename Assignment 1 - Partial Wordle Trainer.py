"""
FIT2004 Assignment 1 - Partial Wordle Trainer
Author: Hee Zhan Zhynn
Student ID: 31989403
Version: 2
"""

#%% Q1
def is_anagram(alt_word, word):
    """ 
    Checks whether the two given words are anagram

    Precondition : Words are same length and in lower-case
    Postcondition: True is the two words are anagram, false otherwise

    Input:
        Two words of similar length and in lower case

    Return: 
        Words are either anagram or not
    
    eg:
    alt_word = "spare"
    word = "spear"
    is_anagram(alt_word, word)
    >>> True

    Time complexity: 
    Best : O(1) when both words are of different length
    Worst: O(M) where M is the length of word

    Space complexity: 
    Input          : O(1)
    Auxiliary Space: O(1)
    """

    #initialize count array
    TOTAL_CHARACTERS = 26 #all lower case alphabets only
    count_array = [0] * TOTAL_CHARACTERS 

    if len(alt_word) != len(word): #different length means not anagram, terminate early 
        return False

    #using a single array, increment character count from alt_word and decrement it from word
    for i in range(len(alt_word)): 
        count_array[ord(alt_word[i]) - ord('a')] += 1
        count_array[ord(word[i]) - ord('a')] -= 1
    
    #check for non-zero alphabets in count_array
    for i in range(TOTAL_CHARACTERS):
        if count_array[i] != 0:
            return False
    return True

def find_anagrams(wordlist, word):
    """
    Return a list of words from wordlist that are anagrams with the given word

    Precondition : Words are same length and in lower-case
    Postcondition: List of words are anagram with given word

    Input:
        A list of words in lower-case and of the same length

    Return: 
        An unsorted list of words that are anagrams with the given word

    eg:
    wordlist = ['limes', 'spare', 'store', 'loser', 'aster', 'pares',
                'taser', 'pears', 'stare', 'spear', 'parse', 'reaps', 'rates',
                'tears', 'losts']
    word = "spear"
    find_anagrams(wordlist, word)
    >>> ['spare', 'pares', 'pears', 'spear', 'parse', 'reaps']

    Time complexity: 
    Best : O(N) when all words in wordlist are of different length with word
    Worst: O(NM) where N is the number of words and M is the length of word

    Space complexity: 
    Input          : O(N) where N is the number of words 
    Auxiliary Space: O(N) where N is the number of words

    """
    new_list = []
    for alt_word in wordlist:
        if is_anagram(alt_word, word): 
            new_list.append(alt_word) 
    return new_list

#%% Counting Sort, remove/accept marker 
def sort_counting_alpha(new_list, col, word, marker):
    '''
    Returns a list of words that are sorted based on alphabet at specific position. The list returned is also
    the new possible words that are eligible based on the marker at the specific position.

    Precondition : Input word list must not be empty and each word must be of the same length
    Postcondition: list returned is sorted based on alphabet at specific position and contain eligible word based on marker

    Input:
        A list of words of the same length, coloumn to check, word to check against and marker

    Return: 
        A sorted list of words containing specific alphabet(s) at a given column
    
    eg:
    new_list = ['limes', 'spare', 'store', 'loser', 'aster', 'pares',
            'taser', 'pears', 'stare', 'spear', 'parse', 'reaps', 'rates',
            'tears', 'losts']
    col = 4
    word = "pears"
    marker = [1,1,1,1,0]
    sort_counting_alpha(new_list, col, word, marker)
    >>> ['spare', 'pares', 'pears', 'spear', 'parse', 'reaps']

    Time complexity: 
    Best : O(N) where N is the number of words in list
    Worst: O(N) where N is the number of words in list

    Space complexity: 
    Input          : O(N) where N is the number of words in list
    Auxiliary Space: O(N) where N is the number of words in list

    '''
    if len(new_list) == 0: #No valid words possible
        return new_list
    
    #Find the maximum
    max_item = ord(new_list[0][col]) - ord('a')
    for item in new_list: #O(N)
        char = ord(item[col]) - ord('a') 
        if char > max_item: 
            max_item = char

    #initialize stable count_array
    count_array = [None] * 26 

    #ensure new list is a separate list
    for i in range(len(count_array)): #ensure new list is a separate list
        count_array[i] = []

    #update count_array
    for item in new_list: #O(N)
        item_index = ord(item[col]) - ord('a')
        count_array[item_index].append(item) 

    #delete/return the list I want        
    index_item = ord(word[col]) - ord('a') 
    if marker[col] == 1: #letter I want
        return count_array[index_item]

    else: #letter I don't want
        count_array[index_item] = [] #delete 

    if len(count_array) > 1:
        new_list = []
        for sublist in count_array: 
            for item in sublist:    
                new_list.append(item)

    #new list will be sorted
    return new_list

#%% Radix Sort
def radix_sort_string(new_list, word, marker):
    '''
    Returns a list of words that are sorted lexicographically. The list returned is also
    the new possible words that are eligible based on the marker.

    Precondition : input word list must not be empty and each word must be of the same length
    Postcondition: list return is sorted and are valid words based on marker

    Input:
        A list of words of the same length, the word and marker to check against

    Return: 
        A sorted list of potential words based on the marker and word
    
    eg:
    new_list = ['limes', 'spare', 'store', 'loser', 'aster', 'pares',
            'taser', 'pears', 'stare', 'spear', 'parse', 'reaps', 'rates',
            'tears', 'losts']
    word = "spare"
    marker = [1,1,0,0,0]
    radix_sort_string(new_list, word, marker)
    >>> ['spear']

    Time complexity: 
    Best : O(NM) where N is the number of words in list and M the length of word
    Worst: O(NM) where N is the number of words in list and M the length of word

    Space complexity: 
    Input          : O(N) where N is the number of words in list
    Auxiliary Space: O(N) where N is the number of words in list

    '''
    max_col = len(word)
    for col in range(max_col - 1, -1, -1): 
        new_list = sort_counting_alpha(new_list, col, word, marker) 
    return new_list


#%%
def trainer(wordlist, word, marker):
    """
    Returns a lexicographically sorted list of strings containing the potential valid words, based on the input provided

    Precondition: all words in wordlist are same length and in lower case
    Postcondition: lexographically sorted list containing words with letters that could be in the correct position based on marker

    Input:
        A list of unsorted words, the guess word and a marker.

    Return:
        A lexicogrpahically sorted list of potential words that are anagram with the given word and with the correct 
        alphabets based on the marker position

    wordlist = ['limes', 'spare', 'store', 'loser', 'aster', 'pares',
            'taser', 'pears', 'stare', 'spear', 'parse', 'reaps', 'rates',
            'tears', 'losts']
    word = 'spare'
    marker = [1, 1, 0, 0, 0]
    trainer(wordlist, word, marker)
    >>> ['spear']

    Time complexity: 
        Best: O(M) when the marker indicates all correct letters and all letters are guessed correctly
        Worst: O(NM) where N is the number of words and M is the length of word
    
    Space complexity: 
        Input: O(N) where N is the number of words in list
        Aux  : O(N) where N is the number of words in list

    """
    #all correctly guessed letters
    if marker == [1] * len(word): #O(M)
        return [word]

    #get list of anagrams with word from wordlist
    new_list = find_anagrams(wordlist, word) 

    #check with marker and sort the list
    new_list = radix_sort_string(new_list,word,marker)
    return new_list