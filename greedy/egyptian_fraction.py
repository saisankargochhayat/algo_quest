# An implementation of the greedy algorithm for decomposing a fraction into an
# Egyptian fraction (a sum of distinct unit fractions).  Egyptian fractions
# are a representation of fractions that dates back at least 3500 years (the
# Rhind Mathematical Papyrus contains a table of fractions written out this
# way).  A number is expressed as an Egyptian fraction if it is written as a
# sum of unit fractions (fractions whose numerators are all zero) such that no
# fraction is duplicated.  For example, 1/2 is already an Egyptian fraction,
# but 2/3 is not.  However, 2/3 = 1/2 + 1/6 is an Egyptian fraction, though
# 2/3 = 1/3 + 1/3 is not because 1/3 is duplicated.
#
# Any rational number has at least one representation as an Egyptian fraction,
# and one simple algorithm for finding an Egyptian fraction representation of
# a rational number is given in Fibonacci's Liber Abaci (the same text that
# contains the eponymous Fibonacci sequence and the introduction of Hindu-
# Arabic numerals to Europe).  This algorithm is a greedy algorithm that works
# as follows: if the rational number already has a numerator of 1, then we are
# done.  Otherwise, subtract out the largest possible unit fraction from the
# number and repeat this process.  For example, to compute an Egyptian fraction
# representation of 42/137, we would write
#
#    42/137 = 1/4 + 31/548
#           = 1/4 + 1/18 + 5/4932
#           = 1/4 + 1/18 + 1/987 + 1/1622628

# Python3 program to print a fraction  
# in Egyptian Form using Greedy 
# Algorithm 
  
# import math package to use 
# ceiling function 
import math 
  
# define a function egyptianFraction  
# which receive parameter nr as 
# numerator and dr as denominator 
def egyptianFraction(nr, dr): 
  
    print("The Egyptian Fraction " +
          "Representation of {0}/{1} is". 
                format(nr, dr), end="\n") 
  
    # empty list ef to store 
    # denominator 
    ef = [] 
  
    # while loop runs until  
    # fraction becomes 0 i.e, 
    # numerator becomes 0 
    while nr != 0: 
  
        # taking ceiling 
        x = math.ceil(dr / nr) 
  
        # storing value in ef list 
        ef.append(x) 
  
        # updating new nr and dr 
        nr = x * nr - dr 
        dr = dr * x 
  
    # printing the values 
    for i in range(len(ef)): 
        if i != len(ef) - 1: 
            print(" 1/{0} +" .  
                    format(ef[i]), end = " ") 
        else: 
            print(" 1/{0}" . 
                    format(ef[i]), end = " ") 
  
# calling the function 
egyptianFraction(4, 17) 

