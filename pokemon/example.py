from pokemon import Pokemon
from type import getWeaknessPoint
import random # dummy
import operator

# create Pokemon
poke1 = Pokemon("Venusaur", ["GRASS", "POISON"], ["NORMAL", "GRASS", "POISON"], 80, 82, 83, 100, 80)
poke2 = Pokemon("Charizard", ["FIRE", "FLYING"], ["NORMAL", "FIRE"], 78, 84, 78, 85, 100)
# print(poke1)
# print(poke2)

all_pokemons = [poke1, poke2]

weights = {
	'hp': 0.3,
	'attack': 0.4,
	'defense': 0.2,
	'special': 0.4,
	'speed': 0.1
}

def calculate_stat(en_po, our_po):
	stat = (our_po.hp - en_po.hp)*weights['hp'] + (our_po.attack - en_po.attack)*weights['attack'] + \
		(our_po.defense - en_po.defense)*weights['defense'] + (our_po.special - en_po.special)*weights['special'] + \
		(our_po.speed - en_po.speed)*weights['speed']
	print("Stat: "+str(stat))
	return stat

# MAIN ALGORITHM
def predict(enemy_pokemons):
	# if len(enemy_pokemons) is not 6:
	# 	print("ERR: enemy_pokemons must have length = 6")
	# 	return None

	our_pokemons = []
	# 
	all_predictions = []
	for en_po in enemy_pokemons:
		# calculate points for each pokemons
		predictions = {}
		for al_po in all_pokemons:
			strongs = [getWeaknessPoint(en_po.types, mo_ty) for mo_ty in al_po.move_types]
			weaks = [getWeaknessPoint(al_po.types, mo_ty) for mo_ty in en_po.move_types]
			predictions[al_po.name] = {
				'pokemon': al_po, 
				'strong_point': sum(strongs),
				'weak_point': float(1) / sum(weaks),
				'stat_point': calculate_stat(en_po, al_po)
				}

		# sort based on points
		sorted_predictions = sorted(predictions.items(), key=lambda x: x[1]['stat_point'])
		print(sorted_predictions)
		all_predictions.append(sorted_predictions)

	used_pokemons = []
	for i in range(len(enemy_pokemons)):
		found = False
		j = 0
		while not found:
			if all_predictions[i][j][0] not in used_pokemons:
				found = True
			else:
				j += 1

		pokemon_name = all_predictions[i][j][0]
		used_pokemons.append(pokemon_name)
		our_pokemons.append(all_predictions[i][j][1])


	return our_pokemons

pred = predict([poke1, poke2])
for p in pred:
	print(p['pokemon'])
	print(p['strong_point'])
	print(p['weak_point'])
	print(p['stat_point'])