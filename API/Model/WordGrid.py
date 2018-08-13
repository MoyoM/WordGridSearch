
# coding: utf-8

# In[5]:


from string import ascii_uppercase, ascii_lowercase
from random import choice
import numpy as np
import word_list_generation as wlg


# ### Grid Class and its methods

# A Class called Grid is created. The class creates a word grid and has methods to operate on this grid

# In[6]:


class Grid:
    
    def __init__(self, N):
        self.N = N
        
    def create_grid(self):
        '''This function creates an empty grid of NXN size.
        '''
        grid = []
        for row in range(self.N):
            grid.append([])
            for col in range(self.N):
                grid[row].append('.')
        return grid
    
    def print_grid(self, grid):
        '''
        Print grid
        '''
        for row in grid:
            print(' '.join(row))

    def count_spaces(self, grid, direction, word_len, start_row, start_col):
        '''
        This functions counts spaces available in the direction from selected
        coordinates start_row and start_col. This is used to control for placement of words in grid.
        Words are not placed if there is no space in the given direction.
        direction = 'H','V','D' for Horizontal, Vertical and Diagonal
        word_len = length of word to be placed
        start_row = starting row coordinate of placement
        start_col = starting col coordinate of placement
        
        '''
        if direction == 'H':
            spaces = grid[start_row][start_col:(start_col+word_len)].count('.')
        if direction == 'V':
            spaces = 0
            for i in range(word_len):
                spaces += grid[start_row+i][start_col].count('.')
        if direction == 'D':
            spaces = 0
            for i in range(word_len):
                spaces +=grid[start_row+i][start_col+i].count('.')
        return spaces

    def check_empty_spaces(self, grid):
        '''
        This counts empty spaces in grid.
        '''
        empty_spaces=0
        for row in grid:
            empty_spaces += row.count('.')
        return empty_spaces
    
    
   
    def add_word(self, grid,word, P=[]):
        '''
        Adds word with probability vector P=[P(H),P(V),P(D)].
        H,V,D = Horizontal, Vertical , Diagonal
        '''
        word_len = len(word)

        first_empty = self.check_empty_spaces(grid)
        last_empty = first_empty

        while last_empty == first_empty:
            #start empty spaces
            first_empty = self.check_empty_spaces(grid)

            #random start positions
            start_row = np.random.randint(0,(self.N-1))
            start_col = np.random.randint(0,(self.N-1))


            ## sample direction   
            direction_set=['H', 'V','D']
            #direction Horizontal=0, Vertical=1, Diagonal=1
            direction_ind=np.random.choice(a=range(len(P)),size=1,p=P)
            direction=direction_set[int(direction_ind)]



            if direction=='H':
                if (start_col+word_len+1) > self.N: 
                    start_col = self.N - word_len
                else:
                    start_col = start_col

                spaces_h = self.count_spaces(grid,direction='H',word_len=word_len,start_row=start_row,start_col=start_col)

                if spaces_h == word_len:            
                    for letter in word:
                        for i in range(word_len):
                            grid[start_row][start_col+i]=word[i]


            elif direction=='V':
                if (start_row+word_len+1) > self.N: 
                    start_row = self.N - word_len
                else:
                    start_row = start_row

                spaces_v = self.count_spaces(grid,direction='V',word_len=word_len,start_row=start_row,start_col=start_col)

                if spaces_v == word_len:        
                    for letter in word:
                        for i in range(word_len):
                            grid[start_row+i][start_col]=word[i]

            elif direction=='D':
                if (start_col+word_len+1) > self.N: 
                    start_col = self.N - word_len
                else:
                    start_col = start_col
                if (start_row+word_len+1) > self.N: 
                    start_row = self.N - word_len
                else:
                    start_row = start_row

                spaces_d = self.count_spaces(grid,direction='D',word_len=word_len,start_row=start_row,start_col=start_col)

                if spaces_d == word_len:            
                    for letter in word:
                        for i in range(word_len):
                            grid[start_row+i][start_col+i]=word[i]
            else:            
                Pass

            #check word added
            last_empty = self.check_empty_spaces(grid)
            

        return first_empty,last_empty
    
    
    def add_words_multi(self,grid,word,words_vec,P=[]):
    
        """ 
        This function adds words as generated from word_list_generation module as a 1-D array.
        grid = grid object from Grid.create_grid method
        word = word to enter into grid
        word_dict = keys are the words, values are count of letters in each word (weights)
        n = sample size large enough to sample from to get subarray with sum weights equivalent to required word density(x)
        N passed from self.N is Grid size N*N , e.g. for 12^12 grid N is 12
        weights = 1-D array of number of letters in each word
        P = 1-D array of placement probability to Horizontal, Vertical , Diagonal position
        """
        words_for_grid = words_vec
        for times in range(words_for_grid.count(word)):
            self.add_word(grid=grid,word=word,P=P)
        
        self.print_grid(grid)
        
        
        
    def fill_up_grid(self,grid):
        '''
        Fills up empty spaces in grid with random letters
        '''
        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col] =='.':
                    grid[row][col]=str(choice(ascii_uppercase))
        self.print_grid(grid)
        
        
    def word_search(self, grid, word):
        '''
        This function searches for a given word in the grid. It returns the starting coordinates of
        word and the direction it is placed in.
        '''

        word_len = len(word)

        #horizontal
        for row in  range(len(grid)):
            for col in range(len(grid)):

                any_word = []

                #horizontal
                for n in range(word_len):
                    if (0 <= col + word_len - 1 < len(grid)):
                        any_word += grid[row][col + n ]
                        if word == ''.join(any_word):
                            print("%s Found at (%d,%d)  in Horizontal direction" % (word,row,col))
                            continue
                        continue


        #vertical

        for row in  range(len(grid)):
            for col in range(len(grid)):
                any_word = []

            #vertical
                for n in range(word_len):
                    if (0 <= row + word_len - 1  < len(grid)):
                        any_word += grid[row + n][col]
                        if word == ''.join(any_word):
                            print("%s Found at (%d,%d)  in Vertical direction" % (word,row,col))
                            continue
                    continue

     #diagonal
        for row in  range(len(grid)):
            for col in range(len(grid)):
                any_word = []

                #diagonal
                for n in range(word_len):
                    if (0 <= row + word_len - 1  < len(grid) and 0 <= col + word_len - 1 < len(grid)):
                        any_word += grid[row + n][col + n ]
                        if word == ''.join(any_word):
                            print("%s Found at (%d,%d)  in Diagonal direction" % (word,row,col))
                            continue
                    else:
                        pass



# ### Test key functions

# In[7]:


grid= Grid(12)


# In[8]:


my_grid=grid.create_grid()


# In[9]:


grid.print_grid(my_grid)


# In[10]:


grid.count_spaces(my_grid,'H',7,0,0)


# In[11]:


grid.add_word(my_grid,'HOUSE',[0.3,0.3,0.4])


# In[12]:


grid.print_grid(my_grid)


# ## STAGE 1 SOLUTION

# Create a Grid Filled with specific words
# ------------------------------------------
# 
# This the part of solution that creates a grid and add words to grid. A 12X12 grid is created in this work.
# Please note - The first part of solution genearating words for a given WordDensity x% is presented  the in word_list_generation notebook/module. This module is imported into this module to add functionality to given methods.
# 
# The words chosen for this work are 'HOUSE','DOG','KITCHEN'.
# 
# The words are added to grid to fill 25% of the 12X12 cells in grid. Each word is placed in grid with a set probability 
# for Horizontal, Vertical, Diagonal placement. Here these probabilities are P=[0.3,0.4,0.3] consecutively.

# a) Empty 12X12 grid created

# In[13]:


my_grid=grid.create_grid()


# In[14]:


grid.print_grid(my_grid)


# b) Generate words that fill 25% of 12X12 grid are generated from word_list_generation module

# In[15]:


words_for_grid = wlg.get_words(word_dict = {'HOUSE':5,'DOG':3, 'KITCHEN':7}, weights=[5,3,7], n=50, N=144, x=0.25)


# In[16]:


words_for_grid


# c) Place words selected with different probabilities of being placed Horizontally, Vertically and Diagonally -> P

# In[17]:


P=[0.3,0.4,0.3]


# In[18]:


grid.add_words_multi(my_grid,'KITCHEN',words_for_grid, P)


# In[19]:


grid.add_words_multi(my_grid,'HOUSE',words_for_grid, P)


# d) All words placed in grid to occupy 36 cells (25%) of 12X12 grid

# In[20]:


grid.add_words_multi(my_grid,'DOG',words_for_grid, P)


# e) Rest of grid filled with random letters

# In[21]:


grid.fill_up_grid(my_grid)


# ## Search For Words in Grid

# In[22]:


grid.word_search(my_grid, 'HOUSE')


# In[23]:


grid.word_search(my_grid, 'DOG')


# In[24]:


grid.word_search(my_grid, 'KITCHEN')


# In[26]:


get_ipython().system('jupyter nbconvert --to script WordGrid.ipynb')

