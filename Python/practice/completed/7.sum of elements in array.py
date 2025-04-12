def sum_of_elements():
    lst=list(map(int,input("Enter Values:").split()))
    lst1=list(lst)
    total=0
    for i in lst1:
        total=total+i
    return total
x=sum_of_elements()
print(x)