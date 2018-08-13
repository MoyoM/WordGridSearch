from string import ascii_uppercase, ascii_lowercase
from random import choice
import numpy as np
import math

# These are functions for generating a set o K words that whose sum of letters adds up to a given sum
# equivalent to Word Density x%

def sum_sub_vect(vect, n, sum):
    """
    This function produces a subarray whose elements add up to a given sum (sum).
    vect = 1-D Array with n samples, inflated number, to choose subset from.
    n = number of elements in full array to choose from, 50 is default.
    sum = sum to achieve in subset selected.     
    """
     
    curr_sum = vect[0]
    start = 0
 
    i = 1
    while i <= n:
        
        while curr_sum  < sum:
            curr_sum = curr_sum + vect[i]
            i += 1
    
        if curr_sum == sum:
            return vect[start:i]
        else:
            curr_sum = curr_sum - vect[start]
            start += 1
         
    if i  == n & curr_sum != sum:
        return("No subarray found, increase sample size N")
    

def best_set(weights, n, sum):
    """
    This function selects the best subset that includes at least onof each unique element.
    weights = length of each word to choose from.
    In this algorithm n elements of given weights are sampled randomly over 10 times
    and the best subset is sought.
    sum = sum to be achieved in subset.
    n = number of elements to choose from, default, n=50
    """

    for iter in range(10):
        vect=np.random.choice(weights, n)
        out_set= len(set(sum_sub_vect(vect=vect,n=n, sum=sum)))
    
        if out_set == len(weights):
            break
    
    return sum_sub_vect(vect=vect,n=n, sum=sum)
        

def get_words(word_dict, n, N, x, weights=[]):
    """
    This function finds the matching words to the best subset of word lengths sampled.
    word_dict = keys are the words, values are count of letters in each word (weights)
    n = sample size large enough to sample from to get subarray with sum weights equivalent required word density(x)
    N = Grid size N*N , e.g. for 12^12 grid N is 12
    weights = 1-D array of number of letters in each word
    """
    sum = math.ceil(N*x)
    out_values=best_set(weights=weights,n=n,sum=sum)
    words_out = []
    for i in range(len(out_values)):
        words_out.append(list(word_dict.keys())[list(word_dict.values()).index(out_values[i])])
    return words_out


def write_out(file_path):
    """ This writes out words """
    with open(file_path,'w') as file:
        for item in words_for_grid:
            file.write("%s\n" % item)

