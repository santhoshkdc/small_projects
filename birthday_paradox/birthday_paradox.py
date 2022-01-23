import datetime, random, calendar


def getbday(no_of_turns):  # this generates a list of mentioned random birthdays
    birthdays = []
    start_of_year = datetime.date(2001,1,1)  # the origin point to fill up a list of birthdays
    for i in range(int(no_of_turns)):
        birthday = start_of_year + datetime.timedelta(random.randint(0,364))
        birthdays.append(birthday)
    return birthdays


def check_repeats():
    # checks if the birthday in the returned list are unique
    birthdays = getbday(no_of_turns)
    matching_dates = []
    if len(birthdays) == len(set(birthdays)):
        return None  # all the dates are unique

    else:
        for i in birthdays:
            counts = birthdays.count(i)
            if counts >= 2:
                matching_dates.append(i)
        return set(matching_dates)


print("""The Birthday Paradox shows that in a group of N people, the probability of
at least two people having the same birthday is surprisingly large.
""")

while True:
    print("\nHow many do you want in a group? (MAX 100)")
    no_of_turns = input("\n> ")

    if int(no_of_turns) <= 100 and no_of_turns.isdecimal():
        getbday(int(no_of_turns))
        break


print(f"""Here are a list of {no_of_turns} randomly generated birthdays:""")
birthdays = getbday(no_of_turns)
bday_text = ''
for birthday in birthdays:
    bday_text = bday_text + f"{calendar.month_name[birthday.month]} {birthday.day}, "
bday_text = bday_text[0:-2] + '.'
print(f"{bday_text}")
print()
print()

match = check_repeats()

print(f"In this simulation, ", end=" ")
if match != None:
    text = ''
    for birthday in match:
        text = text + f"{calendar.month_name[birthday.month]} {birthday.day}, "
    text = text[0:-2] + '.'
    print(f" multiple people have birthdays on {text}")
else:
    print("no one shares their birthdays")
print()

# now we run a 100_000 simulations to find the most probable probability

print("Let's run a 100_000 simulations to see how big the chances are to get common bdays.")

input("Press Enter to continue")
sim_match = 0
for i in range(1,100_001):
    if i % 1_000 == 0:
        print(f"{i} number of turns completed...")
    match = check_repeats()
    if match != None:
        sim_match += 1
probability = round((sim_match/100_000) * 100,3)

print(f""" So, we have run the simulation 100_000 on a randomly generated {no_of_turns} birthdays.
As a result we have matching birthdays on {sim_match} out of the 100_000 simulations.
The  accounts to a probability of {probability}!!!""")