def prime_number():
    number=int(input("Enter a number to check prime or not:"))
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return "Not aprime Number"
    return "Prime Number"
x=prime_number()
print(x)