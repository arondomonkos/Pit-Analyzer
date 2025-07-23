# Pit Analyzer
# Author: Áron Domonkos
# Year: 2023

print('Function 1')

data = []
with open('depth.txt', 'r') as file:
    for line in file:
        line = line.strip()
        data.append(int(line))

print(f'Total number of measurements: {len(data)}')


print('\nFunction 2')

# distance_input = int(input('Enter a distance value: '))
distance_input = 9
print(f'Depth at this location: {data[distance_input - 1]} meters')


print('\nFunction 3')
untouched = 0

for value in data:
    if value == 0:
        untouched += 1

print(f'Percentage of untouched area: {round((untouched / len(data) * 100), 2)}%')


pits = []
pit = []

for i in range(1, len(data)):
    if data[i-1] == 0 and data[i] != 0:
        pit.append(data[i])
    if data[i-1] != 0 and data[i] != 0:
        pit.append(data[i])
    if data[i-1] != 0 and data[i] == 0:
        pits.append(pit)
        pit = []

with open('pits.txt', 'w') as file:
    for pit in pits:
        file.write(' '.join(list(map(str, pit))))
        file.write('\n')


print('\nFunction 5')
print(f'Number of pits: {len(pits)}')


print('\nFunction 6')
print('a)')

selected_pit = []

if data[distance_input - 1] == 0:
    print('There is no pit at the specified location.')

else:
    start = distance_input - 2
    while data[start] != 0:
        start -= 1
    start += 2

    end = distance_input
    while data[end] != 0:
        end += 1
    print(f'Pit starts at: {start} meters, ends at: {end} meters')

    print('b)')
    i = start - 1
    while i < end - 1 and data[i] <= data[i + 1]:
        i += 1
    while i < end - 1 and data[i] >= data[i + 1]:
        i += 1

    if i < end - 1:
        print('Does not deepen continuously.')
    else:
        print('Deepens continuously.')

    print('c)')
    max_depth = data[start - 1]
    for i in range(start, end):
        if data[i] > max_depth:
            max_depth = data[i]
    print(f'Maximum depth: {max_depth} meters')

    width = 10
    volume = 0
    water_capacity = 0
    print('d)')
    for i in range(start - 1, end):
        volume += data[i] * width
        water_capacity += (data[i] - 1) * width
    print(f'{volume} m^3')

    print('e)')
    print(f'{water_capacity} m^3')