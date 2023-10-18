import random

repeat = True

while repeat:
    number = random.randint(1, 100)
    guess = 0
    tries = 0

    while guess != number:
        if guess < number:
            print("mēģini lielāku skaitli")
        else:
            print("mēģini mazāku skaitli")

        guess = int(input("uzmini skaitli: "))
        tries += 1
    else:
        if tries < 4:
            print(f"malacis, uzminēji tikai pēc {tries} reizēm!")
        elif tries < 7:
            print(f"nav slikti, uzminēji pēc {tries} reizēm!")
        else:
            print(f"uzminēji pēc veselām {tries} reizēm...")

    response = input("vai gribi turpināt? y/n: ")    
    if response == "y":
        repeat = True
    elif response == "n":
        repeat = False
        print("paldies par spēli")
    else:
        repeat = False
        print("paldies par spēli")
