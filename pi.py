from decimal import *

ZERO = Decimal('0')
ONE = Decimal('1')
TWO = Decimal('2')
THREE = Decimal('3')
NEG_ONE = Decimal('-1')
TEN = Decimal('10')

class pi(object):

	def __init__(self, accuracy=10):

		self.accuracy=accuracy
		#self.pi, self.error = self.calculate()
		#self.pi = self.calculate()

	def Leibniz(self):

		getcontext().prec = self.accuracy+4
		magnatude=TEN**(NEG_ONE*(self.accuracy+1))

		sum = ZERO
		remainder=ONE/magnatude
		terms = (remainder+ONE)/TWO

		print "Number of terms: {}".format(terms)

		getcontext().prec = int(terms.log10())+2
		print getcontext().prec

		count = ONE

		while count<terms+ONE: 
			part = (NEG_ONE**(count+ONE))/(TWO*count-ONE)
			sum += part
			
			count += ONE

			if count % TEN**TWO == 0:
				print "{}/{}".format(count,terms)

		return (sum*Decimal('4')).quantize(Decimal(".0001"))#, ROUND_HALF_UP)


	def Madhava_Leibniz(self):

	    
	    getcontext().prec = self.accuracy+1

	    #magnatude=Decimal(10)**(Decimal(-1)*(self.accuracy+1))	
	    magnatude=Decimal(self.accuracy+1)**(Decimal(-1))

	    sum = Decimal('0')
	    a = Decimal('12')**Decimal('.5')
	    nThird = Decimal('-1')/Decimal('3')
	    remanider=magnatude/a
	    remanider=remanider**Decimal('-1')
	   # print number_of_terms
	    remainder=0
	    num=0
	    while(remanider>=remainder):
		num+=10
		remainder=(Decimal('3')**Decimal(num+1))*Decimal(((num+1)*2)+1)
	    print num	

	    for i in xrange(0, num, 1):
		numerator = nThird**Decimal(i)
		den = Decimal((i*2)+1)
		sum = sum + (numerator/den)
	       
	    #return (a*sum).quantize(Decimal('.1')**(Decimal(self.accuracy)), rounding=ROUND_HALF_UP), remainder**Decimal(-1)*a
	    return (a*sum).quantize(Decimal('.00000000001'), rounding=ROUND_HALF_UP), remainder**Decimal(-1)*a
	   # return a*sum, (remainder**Decimal(-1))*a

	def Smith(self):
                getcontext().prec = self.accuracy+4
		magnatude=TEN**(NEG_ONE*(self.accuracy+1))

		terms=ONE/magnatude
		terms/=(TWO*TWO)

		count=ZERO

		while terms>((TWO*count**THREE)+(THREE*count**TWO)+count):
                        count += ONE
                print count

                asum = ZERO
		i=ONE
		while i < count:
                        asum+= (NEG_ONE**(i+ONE))/(Decimal('4')*i*((TWO*i**TWO)+(THREE*i)+ONE))
                        i+=ONE

                        if i % TEN**TWO == 0:
				print "{}/{}".format(count,count)
				
		return (asum*Decimal('4')+THREE).quantize(magnatude*TEN, ROUND_HALF_UP)
	
	def __str__(self):
		return str(self.pi)
		
p=pi(accuracy = 100)
#print p.Leibniz()
print p.Smith()
