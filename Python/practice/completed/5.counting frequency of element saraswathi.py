def counting_element():
    lst1= input("Enter value:")
    lst=list(lst1)
    no_duplicate_lst=[]
    for i in lst:
        if i not in no_duplicate_lst:
            no_duplicate_lst.append(i)
    # print(no_duplicate_lst)
    result=[]
    for j in no_duplicate_lst:
        count=0
        for i in lst:
            if i==j:
                count=count+1
        result.append((j,count))
    # print(result)
    for i in range(len(result)):
        print("{}{}".format((result[i][0]),(result[i][1])),end=" ")
counting_element()
