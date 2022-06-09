#To find  whether the given string is an Anagram 
str1=input("Enter the first string:")
str2=input("Enter the second string:")
a=sorted(str1)
b=sorted(str2)
if a==b:
	print("Given string is anagram of  first string")
else:
	print("Given string is not an anagram of  first string")
