# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm

secret_word = "x"
guessed_word = ""
guess_num = 3
out_of_guesses = False

if guess_num <= 0:
    out_of_guesses = True

while guessed_word != secret_word and not out_of_guesses :
    if guess_num > 0:
        guessed_word = input("What is the secret word: ")
        guess_num -= 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose!")
else:
    print("You win!")


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.upper() in "AEIOU":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase:" )))

num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))
operator = input("Operation : ")

if operator == "x":
    print(float(num1*num2))
elif operator == "-":
    print(float(num1-num2))
elif operator == "/":
    print(float(num1/num2))
elif operator == "+":
    print(float(num1+num2))
else:
    print("Invalid Operator!")