#Prime number in the range between 1 to 1000
#Author = RK
#!/usr/bin/python

for num in range(2,10):
	for i in range(2,num):
		if num%i == 0:
			j=num/i
			print '%d equals %d * %d' % (num,i,j)
			break
		else:
			print num, 'is a prime number'
			
'''
for num in range(3,10):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print '%d equals %d * %d' % (num,i,j)
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print num, 'is a prime number'
'''	