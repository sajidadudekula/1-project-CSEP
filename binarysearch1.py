#binarysearch
def binarysearch(array,low,high,element):
	if  high>=low:
		mid=(low+high)//2
		if array[mid]==element:
			return array[mid]
		elif array[mid]>element:
			return binarysearch(array,low,mid-1,element)
		else:
			return binarysearch(array,mid+1,high,element)
	else:
		return -1
array=[11,22,33,44,55,66,77,88,99]
print("The list is",array)
element=int(input("Enter the element to search:"))


result=binarysearch(array,0,len(array)-1,element)
if result!=-1:
	print("element is present at",result)
else:
	print("element is not present in the list")
