def index_of_target():
    # nums = [1, 3, 5, 6]
    nums=list(map(int,input("enter numbers :").split()))
    # nums=[int(input("enter numbers :").split())]
    target=int(input("Enter target value :"))
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        sorted_list=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums.index(target)
x=index_of_target()
print(x)