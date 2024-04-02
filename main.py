import random
print("This is scissor paper, rock game in text only mode")
def game():
    print("Let's begin")
    print("Your options are as follows: scissor, paper, rock")
    user_options = input("Enter your option: ")
    user_input = user_options.lower()
    options = ("scissor", 'paper', "rock")
    computer_input = random.choice(options)
    if user_input == computer_input:
        print("Your chose", user_input, "and computer chose", computer_input)
        print("its a draw !!!")
    if user_input == "rock" and computer_input == "paper":
        print("Your chose", user_input, "and computer chose", computer_input)
        print("You lost !!!")
    if user_input == 'paper' and computer_input == 'rock':
        print("Your chose", user_input, "and computer chose", computer_input)
        print("You won !!!")
    if user_input == 'scissor' and computer_input == 'paper':
        print("Your chose", user_input, "and computer chose", computer_input)
        print("You won !!!")
    if user_input == "rock" and computer_input == "scissor":
        print("Your chose", user_input, "and computer chose", computer_input)
        print("you won !!!")
    if user_input == 'paper' and computer_input == 'scissor':
        print("Your chose", user_input, "and computer chose", computer_input)
        print("You lost !!!")
    if user_input == 'scissor' and computer_input == 'rock':
        print("Your chose", user_input, "and computer chose", computer_input)
        print("You lost !!!")

    another_input = input("Do you wont to continue? yes or no: ")
    if another_input == "yes":
        game()
    else:
        print('GOODBYE !!!')
game()