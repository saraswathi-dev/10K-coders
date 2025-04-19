lst=map(int,(input("enter values separated by comma :").split(',')))
min=float('inf')
for value in lst:
    if value<min:
        min=value
print("minimum value in the list:{}".format(min))