def num():
    user_input = int(float(input("Enter a number: ")))
    if user_input%2 == 0:
        print("It is an even number")
    else:
        print("It is a odd number")
    options =input("do you want to do it again? yes or no: ")
    if options == "yes":
        num()
    else:
        print("Goodbye")
num()