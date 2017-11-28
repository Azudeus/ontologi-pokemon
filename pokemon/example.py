import dill
import operator
import random

from pokemon import Pokemon
from type import getWeaknessPoint


# load all Pokemons
with open('pokemons.pkl', 'rb') as fi:
	all_pokemons = dill.load(fi)
pikachu = Pokemon("025 Pikachu", ["ELECTRIC"], ["ELECTRIC", "NORMAL", "PSYCHIC"], 35, 55, 30, 50, 90)
psyduck = Pokemon("054 Psyduck", ["WATER"], ["NORMAL", "PSYCHIC", "WATER"], 50, 52, 48, 50, 55)
all_pokemons.insert(24, pikachu)
all_pokemons.insert(53, psyduck)

for p in all_pokemons:
	p.preprocessed()
	# print(p.name)

# get 6 random enemy pokemons
enemy_pokemons = []
for i in range(6):
	enemy_pokemons.append(all_pokemons[random.randint(0, len(all_pokemons)-1)])

weights = {
	'hp': 0.3,
	'attack': 0.4,
	'defense': 0.1,
	'special': 0.4,
	'speed': 0.1
}

weights_point = {
	'strong_point': 0.33,
	'weak_point': 0.33,
	'stat_point': 0
}

def calculate_stat(en_po, our_po):
	stat = (our_po.hp - en_po.hp)*weights['hp'] + (our_po.attack - en_po.attack)*weights['attack'] + \
		(our_po.defense - en_po.defense)*weights['defense'] + (our_po.special - en_po.special)*weights['special'] + \
		(our_po.speed - en_po.speed)*weights['speed']
	return stat

def calculate_point(pokemon):
	point = pokemon['strong_point'] * weights_point['strong_point'] + pokemon['weak_point'] * weights_point['weak_point'] + \
		pokemon['stat_point'] * weights_point['stat_point']
	return point

# MAIN ALGORITHM
def predict(enemy_pokemons):
	if len(enemy_pokemons) is not 6:
		print("ERR: enemy_pokemons must have length = 6")
		return None

	our_pokemons = []
	# 
	all_predictions = []
	for en_po in enemy_pokemons:
		# calculate points for each pokemons
		predictions = {}
		for al_po in all_pokemons:
			strongs = [getWeaknessPoint(en_po.types, mo_ty) for mo_ty in al_po.move_types]
			weaks = [getWeaknessPoint(al_po.types, mo_ty) for mo_ty in en_po.move_types]
			if sum(weaks) == 0:
				weak_point = 0
			else:
				weak_point = float(1) / (sum(weaks)/len(weaks))
			predictions[al_po.name] = {
				'pokemon': al_po, 								
				'strong_point': sum(strongs)/len(strongs),     			# effectiveness of this pokemon's moves against enemy					
				'weak_point': weak_point,					# effectiveness of enemy pokemon's moves against this pokemon
				'stat_point': calculate_stat(en_po, al_po)	# difference in stats * weight	
				}
			predictions[al_po.name]['all_point'] = calculate_point(predictions[al_po.name])

		# sort based on points
		sorted_predictions = sorted(predictions.items(), key=lambda x: x[1]['all_point'])
		all_predictions.append(sorted_predictions)

	used_pokemons = []
	for i in range(len(enemy_pokemons)):
		found = False
		j = len(all_predictions[i]) - 1
		while not found:
			if all_predictions[i][j][0] not in used_pokemons:
				found = True
			else:
				j -= 1

		pokemon_name = all_predictions[i][j][0]
		used_pokemons.append(pokemon_name)
		our_pokemons.append(all_predictions[i][j][1])

	return our_pokemons

# 
preds = predict(enemy_pokemons)
for i in range(len(preds)):
	p = enemy_pokemons[i]
	pred = preds[i]['pokemon']
	print("+--------------------------------------- POKEMON %s -----------------------------------+" % str(i+1))
	print("| Name |"+p.name.ljust(37)+" | "+pred.name.ljust(37)+" | ")
	print("| Type |"+', '.join(p.types).ljust(37)+" | "+', '.join(pred.types).ljust(37)+" | ")
	print("| MTyp |"+', '.join(p.move_types).ljust(37)+" | "+', '.join(pred.move_types).ljust(37)+" | ")
	print("| HP   |"+str(p.hp).ljust(37)+" | "+str(pred.hp).ljust(37)+" | ")
	print("| ATK  |"+str(p.attack).ljust(37)+" | "+str(pred.attack).ljust(37)+" | ")
	print("| DEF  |"+str(p.defense).ljust(37)+" | "+str(pred.defense).ljust(37)+" | ")
	print("| SPC  |"+str(p.special).ljust(37)+" | "+str(pred.special).ljust(37)+" | ")
	print("| SPD  |"+str(p.speed).ljust(37)+" | "+str(pred.speed).ljust(37)+" | ")
	print("+-------------------------------------------------------------------------------------+")
	print("| Strong Point".ljust(15)+": "+str(preds[i]['strong_point']).ljust(68)+" |")
	print("| Weak Point".ljust(15) +": "+ str(preds[i]['weak_point']).ljust(68)+" |")
	print("| Stat Point".ljust(15) +": "+ str(preds[i]['stat_point']).ljust(68)+" |")
	print("| All Point".ljust(15) +": "+ str(preds[i]['all_point']).ljust(68)+" |")
	print("+-------------------------------------------------------------------------------------+\n")


