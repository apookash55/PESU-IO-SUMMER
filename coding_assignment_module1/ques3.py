def binarySearch (arr, l, r, x): 
    if r >= l: 
        mid = l + (r - l)//2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
    else:  
        return -1
s=input("Enter the numbers list : ").split(",")
l=[]
for i in s:
    l.append(int(i))
x=int(input("Enter the nuber to be searched:"))
result = binarySearch(l, 0, len(l)-1, x) 
if result != -1: 
    print ("Element is present at index", result) 
else: 
    print ("Element is not present in array")

