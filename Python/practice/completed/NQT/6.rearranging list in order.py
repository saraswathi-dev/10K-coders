def re_arrange():
    lst=[1,9,4,7,2,3,8,6,10,5,2]
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                lst[i],lst[j]=lst[j],lst[i]
    print(lst)
    n=len(lst)/2
    mid=int(n)
    for i in range(mid,len(lst)):
        for j in range(mid+1,len(lst)):
            if lst[i]<lst[j]:
                lst[i],lst[j]=lst[j],lst[i]
    return lst
x=re_arrange()
print(x)
