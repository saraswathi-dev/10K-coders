def  gp_ratio():
    a=int(input("Enter Starting Number:"))
    r=int(input("Enter ratio:"))
    n=int(input("Enter number of values in series:"))
    if r==1:
        series=a*n
    else:
         series =a * ((1 - r**n) // (1 - r)) if r < 1 or (1 - r**n) % (1 - r) == 0 else a*((1-r**n)/(1-r))
    print(series)
gp_ratio()
        