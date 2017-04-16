def sum(seq):
	def add(x,y): return x+y
	return reduce(add, seq, 0)

result=sum(range(1,6))
print result