
# coding: utf-8

# In[2]:


from string import ascii_uppercase, ascii_lowercase
from random import choice
import numpy as np
import math


# ### functions for generating a set o K words that whose sum of letters adds up to a given sum

# In[3]:


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
    


# In[4]:


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
        


# In[5]:


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


# In[6]:


def write_out(file_path):
    """ This writes out words """
    with open(file_path,'w') as file:
        for item in words_for_grid:
            file.write("%s\n" % item)


# ### tests

# In[7]:


test = np.random.choice([4,5,7,5,3],50, p=[0.1, 0.2, 0.3, 0.2, 0.2])
test


# In[8]:


sum_sub_vect(test,50, 30)


# In[9]:


out_values=best_set(weights=[5,3,7], n=50, sum=30)


# In[10]:


out_values


# ## STAGE 1 SOLUTION 
# 

# Generation of a list of words that occupy  25%  (x%) of Grid.
# -------------------------------------------------------------
# 25% of a 12X12 Grid is 36. 
# A set of words that add to 36 words letters were selected using 'sum_sub_vector', 'best_set' and 'get_words' methods in this module.
# 
# Summary of solution
# -------------------
# A set of words that give this sum of letters equivalent to x% f grid is generated.
# The best is selected as the set that contains at least on of each word.
# Possible limitations and extensions to the approach I used are:
# a) I chose a words with unique lengths and used length size to identify the frequency of
# the given words by matching the lengths in an array of lengths that adds up to N*x%, the required
# word density.
# If a set of different words with same length are chosen, in this current code, this may lead to problems
# identifying which words where chosen to satisfy the Word Density constraint.
# However any words matching the length requirements can still be used. Alternatively a method to place words 
# with same length with different probabilities can be employed. This will be one among other posible solutions depending on use case needs for the project.
# b) At some point x%, the Word Density, may not be accomodated as there may not be enough empty spaces in the grid to
# fill with chosen words. At this time the limit in empty spaces in Grid as x% tends to increase to 100% has not been explored.
# One possible solution will be to create an exception in the algorithm for adding words when no empty spaces are available for chosen words.

# In[11]:


words_for_grid = get_words(word_dict = {'HOUSE':5,'DOG':3, 'KITCHEN':7}, weights=[5,3,7], n=50, N=144, x=0.25)


# In[12]:


words_for_grid


# In[13]:


write_out("words_for_grid_at_density_x.txt")


# In[14]:


# test that the word set produced has 36 letters to fill 25% Grid as designed


# In[15]:


0.25*144


# In[16]:


letters=0
for letter in ''.join(words_for_grid):
    letters +=1
letters


# In[17]:


# prepare python script to import into other modules


# In[18]:


get_ipython().system('jupyter nbconvert --to script word_list_generation.ipynb')

