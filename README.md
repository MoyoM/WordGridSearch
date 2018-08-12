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
The implemented solution are in this repository
Stage 1: 2D GRID OF ENGLISH ALPHABETS - https://github.com/MoyoM/WordGridSearch/word_grid.ipynb
Stage 2: SEARCH ENGLISH WORDS IN A 2D GRID - https://github.com/MoyoM/WordGridSearch/word_grid.ipynb

The Jupyter Notebooks allow interactive testing of the functionality created in this project. Test data and test runs are presented at the end
of each notebook


b) Python Modules
The implemented solution are in this repository
Stage 1: 2D GRID OF ENGLISH ALPHABETS - https://github.com/MoyoM/WordGridSearch/word_grid.py
Stage 2: SEARCH ENGLISH WORDS IN A 2D GRID - https://github.com/MoyoM/WordGridSearch/word_grid.py

Comments on the following:


Complexity of the search algorithm with N and grid dimension (1D, 2D, 3D...)?
What are some of the alternate solutions of the search problem worth exploring?
Anything else that you suggest that will make this problem/solution more interesting?
