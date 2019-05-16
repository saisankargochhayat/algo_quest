import math
    # math.acos(x) is the arccosine of x.
    # math.sqrt(x) is the square root of x.

import sys

def read_file(filename):
    """ 
    Read the text file with the given filename;
    return a list of the lines of text in the file.
    """
    try:
        f = open(filename, 'r')
        return f.readlines()
    except IOError:
        print("Error opening or reading input file: ",filename)
        sys.exit()

def get_words_from_line_list(L):
    """
    Parse the given list L of text lines into words.
    Return list of all words found.
    """
    word_list = []
    for line in L:
        words_in_line = get_words_from_string(line)
        #extend is more efficient than concatenation
        word_list.extend(words_in_line)
    return word_list

def get_words_from_string(line):
    """
    Return a list of the words in the given input string,
    converting each word to lower-case.

    Input:  line (a string)
    Output: a list of strings 
              (each string is a sequence of alphanumeric characters)
    """
    word_list = []          # accumulates words in line
    character_list = []     # accumulates characters in word
    for c in line:
        if c.isalnum():
            character_list.append(c)
        elif len(character_list)>0:
            word = "".join(character_list)
            word = word.lower()
            word_list.append(word)
            character_list = []
    if len(character_list)>0:
        word = "".join(character_list)
        word = word.lower()
        word_list.append(word)
    return word_list

def count_frequency(word_list):
    """
    Return a list giving pairs of form: (word,frequency)
    """
    D = {}
    for new_word in word_list:
        if new_word in D:
            D[new_word] = D[new_word]+1
        else:
            D[new_word] = 1
    #print(D.iteritems())
    return list(D.items())

def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>-1 and A[i]>key:
            A[i+1]=A[i]
            i = i-1
        A[i+1]=key
    return A

def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>-1 and A[i]>key:
            A[i+1]=A[i]
            i = i-1
        A[i+1]=key
    return A


def word_frequencies_for_file(filename):
    """
    Return alphabetically sorted list of (word,frequency) pairs 
    for the given file.
    """
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)
    insertion_sort(freq_mapping)
    #print(freq_mapping)
    return freq_mapping

# def inner_product(L1,L2):
#     """
#     Inner product between two vectors, where vectors
#     are represented as lists of (word,freq) pairs.

#     Example: inner_product([["and",3],["of",2],["the",5]],
#                            [["and",4],["in",1],["of",1],["this",2]]) = 14.0 
#     """
#     sum = 0.0
#     for word1, count1 in L1:
#         for word2, count2 in L2:
#             if word1 == word2:
#                 sum += count1 * count2
#     return sum

def inner_product(L1,L2):
    sum = 0.0
    i = 0
    j = 0
    while (i<len(L1)) and (j<len(L2)):
        if L1[i][0] == L2[j][0]:
            sum += L1[i][1] * L2[j][1]
            i+=1
            j+=1
        elif L1[i][0] < L2[j][0]:
            i += 1
        else:
            j += 1
    return sum


def vector_angle(L1,L2):
    """
    The input is a list of (word,freq) pairs, sorted alphabetically.

    Return the angle between these two vectors.
    """
    numerator = inner_product(L1,L2)
    denominator = math.sqrt(inner_product(L1,L1)*inner_product(L2,L2))
    return math.acos(numerator/denominator)

def main():
    if len(sys.argv) != 3:
        print("Usage: docdist1.py filename_1 filename_2")
    else:
        filename_1 = sys.argv[1]
        filename_2 = sys.argv[2]
        sorted_word_list_1 = word_frequencies_for_file(filename_1)
        sorted_word_list_2 = word_frequencies_for_file(filename_2)
        distance = vector_angle(sorted_word_list_1,sorted_word_list_2)
        print("The distance between the documents is: %0.6f (radians)"%distance)

if __name__ == "__main__":
    import cProfile
    cProfile.run("main()")
