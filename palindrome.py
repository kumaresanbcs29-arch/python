n=int(input("enter a number:"))
reverse=0
orginal=n
while(n>0):
    sum=n%10
    reverse=reverse*10+sum
    n=n//10
if(orginal==reverse):
    print("IT is palindrome")
else:
    print("Not a palindrome")
