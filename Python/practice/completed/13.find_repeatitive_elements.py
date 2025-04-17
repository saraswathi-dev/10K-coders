def find_repeatitive():
    numbers=list(map(int,input("Enter values:").split()))
    repeated_numbers=[]
    duplicates_removed_array=[]
    for i in numbers:
        if i not in duplicates_removed_array:
            duplicates_removed_array.append(i)
            # print(removed_duplicates)
        else:
            repeated_numbers.append(i)
    return repeated_numbers
x=find_repeatitive()
print(x)