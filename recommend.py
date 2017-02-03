#from data import critics
from engines import pearson, euclid, spearman
# n is how many results you want 
# sim is the similarity function you want to use
def match(data,person,e,n=5):

	if e == 0:
		sim = euclid
	elif e == 1:
		sim = pearson
	elif e == 2:
		sim = spearman

	s = []
	for people in data:
		#print people
		if people != person:
			s.append((sim(data,person,people),people))
	s.sort()
	if e == 1 or e == 2:
		s.reverse()
	# Return the best n results
	return s[0:n]

#m = match(critics,'Toby',1,n=3)
#print m