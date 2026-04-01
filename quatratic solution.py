a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if(a==0 or b==0 or c==0):
    print("It is a infinity solution")
else:
    d=b*b-4*a*c
    print("D=",d)
    if(d>0):
        print("roots are real and distinct")
    elif(d==0):
        print("roots are real and equal")
    else:
        print("IT IS COMPLEX AND DISTINCT")
