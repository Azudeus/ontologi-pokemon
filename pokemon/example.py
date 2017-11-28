from pokemon import Pokemon
import random # dummy
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}


# create Pokemon
poke1 = Pokemon("Venusaur", ["GRASS", "POISON"], ["NORMAL", "GRASS", "POISON"], 80, 82, 83, 100, 80)
poke2 = Pokemon("Charizard", ["FIRE", "FLYING"], ["NORMAL", "FIRE"], 78, 84, 78, 85, 100)
print(poke1)
print(poke2)

all_pokemons = [poke1, poke2]

# dummy method (TODO)
def getWeaknessPoint(attack_move_types, defense_types):
	return random.randint(1, 5)

print(getWeaknessPoint(poke1.move_types, poke2.types))

# MAIN ALGORITHM
def predict(enemy_pokemons):
	# if len(enemy_pokemons) is not 6:
	# 	print("ERR: enemy_pokemons must have length = 6")
	# 	return None

	our_pokemons = []
	# 
	all_predictions = []
	for en_po in enemy_pokemons:
		predictions = {}
		for al_po in all_pokemons:
			predictions[al_po.name] = {
				'pokemon': al_po, 
				'strong_point': getWeaknessPoint(al_po.move_types, en_po.types),
				'weak_point': float(1) / getWeaknessPoint(en_po.move_types, al_po.types) 
				}
		sorted_x = sorted(predictions.items(), key=lambda x: x[1]['weak_point'])
		print(sorted_x)
		all_predictions.append(predictions)

	return our_pokemons

print(predict([poke1, poke2]))