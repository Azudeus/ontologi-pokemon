weaknessMatrix = [
	[1,1,1, 1,1,1, 1,1,1, 1,1,1, 0.5,0,1],
	[1,0.5,0.5, 1,2,2, 1,1,1, 1,1,2, 0.5,1,0.5],
	[1,2,0.5, 1,0.5,1, 1,1,2, 1,1,1, 2,1,0.5],
	[1,1,2, 0.5,0.5,1, 1,1,0, 2,1,1, 2,1,0.5],
	[1,0.5,2, 1,0.5,1, 1,0.5,2, 0.5,1,0.5, 2,1,0.5],
	[1,1,0.5, 1,2,0.5, 1,1,2, 2,1,1, 1,1,2],
	[2,1,1, 1,1,2, 1,0.5,1, 0.5,0.5,0.5, 2,0,1],
	[1,1,1, 1,2,1, 1,0.5,0.5, 1,1,2, 0.5,0.5,1],
	[1,2,1, 2,0.5,1, 1,2,1, 0,1,0.5, 2,1,1],
	[1,1,1, 0.5,2,1, 2,1,1, 1,1,2, 0.5,1,1],
	[1,1,1, 1,1,1, 2,2,1, 1,0.5,1, 1,1,1],
	[1,0.5,1, 1,2,1, 0.5,2,1, 0.5,2,1, 1,0.5,1],
	[1,2,1, 1,1,2, 0.5,1,0.5, 2,1,2, 1,1,1],
	[0,1,1, 1,1,1, 1,1,1, 1,0,1, 1,2,1],
	[1,1,1, 1,1,1, 1,1,1, 1,1,1, 1,1,2]
]

def getWeaknessPoint(pokemonType, attackType):	
	if len(pokemonType) == 2:
		return weaknessMatrix[mapTypeToInt(attackType)][mapTypeToInt(pokemonType[0])] * weaknessMatrix[mapTypeToInt(attackType)][mapTypeToInt(pokemonType[1])]
	else:
		return weaknessMatrix[mapTypeToInt(attackType)][mapTypeToInt(pokemonType[0])]

def mapTypeToInt(type):
	return {
		'NORMAL': 0,
		'FIRE': 1,
		'WATER': 2,
		'ELECTRIC': 3,
		'GRASS': 4,
		'ICE': 5,
		'FIGHTING': 6,
		'POISON': 7,
		'GROUND': 8,
		'FLYING': 9,
		'PSYCHIC': 10,
		'BUG': 11,
		'ROCK': 12,
		'GHOST': 13,
		'DRAGON': 14,
	}.get(type, "ERROR")
