def sort_elements_by_frequency():
    lst=[1,9,4,7,2,3,8,6,2,3,7,9,5,10,2]
    duplicates_removed_list=[]
    # for i in range(0,len(lst)):
    #     for j in range(i+1,len(lst)):
    #         if lst[i]>lst[j]:
    #             lst[i],lst[j]=lst[j],lst[i]
    for i in lst:
        if i not in duplicates_removed_list:
            duplicates_removed_list.append(i)
    print(lst)
    print(duplicates_removed_list) 
    sorted_elements_frequency=[]
    for i in duplicates_removed_list:
        count=0
        for j in lst:
            if i==j:
                count+=1
        sorted_elements_frequency.append((i,count))
    sorted_elements_frequency.sort(key=lambda x:x[1],reverse=True)
    print(sorted_elements_frequency)
    final_dict=dict(sorted_elements_frequency)
    return final_dict     
x=sort_elements_by_frequency()
print(x)
