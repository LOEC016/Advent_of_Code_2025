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

print(counter)
