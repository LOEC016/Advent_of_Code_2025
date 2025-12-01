import pandas as pd

position = 50 #start
counter = 0 

df = pd.read_csv(r".venv\input.txt", header=None, dtype=str)

for entry in df[0]:
    entry = entry.strip()
    direction = entry[0] # L or R
    spins = int(entry[1:])

    if direction == "R":
        position = (position + spins) % 100
    elif direction == "L":
        position = (position - spins) % 100

    if position == 0:
        counter += 1

print("Code part 1: " +  str(counter))
#END PART ONE

df = pd.read_csv(r".venv\input.txt", header=None, dtype=str)
position = 50 #start
counter = 0 #reset
dials = 100  # 0..99

for entry in df[0]:
    # Delete possible whitespaces
    entry = entry.strip() 
     # L or R
    direction = entry[0] 
   
    raw_spins = int(entry[1:]) # spins from input
    # (positiv) +spins = right; (negativ) -spins = left
    spins = raw_spins if direction == "R" else -raw_spins 

    new_position = (position + spins) % dials
    if spins > 0:
        passed_zeros = ((position + spins) // dials) - (position // dials)
    else:
        passed_zeros = ((position - 1) // dials) - ((position + spins - 1) // dials)

    counter += passed_zeros


    position = new_position

print("Code part 2: " + str(counter))