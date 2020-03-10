# Python3 program to find next 
# sparse number 

def nextSparse(x): 
	
	# Find binary representation of 
	# x and store it in bin[]. 
	# bin[0] contains least significant 
	# bit (LSB), next bit is in bin[1], 
	# and so on. 
	bin = [] 
	while (x != 0): 
		bin.append(x & 1) 
		x >>= 1

	# There my be extra bit in result, 
	# so add one extra bit 
	bin.append(0) 
	n = len(bin) # Size of binary representation 
	
	# The position till which all 
	# bits are finalized 
	last_final = 0

	# Start from second bit (next to LSB) 
	for i in range(1,n - 1): 
		if ((bin[i] == 1 and (bin[i - 1] == 1
			or bin[i + 1] != 1))): 
			bin[i + 1] = 1
			for j in range(i,last_final-1,-1): 
				bin[j] = 0
			last_final = i + 1
	ans = 0
	for i in range(n): 
		ans += bin[i] * (1 << i) 
	return ans 

# Driver Code 
if __name__=='__main__': 
	x = 38
	print("Next Sparse Number is",nextSparse(x)) 

# This code is contributed by 
# mits 

