#prompt user with 
#with open("flashfilename", "a") as x:
	#x.write("appended text")


flashcard = {}
ivd = {v: k for k, v in flashcard.items()}
print flashcard
print ivd

x = raw_input('>>>')
y = raw_input('>>>')

flashcard[x] = y

print flashcard

