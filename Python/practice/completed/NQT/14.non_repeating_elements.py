def find_non_repeatitive():
    numbers=list(map(int,input("Enter values:").split()))
    repeated_numbers=[]
    non_repeated_numbers=[]
    duplicates_removed_array=[]
    for i in numbers:
        if i not in duplicates_removed_array:
            duplicates_removed_array.append(i)
        else:
            repeated_numbers.append(i)
    for i in repeated_numbers:
        for j in duplicates_removed_array:
            if i==j:
                duplicates_removed_array.remove(i)
             
    return duplicates_removed_array
x=find_non_repeatitive()
print(x)