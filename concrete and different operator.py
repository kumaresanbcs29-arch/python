
while True:
    print("\n1,addition")
    print("\n2,subtraction")
    print("\n3,exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        d1={"a":1,"b":2}
        d2={"a":3,"b":4}
        d1.update(d2)
        print("result",d1)
    elif choice==2:
        d1={"a":1,"b":2,"c":3}
        d2={"b":2}
        result={}
        for key in d1:
            if key not in d2:
                result[key]=d1[key]
        print("difference:",result)
    elif choice==3:
        print("exit")
        break
    else:
        print("invalid choice")


