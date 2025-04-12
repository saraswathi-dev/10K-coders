def moving_elements():
    n=int(input("Enter how many values u want in list:"))
    lst=list(map(int,input("Enter values:").split()))
    shift_value=int(input("Enter how many values u want to shift:"))
    if shift_value<=len(lst):
        lst1=lst[shift_value:]
        lst2=lst[:shift_value]
        return lst1 + lst2
    else:
        print("shift_value not greater than len(lst)")

x=moving_elements()
print(x)
