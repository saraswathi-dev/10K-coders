def max_product_in_subarray():
    nums=[2,5,6,0,-4,-5,-9,-1,0,-8]
    maxProduct=0
    maxList=[]
    for i in range(0,len(nums)-1):
        if nums[i]==0:
            continue
        product=1
        tem_maxList=[]
        for j in range(i,len(nums)):
            product=product*nums[j]
            tem_maxList.append(nums[j])
            if product>maxProduct:
                maxProduct=product
                maxList=tem_maxList[:]
            if nums[j]==0:
                break
            
    return maxProduct,maxList
x=max_product_in_subarray()
print(x)

# numbers=list(map(int,input("Enter numbers :").split()))
# print(numbers)
# def subarray_max_product(numbers):
#     max_value=0
#     sub_array=[]
#     for i in range(0,len(numbers)-1):
#         if numbers[i]==0:
#             continue
#         product=1
#         print("products of {} ".format(numbers[i]))
#         tem_sub_array = []
#         for j in range(i,len(numbers)):
#             print("{}*{}={}".format(product,numbers[j],product*numbers[j]))
#             product = product * numbers[j]
#             # max_value=max(product,max_value)
#             tem_sub_array.append(numbers[j])
#             if product>max_value:
#                 max_value=product
#                 sub_array=tem_sub_array[:]

#             if numbers[j]==0:
#                 break
#         print("*" * 40)
#     return max_value,sub_array
# x=subarray_max_product(numbers)
# print(x)