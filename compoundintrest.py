#compound intrest

def  compound_interest(principal,r,t):
	if t==0:
		return principal
	else:
		return  compound_interest(p+(p*r)/100,r,t-1)
#print(c(1000,10,2))
p=int(input("enter the value of principal amount:"))
t=int(input("enter the time period:"))
r=int(input("enter the value of rate of interest:"))
print(compound_interest(p,r,t))
