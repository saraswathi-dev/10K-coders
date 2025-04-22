def replace():
    input_value=input("Enter Value:")
    output=""
    for i in input_value:
        if i==",":
            output=output+"."
        else:
            output=output+i
    print(output)
replace()

# input_value=input("Enter Value:")
# input_value_updated=input_value.replace(",",".")
# print(input_value_updated)

