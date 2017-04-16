#!/usr/bin/python
from tabulate import tabulate
# Open a file
with open("C:\\Users\\rnooji.ORADEV\Documents\\file.txt", "r+") as f:
    list=[]
    for line in f:
        list.append(line)
#	for i in range(len(list)):
	if 'Success' in line:
            print line
	elif 'Failed' in line:
	    print line
	elif 'In Progress' in line :
	    print "Status In Progress"





'''
fo = open("C:\\Users\\rnooji.ORADEV\Documents\\file.txt", "r+")
str = fo.readline();
print "Read String is : -->", str

#for line in str:
#    print "--->",line

'''
