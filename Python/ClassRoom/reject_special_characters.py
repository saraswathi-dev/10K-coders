def reject_special_characters():
    input_string=input("Write Here:")
    special_characters="!@#$%^&*()<>;:'-+=_/.,`~"
    for i in input_string:
        if i in special_characters:
            print("String is not accepted")
            print("please rerenter the value....")
            return
    print("String is accepted") 
reject_special_characters()
