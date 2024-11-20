# Shea Oliver
# 11/18/2024
# P5HW
# Use functions to create a game with characters
'''concept: create a game called poverty simulator where users start with a set amount of money and are given the option to purchase lottery tickets for $5. Users start with a set amount of money and "stamina" and the end goal is to cash out with the most money. If players are running low on money, they can complete jobs to earn a$155, at the cost of 10 stamina. Purchasing a lottery ticket also requires some effort, taking a smaller amount of stamina from 2-5. If a player reaches 0 or less stamina, they can no longer take turns. In summary, each turn gives an option to either purchase a lottery ticket, work, or "cash out", completing that player's gameplay and allowing the other player to continue taking turns until they are done.
'''
import random

def create_character():
    """
    Create a game character by getting name and stamina from user input.
    
    Returns:
    dict: A dictionary representing the game character
    """
    name = input("Enter player name: ").strip()
    stamina = int(input("Enter player stamina: "))
    money = int(input("Enter player money: "))

    
    player = {
        "name": name,
        "stamina": stamina,
        "money": money
    }
    
    return player    
def display_character(player):
    """
    Displays the current attributes of a player.
    
    Args:
    player (dict): The player dictionary containing name, stamina, and money
    """
    print(f"Character: {player['name']}")
    print(f"Stamina: {player['stamina']}")
    print(f"Money: ${player['money']}")

def take_turn(player):
    """
    Allows a player to take a turn in the game.
    
    Args:
    player (dict): The player dictionary containing name, stamina, and money
    
    Returns:
    dict: Updated player dictionary
    """
    if player['stamina'] <= 0:
        print(f"{player['name']} is out of stamina and cannot take a turn.")
        return player
    
    print(f"\n{player['name']}'s turn")
    print("Options:")
    print("1. Buy Lottery Ticket (5 money, 5% chance to win 200, costs 2-5 stamina)")
    print("2. Work (earn 15 money, costs 10 stamina)")
    print("3. Cash Out")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        if player['money'] < 5:
            print("Not enough money to buy a lottery ticket!")
            return player
        
        player['money'] -= 5
        stamina_used = random.randint(2, 5)
        player['stamina'] -= stamina_used
        
        if random.random() < 0.05:  # 5% chance
            print("Congratulations! You won the lottery!")
            player['money'] += 200
        else:
            print("Sorry, no luck this time.")
    
    elif choice == '2':
        if player['stamina'] < 10:
            print("Not enough stamina to work!")
            return player
        
        player['stamina'] -= 10
        player['money'] += 15
        print("Worked and earned 15 money. Stamina used: 10")
    
    elif choice == '3':
        print(f"{player['name']} has cashed out.")
        player['active'] = False
    
    else:
        print("Invalid choice. Turn skipped.")
    
    return player


# Define the main
def main():
    print("Game is starting....")
    print("\n\n\n")
    
    # Create two characters
    print("Create first player: ")
    player1 = create_character()
    player1['active'] = True
    
    print("\nCreate second player: ")
    player2 = create_character()
    player2['active'] = True

    # Game loop
    while player1['active'] or player2['active']:
        # Player 1's turn
        if player1['active']:
            player1 = take_turn(player1)
            display_character(player1)
            
            # Check if player 1 is now inactive
            if player1['stamina'] <= 0:
                player1['active'] = False
        
        # Player 2's turn
        if player2['active']:
            player2 = take_turn(player2)
            display_character(player2)
            
            # Check if player 2 is now inactive
            if player2['stamina'] <= 0:
                player2['active'] = False

    # Determine and announce the winner
    if player1['money'] > player2['money']:
        print(f"{player1['name']} wins with ${player1['money']}!")
    elif player2['money'] > player1['money']:
        print(f"{player2['name']} wins with ${player2['money']}!")
    else:
        print("It's a tie!")



# Call the main
if __name__ == "__main__":
    main()

