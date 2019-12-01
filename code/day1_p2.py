mass = []
fuel = 0
with open('day1_input', 'r') as file:

    for line in file:
        mass.append(int(line))



def fuel_calc(mod_mass):
    mod_fuel = 0
    temp_mod_fuel = (int(mod_mass / 3) - 2 )
    mod_fuel += temp_mod_fuel
    while True:
        temp_mod_fuel = (int(temp_mod_fuel / 3) - 2 )
        if temp_mod_fuel <= 0:
            break
        mod_fuel += temp_mod_fuel
    return mod_fuel


for i in mass:
    fuel += fuel_calc(i)

print(fuel)