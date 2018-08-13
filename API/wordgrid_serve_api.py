# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 20:08:02 2018

@author: mphat

This script executes a Flask API
Calls to API can create a new grid and search from it.
The API is Parametised with follwing requests received from client server
D - length of square grid, N = D*D
x% - word density required for filling words
P1,P2,P3 -probabilty of word placement Horizontally,Vertically and Diagonally 
Only 3 words for filling in grid are allowed in present API
"""

from flask import Flask
from flask import request, jsonify
import requests
import Model.word_list as word_list
import Model.WordGrid as WordGrid

app = Flask(__name__)
app.config["DEBUG"]=True

#data input expected
#some test data to be received from client server
#data is received and collected into list
#only 3 words are allowed in present API
#D is dimension of Grid of DXD
#x is word density for selected words
#P1,P2,P3 are probabilities of word placement in Horizontal,Vertical and Diagonal 
#directions

data_eg={'word1': 'CAT','word2': 'DOG','word3' :'HOUSE','D' : 12,
         'x' : 0.25, 'P1' : 0.2,'P2' : 0.3,'P3': 0.4}
             

@app.route('/', methods=['GET'])
def home():
    return "<h1>Word Grid and Search</h><p>This site is a prototype API for creating word grids and word search from created grids</p>"


@app.route('/creategrid', methods=['POST'])
def api_create_grid():
    """API Call

    string of parameters from API Call
    """
    params = requests.get_json()
    
    word1=params['word1']
    word2=params['word2']
    word3=params['word3']
    D=params['dimension']
    x=params['density']
    P1=params['p1']
    P2=params['p2']
    P3=params['p3']
    
    N = D*D
    words = [word1, word2, word3]
    P = [P1,P2,P3]

    # create grid DXD 
    grid = WordGrid.Grid(D)
    my_grid = WordGrid.grid.create_grid()
    #need to figure out how to store this grid for searches in
    #susbequent API calls below
    
                     
    def create_dict(words):
        word_dict = {}
        for word in words:
            word_dict[word] = len(word)
        weights = list(word_dict.values())
        return word_dict, weights

    word_dict, weights = create_dict(words)

    #sample list of words equal to density x%
    # n is size of random samples created to select subset of x%,default set at 50
    words_for_grid = word_list.get_words(word_dict=word_dict, weights=weights, n=50, N=N, x=x)

    words_out = ' '.join(words_for_grid)
    
    #enter words in grid with probability vector P
    for word in words:
        grid.add_words_multi(my_grid,word,words_for_grid,P)
    
    grid.fill_up_grid(my_grid)
    
    #return list of words that were entered in grid
    return jsonify(words_out)


@app.route('/findwords', methods=['POST'])
def api_word_search():
    #Assumes the previous grid has been stored
    #And search is on this grid
    
    findwords = requests.get_json().keys()
    
    results= []
    for word in findwords:
        results.append(grid.word_search(my_grid, word))
    
    return jsonify(results)


app.run()