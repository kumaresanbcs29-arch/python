sample_set={"yellow","orange","pink"}
sample_list=["blue","green","black"]
sample_tuple=("white","pink")
for item in sample_list:
    sample_set.add(item)
for item in sample_tuple:
    sample_set.add(item)
print("updated sample set",sample_set)
