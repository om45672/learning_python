ingredients = ["Water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")

ingredients.remove("Water")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger","cardamom"]
chai_ingredients = ["water","milk"]

chai_ingredients.extend(spice_options)

print(f"Chai ingredients are {chai_ingredients}")
chai_ingredients.pop() # Also returns the element that is popped
print(f"Chai ingredients are {chai_ingredients}")

chai_ingredients.insert(2,"black tea")
print(f"Chai ingredients are {chai_ingredients[::-1]}")

chai_ingredients.sort()
print(f"Chai ingredients are {chai_ingredients}")

sugar_levels = [1,2,3,4,5]
print(f"Maximum sugar level:  {max(sugar_levels)}")

base_liquid = ["water","milk"]
extra_flavor = ["ginger"]

base_liquid+=extra_flavor

print(f"Base Liquid: {base_liquid}")

# base_liquid*=3
# print(f"Base Liquid: {base_liquid}")

base_liquid+=base_liquid[::-1]
print(f"Base Liquid: {base_liquid}")

# from operator import itemgetter

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes {raw_spice_data}")