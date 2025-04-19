def equlibrium_index():
    nums = [1,-1,4,2,3,1,6]
    for i in range(len(nums)):
        lst_left=nums[:i]
        lst_right=nums[i+1:]
        sum_left=sum(lst_left)
        sum_right=sum(lst_right)
        if sum_left==sum_right:
            return i
    return -1
x=equlibrium_index()
print(x)