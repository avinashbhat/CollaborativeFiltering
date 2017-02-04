<h1>Recommender

<h2>User-User Collaborative filtering</h2>
<br>To run, go to prompt.
<br>\>\>\> from data import critics
<br>\>\>\> from recommend import match
<br>\>\>\> match(critics,'Toby',1,n=3) 
<br>\# this uses Pearson Correlation and displays 3 results similar to Toby.
<br><br><br>
engine.py contains two recommender engines i)Euclid's distance and ii)Pearson Correlation. 
<br>data.py contains test data.
<br>recommend.py contains functions 
<br>i) match(data,person_to_be_matched,type_of_engine,no_of_results) - return the similar people based on the ratings.<br> person_to_be_matched is the person who's similar people we need to find, this is taken from the dataset.<br> type_of_engine is which engine you want to use for recommendation. 0 - Euclid's distance, 1 - Manhatten Distance, 2 - Pearson Correlation, 3 - Spearman Correlation, 4 - Cosine Distance .<br> no_of_results is the total number of similar people we need as output.
