from numpy import random
from sys import stdout
wordBank = [
	"copper",
	"explain",
	"educated",
	"truck",
	"neat",
	"unite",
	"branch",
	"tenuous",
	"hum",
	"decisive",
	"notice",
	"yard",
	"snow",
	"sordid",
	"spy",
	"zonked",
	"spoon",
	"shade",
	"amused",
	"greet",
	"embarrass",
	"filthy",
	"retire",
	"aromatic",
	"pizzas",
	"memory",
	"crib",
	"deserve",
	"lean"
	"erect"
]
def enterGuess():
	guess = input("Enter a letter: ").lower()
	#checks if guess is one letter and not used before
	while not guess.isalpha() or len(guess) > 1 or len(guess) == 0:
		print(" ")
		print("Invalid entry. Try again.")
		guess = input("Enter a letter: ").lower()
	letterUsed = True
	while True:
		if not letterUsed:
			break
		letterUsed = False
		for a in range(len(usedLetters)):
			if usedLetters[a] == guess:
				print(" ")
				print("Letter already used. Try again.")
				guess = input("Enter a letter: ").lower()
				letterUsed = True
				break
	#adds guess to used letters
	usedLetters.append(guess)
	usedLetters.sort()
	#checks if guess is right
	contain = False
	for a in range(len(word)):
		if word[a] == guess:
			showing[a] = True
			contain = True
	return contain
def draw():
	#hangman draw
	print("┍---┑")
	if missed > 0:
		print("|   0")
	else:
		print("|")
	if missed == 2:
		print("|  /|")
	elif missed > 2:
		print("|  /|\ ")
	else:
		print("|")
	if missed > 3:
		print("|   |")
	else:
		print("|")
	if missed == 5:
		print("|  /")
	elif missed > 5:
		print("|  / \ ")
	else:
		print("|")
	print("┸")
	#prints word
	for a in range(len(word)):
		if showing[a]:
			stdout.write(word[a])
		else:
			stdout.write("_")
		stdout.write(" ")
	print("")
#game loop to allow restarts
while True:
	#var set on start/restart
	missed = 0
	missedPrint = 0
	word = random.choice(wordBank)
	usedLetters = []
	showing = []
	for a in word:
		showing.append(False)
	while True:
		#indents/refreshes
		for a in range(50):
			print(" ")
		#prints if previous answer was correct or not
		if missedPrint == 1:
			print("Incorrect answer.")
			missedPrint = 0
		elif missedPrint == 2:
			print("Correct answer.")
		draw()
		#writes used letters
		stdout.write("Used letters: ")
		for a in range(len(usedLetters)):
			stdout.write(usedLetters[a] + " ")
		print(" ")
		#guess input, which returns if letter was correct or not
		if not enterGuess():
			missed += 1
			missedPrint = 1
			if missed == 6:
				print("You lost!")
				break
		else:
			missedPrint = 2
		#checks if word has been guessed
		blank = False
		for a in range(len(word)):
			if not showing[a]:
				blank = True
		if not blank:
			draw()
			print("You guessed the word!")
			break
	#play again loop
	play = input("Play again? (Y/N) ").upper()
	while not play == "Y" and not play == "N":
		print("Your answer was invalid.")
		play = input("Play again? (Y/N) ").upper()
	if play == "N":
		break