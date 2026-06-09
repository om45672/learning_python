favourite_chai = [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Lemon Tea",
    "Green Tea",
    "Elaichi Chai"
]

unique_chai = {tea for tea in favourite_chai if "Chai" not in tea}
# print(unique_chai)

recipes ={
    "Masala Chai": ["ginger","cardamom","clove"],
    "Elaichi Chai": ["cardamom","milk"],
    "Spicy Chai": ["ginger","black pepper","clove"],
}

unique_spices = {spice for spices in recipes.values() for spice in spices}

print(unique_spices)

    