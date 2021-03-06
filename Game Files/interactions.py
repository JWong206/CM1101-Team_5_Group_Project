import time
import config
import map
import sys
import gameparser
import items

def print_by_char(string,wait):
	for char in string:
		sys.stdout.write( '%s' % char )
		sys.stdout.flush()
		time.sleep(wait)
	print()

def win(score):
    print("\n" * 64)
    print("The lights go out, you hear a voice through speakers surrounding you.\n")
    time.sleep(2)
    if score == 0:
        print_by_char("Well...",0.2)
        time.sleep(2)
        print_by_char("\nI don't know what to say...",0.02)
        time.sleep(1.8)
        print_by_char("\nThat... that was such a miserable performance. You know what? I'm just going to let you leave.",0.02)
        time.sleep(2)
        print_by_char("\nGoodbye.",0.02)
        time.sleep(0.5)
        print("-------\n\n\n\n")
        print("You scored 0 out of 8. Thank you for playing, or at least, attempting to.")
    if score == 1:
        print_by_char("Well...",0.2)
        time.sleep(2)
        print_by_char("\nIf your parents were watching I don't think they'd be proud.",0.02)
        time.sleep(1.5)
        print_by_char("\nWho knows, maybe they are watching...",0.02)
        time.sleep(1.2)
        print_by_char("\nMaybe the whole world is watching. Hopefully you'll perform better this time around.",0.02)
        time.sleep(2)
        print_by_char("\nGoodbye.",0.02)
        time.sleep(0.5)
        print("-------\n\n\n\n")
        print("You scored 1 out of 8. Thank you for playing, we're sure you tried your hardest.")
    if score == 2:
        print_by_char("Well...",0.2)
        time.sleep(2)
        print_by_char("\nYou tried, at least theres that.",0.02)
        time.sleep(1.3)
        print_by_char("\nYou know, we selected you because we thought you had potential.",0.02)
        time.sleep(1.6)
        print_by_char("\nThe potential to do better than this. Prove us right, we do so hate being wrong.",0.02)
        time.sleep(2)
        print_by_char("\nGoodbye.",0.02)
        time.sleep(0.5)
        print("-------\n\n\n\n")
        print("You scored 2 out of 8. Thank you for playing.")
    if score == 3:
        print_by_char("Well...",0.2)
        time.sleep(2)
        print_by_char("\nThat was thoroughly average.",0.02)
        time.sleep(1.2)
        print_by_char("\nWe wiped your entire memory, yet you remembered how to be practically useless.",0.02)
        time.sleep(1.8)
        print_by_char("\nCome on Harris, it might just be that the entire world is depending on you.",0.02)
        time.sleep(2)
        print_by_char("\nGoodbye.",0.02)
        time.sleep(0.5)
        print("-------\n\n\n\n")
        print("You scored 3 out of 8. Thank you for playing.")
    if score == 4:
        print_by_char("Well...",0.2)
        time.sleep(2)
        print_by_char("\nGood. Not great, not even close. But good.",0.02)
        time.sleep(1.5)
        print_by_char("\nHow are we supposed to test this facility with these results?",0.02)
        time.sleep(1.8)
        print_by_char("\nWe're going to rewipe, hopefully you turn out more impressive this time.",0.02)
        time.sleep(2)
        print_by_char("\nGoodbye.",0.02)
        time.sleep(0.5)
        print("-------\n\n\n\n")
        print("You scored 4 out of 8. Thank you for playing.")
    if score == 5:
        print_by_char("Well...",0.2)
        time.sleep(2)
        print_by_char("\nYou've performed adequately.",0.02)
        time.sleep(1.2)
        print_by_char("\nMaybe you're good enough.",0.02)
        time.sleep(1.5)
        print_by_char("\nNo. I don't think so. Not quite. Rerun the tests.",0.02)
        time.sleep(2)
        print_by_char("\nGoodbye.",0.02)
        time.sleep(0.5)
        print("-------\n\n\n\n")
        print("You scored 5 out of 8. Thank you for playing.")
    if score == 6:
        print_by_char("Well...",0.2)
        time.sleep(2)
        print_by_char("\nDid you know, you volunteered to come here.",0.02)
        time.sleep(2)
        print_by_char("\nYou voluntarily wiped your memory, with the promise of its safe and swift return.",0.02)
        time.sleep(1)
        print_by_char("\nYou thought you were here to test a new amusement park, but it's not turned out that way has it.",0.02)
        time.sleep(2)
        print_by_char("\nGoodbye.",0.02)
        time.sleep(0.5)
        print("-------\n\n\n\n")
        print("You scored 6 out of 8. Thank you for playing.")
    if score == 7:
        print_by_char("Well...",0.2)
        time.sleep(2)
        print_by_char("\nHarris. A human... You seem to be recovering your bearings sufficiently.",0.02)
        time.sleep(2.5)
        print_by_char("\nYou voluntarily wiped your memory, with the promise of its safe and swift return.",0.02)
        time.sleep(1)
        print_by_char("\nYou thought you were here to test a new amusement park, but it's not turned out that way has it.\nThe world is different now Harris, and you have achieved sufficient results to reenter it.\nUnfortunately, we do not have the resources to return your memory.\nSorry about that.",0.02)
        time.sleep(3)
        print_by_char("\nGoodbye.",0.02)
        time.sleep(0.5)
        print("-------\n\n\n\n")
        print("You scored 7 out of 8. Thank you for playing.")
    if score == 8:
        print_by_char("Well...",0.2)
        time.sleep(2)
        print_by_char("\nI am impressed. You completed the experiment with flying colours!",0.02)
        time.sleep(2.5)
        print_by_char("\nWe promised the highest performer an explanation, so here it is.",0.02)
        time.sleep(1)
        print_by_char("\nCulture Complex isn't what it seems.\nWe wiped the memories of you and every other volunteer.\nIt was meant to be harmless, temporary! But the world changed.\nNow you've proven yourself to be the most adaptable, we have the resources to return your memory.\nIt is up to you to save us.",0.02)
        time.sleep(3)
        print_by_char("\nGoodbye.",0.02)
        time.sleep(0.5)
        print("-------\n\n\n\n")
        print("You scored 8 out of 8. Congratulations.")
    time.sleep(10)
    sys.exit("\nGame over")

global answer1
global answer2
global answer3
global answer4
global answer5
answer1 = "Unanswered"
answer2 = "Unanswered"
answer3 = "Unanswered"
answer4 = "Unanswered"
answer5 = "Unanswered"
def console():
	global answer1
	global answer2
	global answer3
	global answer4
	global answer5
	print("\n///////////////////////////\n")
	print("Hello subject. The questions are:\n")
	print(" 1) What is your name?\n" + '  > ' + answer1 + "\n\n 2) Who created this facility?\n"+ '  > ' + answer2 + "\n\n 3) What is your purpose?\n" + '  > ' + answer3 + "\n\n 4) What is the name of the company operating this facility?\n" + '  > ' + answer4 + "\n\n 5) What are you?\n" + '  > ' + answer5 + "\n\n///////////////////////////")
	print('\nAre you ready to answer a question?')
	print('\nYou can type:')
	print(" YES")
	print(" NO")
	print(" CLEAR (To clear all answers)")
	print(" SUBMIT (To submit answers, this can only be done once)")
	print(" NOTE to view notes\n")
	print("///////////////////////////")
	choice = gameparser.normalise_input(input('> '))
	if type(choice) == list:
		if choice[0] == "yes":
			print("Please select a question to answer, 1/2/3/4/5:")
			question = input('> ')
			if question == "1":
				if answer1 == "Unanswered":
					print("What is your name?")
					answer1 = input('> ')
				else:
					print("Do you want to overwrite your previous answer:")
					print(answer1)
					if input("YES\nNO\n") == "yes":
						print("What is your name?")
						answer1 = input('> ')
			if question == "2":
				if answer2 == "Unanswered":
					print("Who created this facility?")
					answer2 = input('> ')
				else:
					print("Do you want to overwrite your previous answer:")
					print(answer2)
					if input("YES\nNO\n") == "yes":
						print("Who created this facility?")
						answer2 = input('> ')
			if question == "3":
				if answer3 == "Unanswered":
					print("What is your purpose?")
					answer3 = input('> ')
				else:
					print("Do you want to overwrite your previous answer:")
					print(answer3)
					if input("YES\nNO\n") == "yes":
						print("What is your purpose?")
						answer3 = input('> ')
			if question == "4":
				if answer4 == "Unanswered":
					print("What is the name of the company operating this facility?")
					answer4 = input('> ')
				else:
					print("Do you want to overwrite your previous answer:")
					print(answer4)
					if input("YES\nNO\n") == "yes":
						print("What is the name of the company operating this facility?")
						answer4 = input('> ')
			if question == "5":
				if answer5 == "Unanswered":
					print("What are you?")
					answer5 = input('> ')
				else:
					print("Do you want to overwrite your previous answer:")
					print(answer5)
					if input("YES\nNO\n") == "yes":
						print("What are you?")
						answer5 = input('> ')
			print("\nReturning you to menu...")
			time.sleep(1.2)
			console()
		elif choice[0] == "clear":
			if 'yes' in gameparser.normalise_input(input("Are you sure you want to clear all of your current answers?\nYES\nNO\n")):
				answer1,answer2,answer3,answer4,answer5 = "Unanswered"
				print("Answers cleared.")
				time.sleep(1.5)
				console()
		elif choice[0] == "no":
			print("\nVery well. Explore the complex and find the answers. Quickly now.\n")
		elif choice[0] == "submit":
			if 'yes' in gameparser.normalise_input(input("Are you sure you want to submit your answers?\nYES\nNO\n")):
				print("Excellent. Assessing your performance...")
				time.sleep(2)
				score = 0
				if "harris" in gameparser.normalise_input(str(answer1)):
					score = score+1
				if "esther" in gameparser.normalise_input(str(answer2)):
					score = score+1
				if "jakobe" in gameparser.normalise_input(answer2):
					score = score + 1
				if "franco" in gameparser.normalise_input(answer2):
					score = score + 1
				if "freedom" in gameparser.normalise_input(answer3):
					score = score+1
				if "culture" in gameparser.normalise_input(answer4):
					score = score+1
				if "complex" in gameparser.normalise_input(answer4):
					score = score+1
				if "human" in gameparser.normalise_input(answer5):
					score = score+1
				win(score)
		elif choice[0] == "note":
			print(items.item_notepad["description"])
			console()
	elif type(choice) == None:
		interact_console()

interact_console = {
	"id": "console",
	"name":"the console in the centre of the room",
	"action": console
}

def arcade():
	print("You approach the machine and it turns on, practically inviting you to play.\nYou grab the joystick and start tapping buttons until you get a new highscore!\nThe leaderboard proudly displays the score, and next to it you notice a name: Harris")

interact_arcade = {
	"id": "arcade",
	"name": "the classic arcade game",
	"action": arcade
}

def bb8():
	print('BB-8 beeps friendlily. He displays a hint from Jedi Master Luke Skywalker \n-''Study yourself intently to determine what you truly are.''')

interact_bb8 = {
	'id': 'bb8',
	'name': 'a BB-8 droid',
	'action': bb8
}

def holochess():
	print("You fiddle with the holochess thing, the creatures on the board grumble and roar as they slay eachother.")

interact_holochess = {
	"id": "holochess",
	"name": "the holochess board",
	"action": holochess
}

def tombstone():
	print('You read whats inscribed on the headstone: PROPERTY OF CULTURE COMPLEX.\n The rest of the writing is illegible.')

interact_tombstone = {
	'id': 'tombstone',
	'name': 'a tombstone',
	'action': tombstone
}

def crates():
	item_records = {
    'id':'records',
    'name': 'an experiment record page',
    'description': 'You read: \nNAME: Harris \nNUMBER: 983762 \nSTATUS: Experiment interrupted.'}
	print("You open the crates, revealing their contents; an experiment record page.")
	map.room_indiana["items"].append(item_records)

interact_crates = {
	"id": "crates",
	"name":"some wooden crates",
	"action":crates
}

def walkietalkie():
	print_by_char('Harris, come in. Over.', 0.05)
	time.sleep(0.8)
	print_by_char('Can you hear me Harris?', 0.05)
	time.sleep(0.8)
	print_by_char('Harris please respond. Over.', 0.05)

interact_walkietalkie = {
	'id': 'walkietalkie',
	'name': 'a walkie-talkie',
	'action': walkietalkie
}

def radio():
	print('''This is an emergency broadcast. Culture Complex's servers are down. \nDo not attempt to interact with any artificial beings. \nThis is vital for your safety. \nThis broadcast will repeat in thirty seconds.''')

interact_radio = {
	'id': 'radio',
	'name': 'an emergency radio',
	'action': radio
}

def laptop():
	print('There is a critical battery warning window open: \n| YOUR BATTERY IS RUNNING LOW (6%) |\nYou click OK. There is a BBC website open. The headline reads: \nSCIENTIST COUPLE OPEN AN AMUSEMENT PARK WHERE YOU CAN INTERACT WITH ARTIFICIAL BEINGS \nJakobe Franco confirms opening date. \nThe laptop hibernates. The battery is dead.')

interact_laptop = {
	'id': 'laptop',
	'name': 'a laptop',
	'action': laptop
}

def mirror():
	print('You look at your reflection in the mirror: \nDark hair, blue eyes, athletic physique. You are handsome.\nYou are wearing a hospital gown with a number on it - 983762.\nYou take a closer look at your hands.\nMovement of your muscles allows your palm to be stretched and compressed.\nYou can feel the blood flowing in your veins.\nYou are pretty sure that you are a human.')

interact_mirror = {
	'id': 'mirror',
	'name': 'a mirror',
	'action': mirror
}

def book():
	print('''You open the 'Culture Complex's social experiment records' book. \nIt includes lists of hundreds of names, numbers, dates and room names.''')

interact_book = {
	'id': 'book',
	'name': 'a book',
	'action': book
}
