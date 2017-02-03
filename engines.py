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