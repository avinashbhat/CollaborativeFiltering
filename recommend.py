#from data import critics
from engines import pearson, euclid, spearman, manhatten, cosine
# n is how many results you want 
# sim is the similarity function you want to use
def recommend_user(data,person,e,n=5):

	if e == 0:
		sim = euclid
	elif e == 1:
		sim = manhatten
	elif e == 2:
		sim = pearson
	elif e == 3:
		sim = spearman
	elif e == 4:
		sim = cosine

	s = []
	for people in data:
		#print people
		if people != person:
			s.append((sim(data,person,people),people))
	s.sort()
	s.reverse()
	# Return the best n results
	return s[0:n]

#m = match(critics,'Toby',1,n=3)
#print m