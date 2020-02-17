import random

def weighted_random(values, weights):
	total_weight = sum(weights)
	acum_weights = [w / total_weight for w in weights[:]]

	# accumulates weights
	for i in range(1, len(weights)):
		acum_weights[i] += acum_weights[i]  # this is not ok!!
	rand = random.random()

	# returns value if weight is higher than random value
	for value, weight in zip(values, acum_weights):
		if weight > rand:
			return value

def new_weighted_random(values, weights):
	total_weight = sum(weights)
	acum_weights = [w / total_weight for w in weights[:]]

	# accumulates weights
	for i in range(1, len(weights)):
		acum_weights[i] += acum_weights[i-1] # Now it works properly
	rand = random.random()

	# returns value if weight is higher than random value
	for value, weight in zip(values, acum_weights):
		if weight > rand:
			return value

print('library loaded')

if __name__=='__main__':
	values = [1, 2, 3]
	weights = [0.5, 0.3, 0.2]
	new_weighted_random(values, weights)