# def n_rotations_left():
#     n=int(input("Enter how many values u want to rotate:"))
#     rotations=int(input("Enter how many times u want to rotate:"))
#     num_list=[]
#     for i in range(1,n+1):
#         num_list.append(i)
#     print(num_list)
#     for i in range(rotations):
#         removed = num_list.pop(0)
#         num_list.append(removed)
#         print(f"{i} rotation:{num_list}")
#     print(num_list)
# n_rotations_left()
def n_rotations_right():
    n=int(input("Enter how many values u want to rotate:"))
    rotations=int(input("Enter how many times u want to rotate:"))
    num_list=[]
    for i in range(1,n+1):
        num_list.append(i)
    print(num_list)
    for i in range(rotations):
        removed = num_list.pop(-1)
        num_list.insert(0,removed)
        print(f"{i} rotation:{num_list}")
    print(num_list)
n_rotations_right()