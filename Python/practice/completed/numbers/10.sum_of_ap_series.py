def ap_series_sum():
    a=int(input("Enter Starting Number:"))
    d=int(input("Enter difference in series:"))
    n=int(input("Enter number of values in series:"))
    series = [a + i * d for i in range(n)]
    print(series)
    sum=0
    for i in series:
        sum+=i
    print(sum)
ap_series_sum()