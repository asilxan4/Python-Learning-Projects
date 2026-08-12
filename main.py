#Making an Calculator on Python level easy

# Asking the user to enter the first number
first_number = int(input("Enter first number: "))


# Asking the user to enter on of the options
calculator = input("Enter on of them: \n+ \n- \n* \n/ \n")


# Asking the user to enter the secound number
secound_number = int(input("Enter secound numbe: "))


# Creating the Function
def calculate():
    # Clarifying that if the option = "-"
    if calculator == "+":
        print(f"{first_number} + {secound_number} = {first_number+secound_number}")


    # Clarifying that if the option = "-"
    elif calculator == "-":
        print(f"{first_number} - {secound_number} = {first_number-secound_number}")


    # Clarifying that if the option = "*"
    elif calculator == "*":
        print(f"{first_number} * {secound_number} = {first_number*secound_number}")


    # Clarifying that if the option = "/"
    elif calculator == "/":
        if first_number == 0:
            print("Error,You cannot devide by zero")


        else:
            print(f"{first_number} / {secound_number} = {first_number/secound_number}")


    else:
        print("Please you should enter on of them:  \n+ \n- \n* \n/ ")


calculate()