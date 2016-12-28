import os

print("UNO v0.7.3")
print("")
print("What would you like to do?")
options = ["setup", "play", "help"]
choice = ""
while not (choice in options):
	print("Your options are - setup, play, help")
	choice = raw_input()
if choice == "setup":
	easymode = ""
	while ((easymode != "yes") and (easymode != "no")):
		print("Should easy mode be enabled? (showing possible moves)")
		easymode = raw_input("yes or no: ")
	theme = ""
	themes = []
	for root, folders, filenames in os.walk('./themes'):
		for filename in [f for f in filenames if f.endswith('.py')]:
			themes.append(filename.replace(".py",""))
	while not (theme in themes):
		print("Which theme would you like to use? Your choices are:")
		print(themes)
		theme = raw_input("")
	with open("config.txt","w") as file:
		file.write("# Should we show the player what cards they can play?\n")
		if easymode == "no":
			file.write("easymode = False\n\n")
		else:
			file.write("easymode = True\n\n")
		file.write("# What theme are we using?\n")
		file.write('execfile("themes/' + theme + '.py")')
	print("Alright! Your changes have been saved.")
elif choice == "play":
	import game
elif choice == "help":
	print("Help is currently unavailable.")