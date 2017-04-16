from random import randint
import time
a=10
for a in range(0,9):
    print(randint(0,9))
	#print 10
	#a++
#	time.sleep( 2 )
    #print Done
print "Start : %s" % time.ctime()
time.sleep( 5 )
print "End : %s" % time.ctime()