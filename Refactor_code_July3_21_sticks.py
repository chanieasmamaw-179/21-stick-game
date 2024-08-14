from colorama import init, Fore, Style

# Initialize colorama for colored terminal output
init(autoreset=True)


def bot_move(sticks):
	"""
	Determines the number of sticks the bot should take to always win.
	The bot aims to leave a multiple of 4 sticks to the opponent.

	Args:
	sticks (int): The current number of sticks in the pile.

	Returns:
	int: The number of sticks the bot will take (1-3).
	"""
	if sticks % 4 == 0:
		return 3
	elif sticks % 4 == 3:
		return 2
	elif sticks % 4 == 2:
		return 1
	else:
		return 1  # If sticks % 4 == 1, take 1 stick to continue with the strategy


def main():
	"""
	The main function to play the game of sticks.
	It initializes the game, takes player inputs, and alternates turns between the bot and the human player.
	"""
	sticks = 21  # Initial number of sticks
	print("From 21 sticks, choose to take 1-3 sticks at a time.")
	print("The one who takes the last stick wins.")
	
	player1 = f"{Fore.RED}Bot{Style.RESET_ALL}"  # The bot's name with red color
	player2 = f"{Fore.GREEN}" + input(
		"Enter name of Player 2: ") + f"{Style.RESET_ALL}"  # Player 2's name in green color
	
	current_player = player1  # Start with the bot
	
	while True:
		print(f"Sticks in the pile: {Fore.YELLOW}{sticks}{Style.RESET_ALL}")  # Display the current number of sticks
		
		if current_player == player1:
			sticks_taken = bot_move(sticks)  # Bot decides how many sticks to take
			print(f"{current_player} takes {Fore.CYAN}{sticks_taken}{Style.RESET_ALL} sticks.")
		else:
			sticks_taken = int(
				input(f"{current_player}, take sticks (1-3): "))  # Player 2 decides how many sticks to take
			if sticks_taken < 1 or sticks_taken > 3:
				print("Invalid choice, you must take between 1 and 3 sticks.")  # Validate the number of sticks taken
				continue  # If invalid, prompt again
		
		sticks -= sticks_taken  # Update the number of sticks in the pile
		
		if sticks <= 0:
			print(
				f"{current_player} took the last stick. {Fore.GREEN}{current_player} wins!{Style.RESET_ALL}")  # Announce the winner
			break  # End the game
		
		# Switch player
		if current_player == player1:
			current_player = player2  # Switch to Player 2
		else:
			current_player = player1  # Switch to the bot (Player 1)


if __name__ == "__main__":
	main()  # Run the main function to start the game
