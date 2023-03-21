"""Choose your own adventure: Star Wars Edition."""

__author__ = "730570597"

from random import randint

points: int
player: str
SNOWFLAKE: str = "\U00002744"
TREE: str = "\U0001F332"
EXIT: str = "\U0001F6D1"
TROPHY: str = "\U0001F3C6"
SAD: str = "\U0001F622"
GUN: str = "\U0001F52B"
DICE: str = "\U0001F3B2"
BOMB: str = "\U0001F4A3"
SHIELD: str = "\U0001F6E1"


def main() -> None:
    """Main Function containing gameloop. User has 3 options: Game 1, Game 2, or Exit. Points displayed at the end of each round. If player exits game with 5 or more points they win. If not, they lose."""
    global points
    points = 0
    global player
    player = ""
    input_check: bool = True
    greet()
    while (input_check is True):
        game_choice: str = input(f"Select an option: 1-Hoth {SNOWFLAKE}, 2-Endor {TREE}, or 3-Exit the game? {EXIT} ")
        if (game_choice == "1"):
            hoth()
            print(f"Your Points: {points}")
        elif (game_choice == "2"):
            points = endor(points)
            print(f"Your Points: {points}")
        elif (game_choice == "3"):
            input_check = False
        else:
            print("Please provide a valid input.")
    print(f"Your Points: {points}")
    if (points >= 5):
        print(f"Congratulations {player}! You've defeated the empire. {TROPHY}")
    elif (points < 5):
        print(f"{player}, due to your incompetence the empire has succeeded and our forces have been eradicated. {SAD}")


def greet() -> None:
    """Tells user the rules of the games and gives them their options."""
    print("Welcome to Star Wars: Battle for the Republic!\nIn this game you can take to the skies of Hoth and battle empire ships or escape stormtroopers on Endor.")
    print(f"On Hoth, you will have 3 options for engaging the enemy. Choose wisely. {GUN}")
    print(f"On Endor, you will be tasked with increasing or decreasing your speed by rolling a die. Too fast and you crash. Too slow and you're caught. {DICE}")
    global player
    player = input("What is your name? ")


def hoth() -> None:
    """Defending Hoth airspace from Empire attack. Like Rock, Paper, Scissors. Shoot beats bomb, bomb beats shield, and shield beats shoot."""
    global points
    global player
    input_check: bool = True
    while (input_check is True):
        enemy: int = randint(0, 30)
        enemy_choice: str = ""
        if (enemy <= 10):
            enemy_choice = "shoot"
        elif (enemy > 10 and enemy <= 20):
            enemy_choice = "bomb"
        elif (enemy > 20 and enemy <= 30):
            enemy_choice = "shield"
        player_choice: str = input(f"Welcome {player}! Do you wish to shoot {GUN}, bomb {BOMB}, or shield {SHIELD}? ")
        if (player_choice == enemy_choice):
            print("You made the wrong choice! The enemy remains at large.")
            input_check = False
        elif (player_choice == "shoot"):
            if (enemy_choice == "bomb"):
                print("You shot the enemy down!")
                points += 1
            elif (enemy_choice == "shield"):
                print(f"The enemy repelled your attack back at you! Return to base {player}.")
            input_check = False
        elif (player_choice == "bomb"):
            if (enemy_choice == "shield"):
                print("You destroyed the enemy's shield!")
                points += 1
            elif (enemy_choice == "shoot"):
                print(f"The enemy shot you down! Return to base {player}.")
            input_check = False
        elif (player_choice == "shield"):
            if (enemy_choice == "shoot"):
                print("You repelled the enemy's attack back at them!")
                points += 1
            elif (enemy_choice == "bomb"):
                print(f"The enemy destroyed your shield! Return to base {player}.")
            input_check = False
        else:
            print("Please enter a valid input")


def endor(points: int) -> int:
    """Escaping stormtroopers on the surface of Endor. Similar to blackjack. If player or computer exceeds 21, they automatically lose. If player's final number is greater than computer's, player wins."""
    global player
    player_sum: int = 0
    enemy_sum: int = 0
    while (player_sum <= 21 and enemy_sum <= 21):
        dice_roll: int = input(f"{player}, would you like to roll the die? Select Yes or No. {DICE} ")
        if (dice_roll != "Yes"):
            if (dice_roll != "No"):
                print("Please enter a valid input.")
        if (dice_roll == "Yes"):
            player_sum += randint(1, 6)
            enemy_sum += randint(1, 6)
            print(f"Your Speed: {player_sum}")
        elif (dice_roll == "No"):
            if (player_sum > enemy_sum):
                print(f"Your Speed: {player_sum}")
                print(f"Enemy Speed: {enemy_sum}")
                print("You were able to escape from the stormtroopers!")
                points += 1
                return points
            elif (player_sum <= enemy_sum):
                print(f"Your Speed: {player_sum}")
                print(f"Enemy Speed: {enemy_sum}")
                print("You were too slow! The stromtroopers caught you.")
                return points
    if (player_sum > 21):
        print("You went too fast and crashed! The enemy has caught you.")
        return points
    if (enemy_sum > 21):
        print("The enemy went too fast and crashed! You escaped.")
        points += 1
        return points

if __name__ == "__main__":
    main()