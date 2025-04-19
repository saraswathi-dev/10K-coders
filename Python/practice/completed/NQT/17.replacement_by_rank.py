def replacement_by_rank():
    marksList=[2,25,45,6,9,10]
    for i in range(len(marksList)):
        for j in range(i+1,len(marksList)):
            if marksList[i]>marksList[j]:
                marksList[i],marksList[j]=marksList[j],marksList[i]
    print(marksList)
    rankList=[]
    initial_rank=1
    for i in range(len(marksList)):
        rankList.append(initial_rank)
        initial_rank+=1
    print(rankList)
    marks_ranks=dict(zip(marksList,rankList))
    print(marks_ranks)
    input_marks=int(input("Enter maarks to show rank:"))
    for i in marksList:
        if i==input_marks:
            rank_of_marks=marks_ranks.get(input_marks)
    return (rank_of_marks)
            
x=replacement_by_rank()
print(x)