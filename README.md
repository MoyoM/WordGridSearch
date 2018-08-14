# WordGridSearch
-------------------------
About this Project
-------------------------
This project presents a coding solution for implementing alogorithms to create a word grid and to search for give words in that grid in answe to to
the problem statetement below.

-------------------------
Problem Statement:
-------------------------

Consider below, a 2-dimensional grid of 10 x 10 cells consisting of a single English alphabet per cell. Some combinations of the alphabets in the grid (horizontally, vertically and diagonally) makes up English words (like CAT, DOG, MONKEY).


This coding challenge is made up of two stages:

Stage 1: 2D GRID OF ENGLISH ALPHABETS

Write an algorithm that will stepwise:


Create a 2D square grid of size N.
Generate a list of k English words (with or without repetition), such that it fills up ~ x% (Grid word density) of the cells (In the example above, the animal names cat, cat, dog, monkey makes up 15% of the total no of cells).
Place the generated words in the grid at random locations, vertically (V), horizontally (H) or diagonally (D) with the placement probability distribution: P(V)=p_1, P(H)=p_2, P(D)=p_3.

A square grid of alphabets.
A set of unique English words that are present inside the grid.


Stage 2: SEARCH ENGLISH WORDS IN A 2D GRID

Given a 2D alphabet grid and a set of unique words present in the grid, Write an algorithm, that will:

Search for all occurrences of the input words in the grid.

The output of this program for the example grid:

'CAT' Found at (0, 0) in Horizontal direction

'DOG' Found at (3, 1) in Vertical direction

'CAT' Found at (6, 4) in Vertical direction

'MONKEY' Found at (0, 4) in Diagonal direction

------------------------------------------------
implemented solution
------------------------------------------------
a) Juypter notebooks
The implemented solutions are in this repository
Stage 1: 2D GRID OF ENGLISH ALPHABETS -
https://github.com/MoyoM/WordGridSearch/blob/master/Notebooks/word_list_generation.ipynb

Stage 2: SEARCH ENGLISH WORDS IN A 2D GRID - 
https://github.com/MoyoM/WordGridSearch/word_grid.ipynb

The Jupyter Notebooks allow interactive testing of the functionality created in this project. Test data and test runs
are presented at the end of each notebook


b) Python Modules for REST API implementation
The implemented solution modules for an API productionizatio are in this repository
Stage 1: 2D GRID OF ENGLISH ALPHABETS - 
https://github.com/MoyoM/WordGridSearch/blob/master/API/Model/word_list.py ;
https://github.com/MoyoM/WordGridSearch/blob/master/API/Model/WordGrid.py

Stage 2: SEARCH ENGLISH WORDS IN A 2D GRID -
https://github.com/MoyoM/WordGridSearch/blob/master/API/Model/WordGrid.py
This has the Class implementation for bonus points.

REST API
https://github.com/MoyoM/WordGridSearch/blob/master/API/wordgrid_serve_api.py

The model server side of the API is created in this code. The code addresses parametisation by N (Grid Size),
x% (Word Density) and P (Orientation probabilities).

The code structure is presented. More effort will be required to stepwise test and amke this work by implementinga
Postman Client Server side.


-------------------------
Comments on the following:
-------------------------

Complexity of the search algorithm with N and grid dimension (1D, 2D, 3D...)?

The agorithm used here starts on a coordinate (x,y) and searches in d directions
for the word.The algorithm is linear on O(1) the cost of locating one letter in the grid for 
a 2D array. The cost on time for n words of length w searched for in d directions will be O(nwd).

N

So as N increases the algorithm cost will increase linearly with increase in N. Here N is taken 
as grid size, there N start positions initiaited in bigger N compared to O(1) are initiated.
However a an improvisation of the algorithm can search for the first letter of a word first and then 
seach for the word. Though still linear it should be less than O(nwd) typically it could
be O(n) {first letter search) + O(wd) {word length in d directions)

3D

Since a 3D array is an array of 2D arrays (array size [n1][n2][n3] is n3 of [n1][n2] arrays)
The cost for a 3D array compared to a 2D array should be n(O(nwd)). The cost increases n times
that of a 2D array.



What are some of the alternate solutions of the search problem worth exploring?
Anything else that you suggest that will make this problem/solution more interesting?


