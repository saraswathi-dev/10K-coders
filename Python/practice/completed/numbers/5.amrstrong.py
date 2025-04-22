def armstrong():
    input_number=input("Enter number:")
    digits = [int(d) for d in str(input_number)]
    sum=0
    for i in digits:
        sum=sum+(i**(len(digits)))
    if sum==int(input_number):
        print("given number is armstrong number")
    else:
        print("not a armstrong number")
armstrong()