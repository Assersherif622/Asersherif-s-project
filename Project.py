import time
import random  # Random module for random events


def get_valid_input(prompt, valid_choices):
    """
    Prompt the user until they provide a valid input.
    :param prompt: The input prompt to display.
    :param valid_choices: A list of valid input choices.
    :return: The valid input provided by the user.
    """
    while True:
        # Get user input and convert it to uppercase for consistency
        choice = input(prompt).strip().upper()
        if choice in valid_choices:
            return choice  # Return valid input
        else:
            # Inform the user about invalid input
            print(f"Invalid choice. Please choose from {', '.join(valid_choices)}.")


def introduction():
    """
    Display the introduction to the game.
    """
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("In this game, you will make choices that affect the outcome of your adventure.")
    time.sleep(1)
    print("Let's begin!")
    time.sleep(1)
    print(
        "You are Captain Elira, a brave adventurer searching for the legendary "
        "Treasure of Eldoria hidden deep within the Whispering Jungle."
    )
    time.sleep(1)


def first_choice(score):
    """
    Handle the first choice in the game.
    :param score: The player's current score.
    :return: The player's choice and updated score.
    """
    print(
        "Your journey begins at the jungle's edge where two paths diverge:"
        "[Choice 1: Which path do you take?]"
    )
    playerchoice = get_valid_input(
        "🔹 A) The Overgrown Path: A narrow trail covered in vegetation, clearly "
        "dangerous but ancient carvings suggest a hidden temple.\n"
        "🔹 B) The River Route: A fast water passage with an old boat available - "
        "faster but riskier.\n",
        ["A", "B"]
    )
    if playerchoice == "A":
        score += 50  # Reward for choosing the adventurous path
    elif playerchoice == "B":
        score += 25  # Smaller reward for choosing the safer path
    return playerchoice, score


def overgrown_path(score):
    """
    Handle the events for the Overgrown Path.
    :param score: The player's current score.
    :return: Updated score.
    """
    time.sleep(1)
    print(
        "You cut through dense foliage, but the ground collapses beneath you! "
        "You fall into an underground cave and spot a golden chest... until a "
        "giant serpent appears![Choice 2: Face the Serpent]"
    )
    time.sleep(1)
    playerchoice = get_valid_input(
        "🔹 A) Fight: Battle the serpent with your sword.\n"
        "🔹 B) Sneak Past: Try to slip by unnoticed but the serpent senses you!\n",
        ["A", "B"]
    )
    if playerchoice == "A":
        # Use random.choice to determine the outcome of the fight
        outcome = random.choice(["win", "lose"])
        if outcome == "win":
            score += 50  # Reward for bravery
            print(
                "You defeated the serpent and opened the secret door to find "
                "Eldoria's legendary crown!"
            )
        else:
            print("The serpent overpowers you, and you barely escape with your life!")
            score -= 20  # Penalty for losing the fight
    elif playerchoice == "B":
        score += 25  # Smaller reward for sneaking past
        print(
            "You sneak past the serpent, but it senses you! You find a treasure map "
            "leading to the Temple of Eldoria... but the serpent is right behind you!"
        )
    return score


def river_route(score):
    """
    Handle the events for the River Route.
    :param score: The player's current score.
    :return: Updated score.
    """
    time.sleep(1)
    print(
        "You sail down the river, but a sudden storm capsizes your boat! You wash "
        "ashore on a mysterious island with two paths:"
    )
    time.sleep(1)
    playerchoice = get_valid_input(
        "🔹 A) Waterfall: A dangerous adventure that may lead to treasure\n"
        "🔹 B) Lagoon: A safer route that might miss the treasure\n",
        ["A", "B"]
    )
    if playerchoice == "A":
        # Use random.choice to determine if the jaguar attacks or helps
        jaguar_outcome = random.choice(["help", "attack"])
        if jaguar_outcome == "help":
            score += 50  # Reward for helping the jaguar
            print("You heal the jaguar, and it leads you to a hidden treasure!")
        else:
            print("The jaguar attacks you, and you barely escape!")
            score -= 20  # Penalty for being attacked
    elif playerchoice == "B":
        score += 25  # Smaller reward for taking the safer route
        print("You take the lagoon route and find a small chest with some gold coins.")
    return score


def check_win_lose(total_score):
    """
    Evaluate if the game should end based on the total score.
    :param total_score: The player's total score across all sessions.
    :return: True if the game should end, False otherwise.
    """
    if total_score >= 100:  # Ends the game when the score hits 100 or more
        print("Game Over! Congratulations, you've reached the goal.")
        return True
    elif total_score < 0:  # Ends the game if the score drops below 0
        print("Game Over! Unfortunately, your score fell too low.")
        return True
    return False


def replay():
    """
    Ask the player if they want to replay the game.
    """
    while True:
        choice = input("Enter yes or no: ").strip().lower()
        if choice == 'yes':
            print("You answered yes.")
            return "YES"
        elif choice == 'no':
            print("You answered no.")
            return "NO"
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")


# Main Game Loop
total_score = 0  # Initialize the total score across all sessions

while True:
    score = 0  # Initialize the score for the current session
    introduction()
    playerchoice, score = first_choice(score)

    if playerchoice == "A":
        score = overgrown_path(score)
    elif playerchoice == "B":
        score = river_route(score)

    # Update the total score
    total_score += score

    # Display the scores
    print(f"Your score for this session is: {score}")
    print(f"Your total score across all sessions is: {total_score}")

    # Check if the game should end based on the total score
    if check_win_lose(total_score):
        break

    # Ask the player if they want to replay
    if replay() == "NO":
        print("Thank you for playing!")
        break