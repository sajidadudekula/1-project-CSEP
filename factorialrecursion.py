#factorial program

def fact(a):
	if(a==1 or a==0):
		return 1
	else:
		n=a*fact(a-1)
		return n

key=int(input("enter the number:"))
print("The factorial of",key,"is",fact(key))
