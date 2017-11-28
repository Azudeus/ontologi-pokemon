import urllib.request
from bs4 import BeautifulSoup
from pokemon import Pokemon
import dill

POKEDEX_URL = "https://www.serebii.net/pokedex/{index}.shtml"
pokemons = []
exceptions = [24, 53]
for i in range(151):
	if i not in exceptions:
		#INDEX
		idx = i+1
		idx = str(idx)
		for i in range(3-len(idx)):
			idx = '0' + idx
		cur_url = POKEDEX_URL.format(index=idx)
		print("Scraping", cur_url)
		resp = urllib.request.urlopen(cur_url).read()
		bs = BeautifulSoup(resp, "lxml")
		
		#NAME
		name = bs.find("font", {"size": 4}).b.text[2:]

		#TYPEpyt
		pokemon_types_str = []
		pokemon_types = bs.find("td", {"class": "cen"}).children
		for j, pokemon_type in enumerate(pokemon_types):
			if j%2 == 0:
				pokemon_types_str.append(pokemon_type['href'][9:-6].upper())

		#MOVE SET
		move_set_str = set()
		move_set = bs.find("a", {"name": "attacks"}).next_sibling.find_all("tr")
		for j, move in enumerate(move_set):
			if (j%2 == 0) and (j!=0):
				move_set_str.add(
					move.find("td", {"class": "cen"}).img['src'][17:-4].upper()
				)
		move_set_str = list(move_set_str)

		#ATTRIBUTES
		hp = None
		attack = None
		defense = None
		special = None
		speed = None

		stats = bs.find("a", {"name": "stats"}).next_sibling.find_all("tr")
		attr = stats[2].find_all("td")
		hp = attr[1].text
		attack = attr[2].text
		defense = attr[3].text
		special = attr[4].text
		speed = attr[5].text

		# CREATE POKEMON
		cur_poke = Pokemon(name, pokemon_types_str, move_set_str,
			hp, attack, defense, special, speed)

		# ADD TO LIST
		pokemons.append(cur_poke)
		print(cur_poke)

# Save to file
with open('pokemons.pkl', 'wb') as fo:
	dill.dump(pokemons, fo)
