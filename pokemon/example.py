from pokemon import Pokemon
from type import getWeaknessPoint

poke1 = Pokemon("Bulbasaur", ["GRASS", "POISON"], ["NORMAL", "GRASS", "POISON"], 80, 82, 83, 100, 80)
print(poke1)

print(getWeaknessPoint(["GRASS", "POISON"], "FIRE"))