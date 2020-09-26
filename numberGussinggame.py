#GET GUESS NUMBER
import random
def num_guess():
	return list(input("Enter a guess number:"))
#GENERATE CODE RANDOM
def code_generater():
        numbers = [str(num) for num in range(20)]
        random.shuffle(numbers)
        return numbers[:3]
#GENERATE THE CLUES
def clues_generater(code,guess_user):
        if guess_user==code:
                return "CODE IS CRACKED!"
        clues = []
        for ind,num in enumerate(guess_user): #ind for index location
                if num == code[ind]:
                        clues.append("MATCH")
                elif num in code:
                        clues.append("YOU ARE CLOSELY TO RELATED THE MATCH")

        if clues == []:
                return ["YOUR GUESS NUMBER IS WRONG"]
        else:
                return clues
#CALL THE FUNCTION
print("WELCOME CODE BREAKER GAME!")
code_secret = code_generater()
clue_report = []

while clue_report != "CODE CRACKED!":
        guess = num_guess()
        clue_report = clues_generater(guess,code_secret)
        print("Here is the result of guess
              ")
        for clue in clue_report:
                print(clue)
