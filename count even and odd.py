n=int(input("Enter a number:"))
even=0
odd=0
for i in range(0,n):
    if (i%2==0):
        even=even+1
    if (i%2!=0):
        odd=odd+1
print("the odd is",odd)
print("the even is ", even)
