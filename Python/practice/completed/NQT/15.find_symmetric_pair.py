def find_symmetric():
            
    input_list = list(map(int, input("Enter all pair elements: ").split()))
    pairs = [(input_list[i], input_list[i+1]) for i in range(0, len(input_list)+1,2)]
    # n=int(input("Enter no of pairs:"))
    # pairs=[]
    for _ in range(n):
        a,b=map(int,input("Enter two values:").replaace(","," ").split())
        pairs.append((a,b))
    print(pairs)
x=find_symmetric()
print(x)

