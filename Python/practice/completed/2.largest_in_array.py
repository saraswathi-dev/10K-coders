lst=map(int,(input("enter values separated by comma :").split(',')))
max=float('-inf')
for value in lst:
    if value>max:
        max=value
print("minimum value in the list:{}".format(max))