# Takes 3 parameters, data, names
def euclid(data,pone,ptwo):
	# Get what items are shared between two people
	shared = {}
	total = 0 
	#print shared
	for movie in data[pone]:
		if movie in data[ptwo]:
			shared[movie] = 1
			# Calculate using Euclid's formula
			total += (data[pone][movie]-data[ptwo][movie])**2

		#print shared

	# If nothing common return 0
	if len(shared) == 0:
		return 0;

	#print shared
	# Return
	return 1/(1+total)

#d = euclidDistance(critics,'Lisa Rose', 'Gene Seymour')
#print d
#-----------------------------------------------------------------------------------------------------------------------
'''def manhatten(data,pone,ptwo):
	shared = {}
	total = 0
	for movie in data[pone]:
		if movie in data[ptwo]:
			shared[movie] = 1
			total += ()'''
#-----------------------------------------------------------------------------------------------------------------------

def pearson(data,pone,ptwo):
	shared = {}
	p1sum = p1sq = 0
	p2sum = p2sq = 0
	prodsum = 0
	for movie in data[pone]:
		if movie in data[ptwo]:
			shared[movie] = 1
			p1sum += data[pone][movie]
			p1sq += data[pone][movie]**2
			p2sum += data[ptwo][movie]
			p2sq += data[ptwo][movie]**2
			prodsum += data[pone][movie]*data[ptwo][movie]

	length = len(shared)
	if length == 0:
		return 0

	temp = prodsum - ((p1sum*p2sum)/length)
	value = ((p1sq-(p1sum**2/length))*(p2sq-(p2sum**2/length)))**0.5
	if value == 0:
		return 0
	else:
		return temp/value

#p = pearson(critics,'Lisa Rose', 'Gene Seymour')
#print p
#-----------------------------------------------------------------------------------------------------------------------
# A function to assign ranks and sort
#	the rankings
def spearman_sort(l):
	l = [[k,v] for k,v in l.items()]
	l.sort(key=lambda l:l[1])
	index = 1
	for each in l:
		each[1] = index
		index += 1
	l.sort()
	return l

''' Spearman Correlation algorithm
		1) Find scores of each object
		2) Calculate ranks for each object
		3) Find the difference between ranks,
			to verify - sum of ranks should be 0
		4) Calculate sum of squares of ranks
		5) Calculate Spearman r = 1 - (6*summ(d**2)/n(n**2-1)) '''
def spearman(data,pone,ptwo):
	shared = {}

	# Find scores of each object
	x = {}
	y = {}
	index = 1
	for movie in data[pone]:
		if movie in data[ptwo]:
			shared[movie] = 1
			x[index] = data[pone][movie]
			y[index] = data[ptwo][movie]
			index += 1

	# If no common element return 0
	if len(shared) == 0:
		return 0

	# Calculate ranks for each object
	x = spearman_sort(x)
	y = spearman_sort(y)

	# Find the difference between ranks
	diff = []
	for index in range(0,len(x)):
		diff.append(x[index][1] - y[index][1])

	# Calculate sum of squares of ranks	
	diffs = 0
	for each in diff:
		diffs += each**2

	# Calculate Spearman r = 1 - (6*summ(d**2)/n(n**2-1))
	l = len(shared)
	temp = (6*diffs)/(l*((l**2)-1))
	r = 1 - temp
	return r
#-----------------------------------------------------------------------------------------------------------------------
				

