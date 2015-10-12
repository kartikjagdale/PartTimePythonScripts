

def main():
	print 'Printing 1 to 100:'

	for i in xrange(1,101):
		if i%3==0 and i%5==0:
			print 'FizzBuzz',
		elif i%3==0:
			print 'Fizz',
		elif i%5==0:
			print 'Buzz',
		else:
			print i,



if __name__ == '__main__':
	main()
