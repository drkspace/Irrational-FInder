from decimal import *

class pi(object):

	def __init__(self, accuracy=10):

		self.accuracy=Decimal(accuracy)
		self.pi, self.error = self.calculate()
		
	def calculate(self):

	    # Madhava Leibniz series
	    getcontext().prec = self.accuracy+3
	    print self.accuracy

	    #magnatude=Decimal(10)**(Decimal(-1)*(self.accuracy))	

	    sum = Decimal('0')
	   # a = Decimal('12')**Decimal('.5')
	    nThird = Decimal('-1')/Decimal('3')
	    number_of_terms=self.accuracy/a
	    number_of_terms=number_of_terms**Decimal('-1')
	    print number_of_terms
	    remainder=0
	    num=0
	    while(number_of_terms>=abs(remainder)):
		num+=1
		remainder=(Decimal('3')**Decimal(num))*Decimal((num*2)+1)
	    	

	    for i in xrange(0, num, 1):
		num = nThird**Decimal(i)
		den = Decimal((i*2)+1)
		sum = sum + (num/den)
	       
	   # return (a*sum).quantize(magnatude, rounding=ROUND_HALF_UP), remainder
	    return a*sum, remainder
	
	def __str__(self):
		return self.pi
		
p=pi(accuracy = 10)
print p
