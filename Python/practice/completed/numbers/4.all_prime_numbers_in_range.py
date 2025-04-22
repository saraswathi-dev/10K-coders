def all_prime_numbers_in_range():
    min_number=int(input("Enter minimum Value:"))
    max_number=int(input("Enter maximum Value:"))
    number_list=[]
    prime_list=[]
    non_prime_list=[]
    for i in range(min_number,max_number+1):
        number_list.append(i)  
    print(number_list)
    
    for i in number_list:
        is_Prime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
               is_Prime=False
        if is_Prime:
            prime_list.append(i)
        else:
            non_prime_list.append(i)
    print("Prime Numbers:",prime_list)
    print("Non Prime Numbers:",non_prime_list)
all_prime_numbers_in_range()
        