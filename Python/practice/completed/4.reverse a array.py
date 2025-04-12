def reverse_array():
    lst=[1,2,7,15,3,12,4,50]
    lst1=[]
    for i in range(-1,-len(lst),-1):
        lst1.append(lst[i])
    return lst1
x=reverse_array()
print(x)

