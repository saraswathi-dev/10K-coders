original_list = [1,2,3,4]
shallow_copy_list=original_list.copy()
shallow_copy_list[3]=10
original_list[2]=0
print(original_list)
print(shallow_copy_list)
deep_copy_list=original_list.shallowcopy()
deep_copy_list[3]=20
print(deep_copy_list)
print(original_list)

