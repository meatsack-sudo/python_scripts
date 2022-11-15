import random

defense_die = input("How many defense dice do you want to roll?")

offense_die = input("How many offense dice do you want to roll?")

defense_rolls = []

offense_rolls = []

for die in range(int(defense_die)):
    defense_roll = random.randint(1, 6)
    defense_rolls.append(defense_roll)


for die in range(int(offense_die)):
    offense_roll = random.randint(1, 6)
    offense_rolls.append(offense_roll)

sorted_defense = sorted(defense_rolls, reverse=True)
sorted_offense = sorted(offense_rolls, reverse=True)

print(f"Defense Rolls: {sorted_defense}")
print(f"Offense Rolls: {sorted_offense}")

if sorted_defense[0] >= sorted_offense[0] and sorted_defense[1] >= sorted_offense[1]:
    print("Defense won both rolls")
elif sorted_defense[0] >= sorted_offense[0] and sorted_defense[1] < sorted_offense[1]:
    print("Defense won 1 and attack won 1")
#elif sorted_defense[0] < sorted_offense[0] and sorted_defense[1] < sorted_offense[1]:
#    print("Offense won both rolls")
else:
    print("Offense won both rolls")