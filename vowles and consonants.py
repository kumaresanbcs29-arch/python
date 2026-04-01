string=input("enter a string")
vowles=0
consonants=0
for ch in string:
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U":
        vowles+=1
    elif(ch>="a" and ch<="z") or (ch>="A" and ch<="z"):
        consonants=consonants+1
print("vowles=",vowles)
print("consonants=",consonants)
