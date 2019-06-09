n=int(input("Enter a number : "))
s=0
while not n==0:
    r=n%10
    s+=r
    n=n//10
print("The sum of the digits :",s)
