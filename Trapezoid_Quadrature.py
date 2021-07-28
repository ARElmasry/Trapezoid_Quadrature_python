class Quadrature:
	def __init__(self,f , a, b, k, tol):
		self.f = f
		self.a = a
		self.b = b
		self.k = k
		self.tol = tol
	def start_int(self):
		I_new = 0.0 ; I_old = 0.0
		R = 1.e50
		for i in range(self.k):
			I_new =self.__recursiveTrapezoid (i+1, I_new)
			if R < self.tol:
				break
			R = abs(I_old-I_new)
			I_old = I_new
		I = I_old
		return I, i+1, R	
	def __recursiveTrapezoid (self,ii, I_old):
		if ii==1 :
			I_new = (self.f(self.a)+ self.f(self.b)) * (self.b-self.a)/2.0
		else:
			n = pow(2,ii-2)
			h = (self.b - self.a)/n
			x = self.a + h/2.0
			sum = 0.0
			for i in range(n):
				sum = sum + self.f(x)
				x = x + h
			I_new = (I_old +  h*sum)/2.0
		return I_new


def f (x):
###########################################################
###########################################################
###############Enter you Function here#####################
###########################################################
###########################################################
#for example:##############################################

	return x**-1
###########################################################
###########################################################
###########################################################
#Enter you boundary intervals here:########################

a = 0.1
b = 1.0
k = 50     # Maximum number of trials
tol= 0.001 # Required tolerance
###########################################################
###########################################################
###########################################################
###########################################################	
###########################################################

def main():
	
	integration_Obj = Quadrature(f, a, b, k, tol)
	I, trials, R = integration_Obj.start_int()	
	if trials == k:
			print(f"The number of trials exceeded {k}, the result of the integration reached is {I} with precision {R}")
			with open ("The results.txt", 'a') as outFile:
				outFile.write(f"\n The number of trials exceeded {k}, the result of the integration reached is {I} with precision {R}")
	print(f"The result of the integration is {I} after {trials} trials")	
	with open ("The results.txt", 'a') as outFile:
		outFile.write(f"\n The result of the integration is {I} after {trials} trials")	

if __name__== "__main__":
	main()
