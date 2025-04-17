def even_odd(lst):
    options=input("Enter how many values you want :")

    for i in range(len(nums)+1):
        for j in range(i+1,len(nums)):
            if nums[i]%2!=0:
                nums[i],nums[j]=nums[j],nums[i]
                print(lst)
    return nums
nums=[10,98,3,33,12,22,21,11]
# nums=[map(int,input("Enter values :").split())]
x=even_odd(nums)
print(x)