masala_spices = ("cardamom", "cloves","cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala sicpe: {spice1} , {spice2}, {spice3}")

ginger_ratio, cadramom_ratio = 2,1
print(f"ratio is G : {ginger_ratio} and C: {cadramom_ratio}")

ginger_ratio,cadramom_ratio = cadramom_ratio,ginger_ratio
print(f"ratio is G : {ginger_ratio} and C: {cadramom_ratio}")

# membership

print(f"Is ginger is masala spices ? {'cloves' in masala_spices}")