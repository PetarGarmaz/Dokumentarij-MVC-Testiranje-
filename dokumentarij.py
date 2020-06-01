# Dokumentarij je aplikacija za ispis i unos novih studenata 
# na kolegiju Razvoj poslovnih aplikacija
# za brisanje: https://note.nkmk.me/en/python-list-clear-pop-remove-del/

class DokumentarijModel:
	def __init__(self):
		self.names = []
	
	@property
	def names(self):
		return self._names

	@names.setter
	#Ovdje moram imat isti naziv metode kao i kod property-a, ako nemam, ispisuje mi error: "AttributeError: can't set attribute"
	def names(self, new_name):
		self._names = new_name

class DokumentarijView:
	def display_title_bar(self):    
		print("\t****************************************************")
		print("\t***  Dokumentarij - Razvoj poslovnih aplikacija  ***")
		print("\t****************************************************")
		
	def get_user_choice(self):
		# Let users know what they can do.
		print("\n[1] Pogledaj listu studenata.")
		print("[2] Dodaj novog studenta.")
		print("[x] Izlaz.")
		
		return input("Što želite napraviti u dokumentariju?")

	def show_names(self, name):
		print(name.title())

	def insert_new_name(self):
		new_name = input("\nUnesite ime studenta: ")
		
		return new_name

class DokumentarijController:
	### MAIN PROGRAM ###

	# Set up a loop where users can choose what they'd like to do.
	def __init__(self, model, view):
		self.model = model
		self.view = view

	def get_names(self):
		# Shows the names of everyone who is already in the list.
		print("\nOvo je popis studenata na kolegiju Razvoj poslovnih aplikacija 2019/2020:\n")
		for name in self.model.names:
			self.view.show_names(name)

	def get_new_name(self):
		# Asks the user for a new name, and stores the name if we don't already
		#  know about this person.
		new_name = self.view.insert_new_name()

		if new_name in self.model.names:
			print("\n{} je već upisan/a u dokumentariju!".format(new_name.title()))
		else:
			self.model.names.append(new_name)
			print("\nDobrodošao/la {}!\n".format(new_name.title()))

	def play(self):
		choice = ''
		self.view.display_title_bar()
		while choice != 'x':    
			
			choice = self.view.get_user_choice()
			
			# Respond to the user's choice.
			self.view.display_title_bar()
			if choice == '1':
				self.get_names()
			elif choice == '2':
				self.get_new_name()
			elif choice == 'x':
				print("\nHvala na pregledu/uređivanju dokumentarija. Pozdrav.")
			else:
				print("\nGreška - napravite hvatanje izuzetaka sami za vježbu.\n")
				
if __name__ == "__main__":
	game = DokumentarijController(DokumentarijModel(), DokumentarijView())
	game.play()