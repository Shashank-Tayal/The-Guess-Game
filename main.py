from random import randint
number_computer = randint(1, 100)
attempts = 0

print("\n-----------------------------------------------------------------------------------")
print("Welcome to the Guessing Game!")
name_user = input("Please enter your name: ").capitalize()
print(f"Hello, {name_user}! I have selected a number between 1 and 100. Can you guess it?")

while True:
    try:
        number_user = int(input("Enter a number between 1 and 100: "))

        if 1 <= number_user <= 100:
            attempts += 1
            if number_user < number_computer:
                print("Too low! Try again.")
            elif number_user > number_computer:
                print("Too high! Try again.")
            elif attempts == 1 and number_user == number_computer:
                print(f"Congratulations! You've guessed the number {number_computer} on your first try!")
                print("Congratulations! You've set the highest score with just 1 attempt!")
                print("-----------------------------------------------------------------------------------\n")
                
                with open("Test_File.txt" , "w") as file:
                    file.write(str(attempts))

                with open("High_Score.txt" , "w") as file:
                    file.write(f"New high score: {attempts} attempt, set by {name_user}!")
                    
                break
            else:
                
                print(f"Congratulations! You've guessed the number {number_computer} in {attempts} attempts!")

                with open("Test_File.txt" , "r") as file:
                    high_score = int(file.read())
                    if high_score == attempts:
                        print("Wow! You've matched the current high score!")
                        
                        with open("Test_File.txt" , "w") as file:
                            file.write(str(attempts))
                        with open("High_Score.txt" , "w") as file:
                            file.write(f"New high score: {attempts} attempts, set by {name_user}!")

                    elif high_score > attempts:
                        with open("Test_File.txt" , "w") as file:
                            file.write(str(attempts))
                        with open("High_Score.txt" , "w") as file:
                            file.write(f"New high score: {attempts} attempts, set by {name_user}!")

                        print(f"Congratulations, {name_user}! You've set a new high score with {attempts} attempts!")
                        print("-----------------------------------------------------------------------------------\n")
                  
                break
            
        else:
            print("Please, enter a number between 1 and 100!")
    except ValueError:
        print("Please enter a valid integer.")