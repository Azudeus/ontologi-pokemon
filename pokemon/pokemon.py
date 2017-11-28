class Pokemon:
	def __init__(self, name, types, move_types, hp, attack, defense, special, speed):
		self.name = name 				# string
		self.types = types 				# list of string
		self.move_types = move_types 	# list of string
		self.hp = hp 					# int
		self.attack = attack 			# int
		self.defense = defense 			# int
		self.special = special 			# int
		self.speed = speed 				# int

	def preprocessed(self):
		self.hp = int(self.hp) 					# int
		self.attack = int(self.attack) 			# int
		self.defense = int(self.defense) 			# int
		self.special = int(self.special) 			# int
		self.speed = int(self.speed) 				# int

	def __str__(self):
		return "\nName: %s\nTypes: %s\nMove Types: %s\nHP: %s\nATK: %s\nDEF: %s\nSPC: %s\nSPD: %s\n" % (self.name, ', '.join(self.types), ', '.join(self.move_types), self.hp, self.attack, self.defense, self.special, self.speed)