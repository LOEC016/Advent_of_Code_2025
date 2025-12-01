import pandas as pd

position = 50
counter = 0 

df = pd.read_csv(r".venv\input.txt", header=None, dtype=str)

for entry in df[0]:
    entry = entry.strip()
    direction = entry[0]
    spins = int(entry[1:])

    if direction == "R":
        position = (position + spins) % 100
    elif direction == "L":
        position = (position - spins) % 100

    if position == 0:
        counter += 1

print("Part 1: " +  str(counter))

for entry in df[0]:
    entry = entry.strip()
    direction = entry[0]
    spins = int(entry[1:])

    if direction == "R":
        updated_position = (position + spins) % 100
        if position < updated_position:
            if position < 0 <= updated_position:
                counter += 1
        else:
            full_rounds = (position + spins) // 100
            counter += full_rounds
        position = updated_position

    elif direction == "L":
        updated_position = (position - spins) % 100
        if position > updated_position:
            counter += 1
        else:
            full_rounds = (spins - position - 1) // 100 + 1 if spins > position else 0
            counter += full_rounds
        position = updated_position
    
print(full_rounds)

