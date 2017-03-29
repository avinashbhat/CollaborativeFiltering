from engines import pearson, euclid, spearman, manhatten, cosine#, centered_cosine
from data import loadData

# User - User CF
# n is how many results you want 
# sim is the similarity function you want to use
# person is the person or movie whose similar one we need to find
# function to find similar user or movie, user - user prediction
def similar_people(data,person,e,n=5):

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
		if people != person:
			s.append((sim(data,person,people),people))
	s.sort()
	s.reverse()
	# Return the best n results
	return s[0:n]


# A function to recommend movies, user - item prediction
# Using weighted averages

def recommend_item(data,person,e):
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
	elif e == 5:
		sim = centered_cosine
	rec_m = {}
	simsum = {}
	for people in data:
		if people != person:
			s = sim(data,person,people)
		if s > 0:
			for movie in data[people]:
				#if movie not in data[person]:
				rec_m.setdefault(movie,0)
				rec_m[movie] += data[people][movie]*s
				simsum.setdefault(movie,0)
				simsum[movie] += s
	ranking = []
		# After normalizing
	for movie in rec_m:
		ranking.append((rec_m[movie]/simsum[movie],movie))
	ranking.sort()
	ranking.reverse()

# A function to convert the data for input to item based
def transform_data(data):
	result = {}
	for person in data:
		for item in data[person]:
			result.setdefault(item,{})
			result[item][person] = data[person][item]

	return result

# Item - item CF
# A function to decide the data
def calculateSimilarityMatrix(data, n = 5):
	matrix = {}
	itemData = transform_data(data)
	'''print itemData
	print '\n'
	print '\n'''
	count = 0
	for item in itemData:
		count += 1
		'''if count%100 == 0:
			print (count,len(itemData))
		else:
			print (count,len(itemData))'''
		scores = similar_people(itemData, item, 2, n)
		matrix[item] = {}
		for each in scores:
			matrix[item][each[1]] = each[0]

	return matrix
data = loadData()
itemBased = calculateSimilarityMatrix(data)
#print itemBased


def getItemRecommmendations(data, itemMatch, person):
	userRating = data[person]
	scores = {}
	totalSimilarity = {}
	for each in itemMatch:
		if each not in userRating:
			for item in userRating:
				#print (each, item)
				if item in itemMatch[each]:
					#print itemMatch[each][item]
					scores.setdefault(each,0)
					scores[each] += itemMatch[each][item]*userRating[item]
					totalSimilarity.setdefault(each,0)
					totalSimilarity[each] += itemMatch[each][item]
	ranking = []
	for item,score in scores.items():
		ranking.append((score/totalSimilarity[item], item))
		#print (score/totalSimilarity[item], item)

	#ranking = [(scores/totalSimilarity[item], item) for item, score in scores.items()]
	ranking.sort(reverse = True)
	return ranking

r = getItemRecommmendations(data, itemBased, '452')	
print r[0:5]