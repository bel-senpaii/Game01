include characters.py

print ("\tWelcome to PyRPG!") #title

print ("Enter your name, stranger: ") #get player name
name = input()
name = name.strip()

print (f"So, {name.title()} ,welcome aboard!") #greetings

characters = ['Mage', 'Warrior', 'Rouge'] #list of characters
print(characters)

player_char = input("Choose your character: ") #player inputs character class

player_char = player_char.title() #sets player's first letter of input to uppercase to prevent errors


#confirm what character player is choosen
if player_char == 'Mage':
	print(f"So, {name.title()}, you want to be a Mage? Good choce!")
elif player_char == 'Warrior':
	print("Alright, tough guy, so the Warrior it is!")
else:
	print(f"{name.title()}, aren't ya a sneaky boi? Shadows will bless ya!")
print(f"You choosen {player_char}")
