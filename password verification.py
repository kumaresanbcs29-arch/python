password=input("enter a password:")
upper=0
lower=0
digit=0
if len(password)>=8:
    for ch in password:
        if ch >="A" and ch <="Z":
           upper=1
        elif ch>="a" and ch <="z":
            lower=1
        elif ch>="0" and ch <="9":
            digit=1
    if upper==1 and lower==1 and digit==1:
        print("valid password")
    else:
        print("invalid password")
else:
    print("invalid password")
