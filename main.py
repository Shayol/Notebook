from record import Record
import shelve

print('''Notebook program starting...\n
"Enter new record or type 'Quit' to exit.\n
Type 'More' to get a list of commands that Notebook understands.\n
Type 'Delete' to delete last entered record.\n
A record is saved when you press enter \n''')

db = shelve.open("recordDB")     

while True:

	user_input = str(input(" >> "))
	modified_input = user_input.strip().lower()

	if modified_input == 'quit':
		db.close()
		print("See you soon.")
		break

	elif modified_input == 'more':
		print('''Quit - to exit the program\n
Delete - to delete last entered record\n
All - to see all records''')

	elif modified_input == 'all':
		for key in sorted(db):
			print(db[key])

	elif modified_input == 'delete':
		if db.len > 0:
			last_record_key = sorted(db)[-1]
			del db[last_record_key]
			print("Record deleted.")
		else:
			print("No records yet.")

	else:
		new_record = Record(user_input.strip())
		db[new_record.date] = new_record
		print(new_record)
