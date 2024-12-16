# Ryan Haddadi, September 2 2021, create a main menu that holds a contacts list

def print_list(contact_list):
#this prints out any of the clients inputs for first name and last name
	print ("*** Tuffy Titan Contact Main Menu")
	print ("INDEX       First Name          Last Name")
	for contact in range(len(contact_list)):
		print (f'{str(contact):8}{contact_list[contact][0]:22}{contact_list[contact][1]}')

def add_contact(contact_list):
#this is where the client inputs their contacts
	firstname = input("Enter First name:")
	lastname = input("Enter Last name:")
	fullname = [firstname,lastname]
	contact_list.append(fullname)
	return contact_list

def modify_contact(contact_list):
#this is where we would change contacts if we made an error related to someones name
	indexcheck = int(input("Please give me the index number of the contact you would like to change."))
	if (indexcheck not in range (len(contact_list))):
		print ("Invalid index number.")
		return contact_list
	else:
		firstname = input("Enter First name:")
		lastname = input("Enter Last name:")
		contact_list[indexcheck] = [firstname,lastname]
	return contact_list

def delete_contact(contact_list):
#this where the user will delete a contact if neccessary
	deleteindex = int(input("Please give me the index number of the contact you would like to delete"))
	if (deleteindex not in range(len(contact_list))):
		print ("Invalid index number.")
		return contact_list

	else:
		contact_list.remove(contact_list[deleteindex])
	return contact_list
