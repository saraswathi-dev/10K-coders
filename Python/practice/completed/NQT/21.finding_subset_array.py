def subset():
    arr1= [1,3,4,5,2]
    arr2= [2,4,3,1,7,5,15]
    for i in arr1:
        # for j in arr2:
            if i not in arr2:
                print("arr1 is not subset") 
                return
    print( "arr1 is a subset")    
x=subset()
print(x)        