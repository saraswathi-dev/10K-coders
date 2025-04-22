def pallindrom_range():
    min_number=int(input("Enter minimum Value:"))
    max_number=int(input("Enter maximum Value:"))
    pallindrom_list=[]
    for i in range(min_number,max_number+1,1): 
        j=str(i)
        if j==j[::-1]:
            pallindrom_list.append(i)
    # return " ".join(pallindrom_list)
    return " ".join(map(str,pallindrom_list))
x=pallindrom_range()
print(x)
    