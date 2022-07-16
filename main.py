

print ("\tWelcome to PyRPG!") #title mthfcka

print ("Enter your name, stranger: ") #account name. sort of.
name = input()
name = name.strip()

print (f"So, {name.title()} ,welcome aboard!") #greetings

characters = ['Mage', 'Warrior', 'Rouge']
print(characters)
player_char = input("Choose your character: ")
player_char = player_char.title()
if player_char == 'Mage':
	print(f"So, {name.title()}, you want to be a Mage? Good choce!")
elif player_char == 'Warrior':
	print("Alright, tough guy, so the Warrior it is!")
else:
	print(f"{name.title()}, aren't ya a sneaky boi? Shadows will bless ya!")
print(f"You choosen {player_char}")
