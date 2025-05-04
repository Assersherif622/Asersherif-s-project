import time

def get_valid_input(prompt, valid_choices):
    
    while True:
        choice = input(prompt).strip().upper()
        if choice in valid_choices:
            return choice
        else:
            print(f"Invalid choice. Please choose from {', '.join(valid_choices)}.")

while True:
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("In this game, you will make choices that affect the outcome of your adventure.")
    time.sleep(1)
    print("Let's begin!")
    time.sleep(1)
    print("You are Captain Elira, a brave adventurer searching for the legendary Treasure of Eldoria hidden deep within the Whispering Jungle.")
    time.sleep(1)
    print("Your journey begins at the jungle's edge where two paths diverge:[Choice 1: Which path do you take?]")
    
    
    playerchoice = get_valid_input(
        "🔹 A) The Overgrown Path: A narrow trail covered in vegetation, clearly dangerous but ancient carvings suggest a hidden temple.\n"
        "🔹 B) The River Route: A fast water passage with an old boat available - faster but riskier.\n",
        ["A", "B"]
    )
    
    if playerchoice == "A":
        time.sleep(1)
        print("You cut through dense foliage, but the ground collapses beneath you! You fall into an underground cave and spot a golden chest... until a giant serpent appears![Choice 2: Face the Serpent]")
        time.sleep(1)
        playerchoice = get_valid_input(
            "🔹 A) Fight: Battle the serpent with your sword.\n"
            "🔹 B) Sneak Past: Try to slip by unnoticed but the serpent senses you!\n",
            ["A", "B"]
        )
        if playerchoice == "A":
            time.sleep(1)
            print("If you defeated the serpent and opened the secret door, you find Eldoria's legendary crown... but the cave begins collapsing! Final Choice:")
            time.sleep(1)
            playerchoice = get_valid_input(
                "🔹 A) Risk grabbing the crown\n"
                "🔹 B) Retreat to save your life\n",
                ["A", "B"]
            )
        elif playerchoice == "B":
            time.sleep(1)
            print("You sneak past the serpent, but it senses you! You find a treasure map leading to the Temple of Eldoria... but the serpent is right behind you!")
            time.sleep(1)
            print("If you found the puzzle box, you discover it's a map to a magical healing spring... until rival explorer Drake Voss ambushes you!")
    elif playerchoice == "B":
        time.sleep(1)
        print("You sail down the river, but a sudden storm capsizes your boat! You wash ashore on a mysterious island with two paths:")
        time.sleep(1)
        playerchoice = get_valid_input(
            "🔹 A) Waterfall: A dangerous adventure that may lead to treasure\n"
            "🔹 B) Lagoon: A safer route that might miss the treasure\n",
            ["A", "B"]
        )
        if playerchoice == "A":
            print("You survive the plunge, but your boat is wrecked. On the shore, you find a wounded jaguar guarding a golden key.")
            time.sleep(1)
            playerchoice = get_valid_input(
                "🔹 A) Heal the jaguar (Uses your last medkit; it may guide or attack you).\n"
                "🔹 B) Take the key by force (Its mate is watching from the trees…).\n",
                ["A", "B"]
            )
    
    # Replay option
    playerchoice = get_valid_input("Would you like to play again? (yes/no): ", ["YES", "NO"])
    if playerchoice == "NO":
        print("Thank you for playing!")
        break