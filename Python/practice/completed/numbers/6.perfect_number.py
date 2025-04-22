def perfect_number():
    input_number=int(input("enter number:"))
    divisers_list=[]
    for i in range(1,input_number):
        if input_number%i==0:
            divisers_list.append(i)
    # print(divisers_list)
    sum=0
    for i in divisers_list:
        sum+=i
    print(sum)
    if sum==input_number:
        print("Given number is a perfect number")
    else:
        print("Given number is a not perfect number")

perfect_number()