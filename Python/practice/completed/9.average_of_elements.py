def average():
    n=int(input("Enter no of values:"))
    values=list(map(int,input("Enter values:").split()))
    # sum_of_values=sum(values)
    # average=sum_of_values/n
    sum=0
    for i in values:
        sum+=i
        average=sum/n   
    return average
x=average()
print(x)