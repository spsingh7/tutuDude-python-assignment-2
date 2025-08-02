def getInput():
    while True:
        user_input = input("Enter an number: ")
        try:
            n = int(user_input)
            return n 
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

num = getInput()
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

