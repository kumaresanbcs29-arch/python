m1=int(input("enter a number:"))
m2=int(input("enter a number:"))
m3=int(input("enter a number:"))
m4=int(input("enter a number:"))
m5=int(input("enter a number:"))
total=m1+m2+m3+m4+m5
precentage=total/5
print("MARK%=",precentage)
if(precentage>=90):
    print("o GRADE")
elif(precentage>=80):
    print("A+GRADE")
elif(precentage>=70):
    print("A GRADE")
elif(precentage>=60):
    print("B+GRADE")
elif(precentage>=55):
    print("B GRADE")
elif(precentage>=50):
    print("C GRADE")puthon3
else:
    print("FAIL")