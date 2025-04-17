# For example, there are n=7 socks with colors ar = {1,2,1,2,1,3,2}. There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

# Function Description
# Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.
# sockMerchant has the following parameter(s):
#              n: the number of socks in the pile
#              ar: the colors of each sock

# Input Format
#             The first line contains an integer n, the number of socks represented in ar.
#             The second line contains n space-separated integers describing the colors ar[i] of the socks in the pile.

# Constraints
#              1 <= n <= 100
#              1 <= ar[i] <= 100 & 0 <= i < n

# Output Format
#              Return the total number of matching pairs of socks that Alex can sell.

# Sample Input
#              9
#              10 20 20 10 10 30 50 10 20
# Sample Output
#              3

# Explanation
#              Alex can match 3 pairs of socks i.e 10-10, 10-10, 20-20
#              while the left out socks are 50, 60, 20
def count_pairs():
    n=input("Enter how many socks values u want:")
    socks=input("Enter color codes:").split()
    setSocks=set(socks)
    print(setSocks)
    color_count_dict={}
    for color in socks:
        if color in color_count_dict:
            color_count_dict[color]+=1
        else:
            color_count_dict[color]=1
    totalPairs=0
    for count in color_count_dict.values():
        totalPairs+=count//2
    return totalPairs
        
x=count_pairs()
print("Total Pairs",x)
    
    