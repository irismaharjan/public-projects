def num():
    user_input = int(float(input("Enter your number: ")))
    another_input = int(input("How many multiples do you want: "))
    print("The multiples are:")
    for i in range(another_input+1):
        print(i*user_input)
    option = input("Do you want to do it again? yes or no: ")
    if option == "yes":
        num()
    else:
        print("Goodbye !!!")
num()