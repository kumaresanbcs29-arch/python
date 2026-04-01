l1=[10,20,30,40,50,60,70]
new_list=[]
for i in range(len(l1)):
    if i!=0 and i !=5:
        new_list.append(l1[i])
print("list after removing 0th and 5th:",new_list)
