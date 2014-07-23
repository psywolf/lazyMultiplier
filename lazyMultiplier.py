#!/usr/bin/python3

class LazyMultiplier:
	def __init__(self, startArray):
		#create initial cache
		self.cache = dict()
		for i in range(len(startArray)):
			self.cache[(i,i)] = startArray[i]

		#only for evaluating performance
		self.cacheMisses = 0

	def multiplyRange(self, startIndex, endIndex):
		if (startIndex, endIndex) not in self.cache:
			divider = startIndex + (endIndex - startIndex) // 2
			self.cache[(startIndex, endIndex)] = self.multiplyRange(startIndex, divider) * self.multiplyRange(divider+1,endIndex)
			self.cacheMisses += 1
		return self.cache[(startIndex, endIndex)]


def calculateAnswer(initialArray, printStats):
	lazy = LazyMultiplier(initialArray)

	answer = []
	for i in range(len(initialArray)):
		if i == 0:
			answer.append(lazy.multiplyRange(i+1,len(initialArray)-1))
		elif i == len(initialArray)-1:
			answer.append(lazy.multiplyRange(0,i-1))
		else:
			answer.append(lazy.multiplyRange(0,i-1) * lazy.multiplyRange(i+1,len(initialArray)-1))
	
	if printStats:
		size = len(initialArray)
		n2 = size * size
		percent = (lazy.cacheMisses / n2) * 100
		print('arraySize:{}, cacheMisses:{}, n2:{}, percent:{:.2f}%'.format(size, lazy.cacheMisses, n2, percent))

	return answer


# test
testInput = [1,2,3,4,5]
print("testing with input {}\nanswer={}\n".format(testInput,calculateAnswer(testInput, False)))

print("performance testing")
for i in range(1000, 5001, 1000):
	calculateAnswer([0]*i, True)



	