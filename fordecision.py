#!/usr/bin/python

fruits = ['banana','pear','orange','apple']

print 'Program starts ...'
for fruit in fruits:
	print fruit



print 'next for loop...'



def frange(start,stop,step):
	i = start;
	while i < stop:
		yield i
		i += step
for i in frange(4.0,10.0,2.0): 
	print (i)
print 'Program ends'