def remove_duplicates():
    array=list(map(int,input("Enter values:").split()))
    print(array)
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i]<array[j]:
                array[i],array[j]=array[j],array[i]
    print(array)
    no_duplicate_array=[]
    for i in array:
        if i not in no_duplicate_array:
            no_duplicate_array.append(i)
    return no_duplicate_array
x=remove_duplicates()
print(x)
    
    