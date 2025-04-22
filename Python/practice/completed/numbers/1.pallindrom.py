def pallindrom():
    input_word=input("enter sentence:")
    if input_word==input_word[::-1]:
        return "Pallindrom"
    else:
        return "Not Pallindrom"
x=pallindrom()
print(x)