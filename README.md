# recommender

<h2>User-User Collaborative filtering</h2>

To run, go to prompt.

>>> from data import critics
>>> from recommend import match
>>> match(critics,'Toby',1,n=3) 
this uses Pearson Correlation and displays 3 results similar to Toby.

engine.py contains two recommender engines i)Euclid's distance and ii)Pearson Correlation. 

data.py contains test data.

recommend.py contains functions 

i)match(data,person_to_be_matched,type_of_engine,no_of_results) - return the similar people based on the ratings. person_to_be_matched is the person who's similar people we need to find, this is taken from the dataset. type_of_engine is which engine you want to use for recommendation. 0 - Euclid's distance, 1 - Pearson Correlation. no_of_results is the total number of similar people we need as output.
