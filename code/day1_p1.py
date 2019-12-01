mass = []
fuel = 0
with open('day1_input', 'r') as file:

    for line in file:
        mass.append(int(line))

for i in mass:
    output = (int(i / 3) - 2 )
    fuel += output

print(fuel)