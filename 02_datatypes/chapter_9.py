essential_spices = {"cardamon","ginger","cinnamon"}
optional_spices = {"cloves","ginger","black pepper"}

all_spices = essential_spices | optional_spices
print(f"Union spices {all_spices}")
all_spices = essential_spices & optional_spices
print(f"Intersection spices {all_spices}")