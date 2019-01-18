import csv

class HashMap():

    def __init__(self, map_len):
        self.map_len = map_len
        self.map = self.map_len * [False]
        self.hash = None

    def get_hash(self, key):
        sum = 0
        for char in str(key):
            sum += ord(char)
        self.hash = sum
        return self.hash

    def add(self, key, value):
        entry = [key, value]
        hash_value = self.get_hash(key)
        if self.map[hash_value] is False:
            self.map[hash_value] = [entry]
            return True

        else:

            for old_entry in self.map[hash_value]:
                if (old_entry[0] == entry[0]) and (old_entry[1] == entry[1]):
                    print('The key already in the hash map.')
                    return True
                else:
                    self.map[hash_value].append(entry)
                    return True

    def get(self, key):
        hash_value = self.get_hash(key)
        if self.map[hash_value] is False:
            print('This key is not in the hash map.')
            return None
        else:
            if len(self.map[hash_value]) == 1:
                return self.map[hash_value][0][1]
            else:
                for pair in self.map[hash_value]:
                    if pair[0] == key:
                        return pair[1]

    def remove(self, key):
        hash_value = self.get_hash(key)
        if self.map[hash_value] is False:
            return True
        else:
            # in case of no collision
            if len(self.map[hash_value]) == 1:
                self.map[hash_value].pop()
            else:
                # in case of collision we use "for loop"
                for pair in self.map[hash_value]:
                    if pair[0] == key:
                        self.map[hash_value].remove(pair)

    # can be called additionally to inspect the collisions
    def print_collision(self):
        for address in self.map:
            if address is not False and len(address) > 1:
                print(address)


pokemon_hashmap = HashMap(20000)

with open('pokemon.csv', 'r') as csvfile:
    pokemons = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in pokemons:
        pokemon_name = row[1]
        pokemon_type = row[2]
        pokemon_hashmap.add(pokemon_name, pokemon_type)

# let's get pokemon type for Bulbasaur
pokemon_query = 'Bulbasaur'
print('{} is of type: {}'.format(pokemon_query, pokemon_hashmap.get(pokemon_query)))
# let's get pokemon type for Gastly
pokemon_query = 'Gastly'
print('{} is of type: {}'.format(pokemon_query, pokemon_hashmap.get(pokemon_query)))
# let's now remove Gastly and then try to look it up
pokemon_hashmap.remove(pokemon_query)
print('{} is of type: {}'.format(pokemon_query, pokemon_hashmap.get(pokemon_query)))
# let's put Gastly back in it's place
pokemon_hashmap.add('Gastly', 'Ghost')



