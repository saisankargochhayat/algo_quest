# Given a range [L,R] find the count of numbers having prime number of set bits 
# in their binary representation.
# [This hint was included in O/P section. Only even numbers should be checked within the L,R range]
def setBits(n):
    return bin(n)[2:].count('1')
def SieveOfEratosthenes(n):
	
	# Create a boolean array "prime[0..n]" and initialize
	# all entries it as true. A value in prime[i] will
	# finally be false if i is Not a prime, else true.
	prime = [True for i in range(n+1)]
	p=2
	while(p * p <= n):
		
		# If prime[p] is not changed, then it is a prime
		if (prime[p] == True):
			
			# Update all multiples of p
			for i in range(p * 2, n+1, p):
				prime[i] = False
		p+=1
	lis =[]
	
	# Print all prime numbers
	for p in range(2, n):
		if prime[p]:
			lis.append(p)
	return lis
if __name__ == "__main__":
    x ,y = list(map(int,input().strip().split()))
    # for i in range():
    counter = 0
    primearr = SieveOfEratosthenes(y)
    for i in range(x,y+1):
        temp = setBits(i)
        if temp in primearr:
            counter+=1
    print(counter)