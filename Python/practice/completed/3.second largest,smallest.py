def second_largest():
    lst=[1,2,7,15,3,12,4,50]
    max1=float('-inf')
    max2=float('-inf')
    for i in lst:
        if i>max1:
            max1=i
    for i in lst:
        if max2<i<max1:
            max2=i
    return max1,max2
x=second_largest()
print(x)