def median():
    n=int(input("Enter no of values:"))
    values=list(map(int,input("Enter values:").split()))
    for i in range(len(values)):
        for j in range(len(values)):
            if values[i]<values[j]:
                values[i],values[j]=values[j],values[i]
    print(values)
    mid=len(values)//2
    mid_value=round(mid)
    if len(values)%2==0:
        median=(values[mid-1]+values[mid])/2
        return median
    else:
        median=values[mid_value]
        return median
x=median()
print(x)