#Problem Statement: Given a string, write a program to Capitalize the first and last character of each word of that string.
# Input: String str = "take u forward is awesome"
# Output: “TakE U ForwarD IS AwesomE”
# Explanation: We get the result after capitalizing the first and last character of each word of a string
def capitalize():
    statement=input("Enter statement:").split()
    # for i in range(len(statement)):
    result=[]
    for word in statement:
        if len(word)==1:
            result.append(word.upper())
        elif 3>len(word)>1:
            result.append(word.upper())
        elif  len(word)>=3:
            newWord=word[0].upper()+ word[1:-1] +word[-1].upper()
            result.append(newWord)
    return (" ".join(result))
x=capitalize()
print(x)