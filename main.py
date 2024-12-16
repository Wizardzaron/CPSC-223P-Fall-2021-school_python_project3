#Ryan Haddadi, September 6 2021, acts as the main interface for the client

from contacts import*

contact_list = [];
choice = 0
while (choice >= 0 and choice < 5):
	print("1.) Print list")
	print("2.) Add contact")
	print("3.) Modify contact")
	print("4.) Delete contact")
	print("5.) Exit the program")
	choice =int(input ("Please choose from the selections above"))

	if(choice == 1):
		print_list(contact_list)
	elif	(choice == 2):
		add_contact(contact_list)
	elif	(choice == 3):
		modify_contact(contact_list)
	elif	(choice == 4):
		delete_contact(contact_list)
