import random

# We are going to create a Rock, Paper, Scissors game with OOP

class RockPaperScissorsGame:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0

    def play_round(self, player_choice):
        # Validate player's choice 
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            return
        
        # Computer's random choice
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Determine winner
        if player_choice == computer_choice:
            result = "tie"
        elif(
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
        ):
            result = "win"
            self.player_score += 1
        else:
            result = "loss"
            self.computer_score += 1
        
        # Display results
        print(f"Player: {player_choice} vs Computer: {computer_choice}")

        # Update rounds played
        self.rounds_played += 1
    
    def display_score(self):
        print(f"Player: {self.player_score} vs Computer: {self.computer_score}")
    

# Main game loop
if __name__ == "__main__":
    game = RockPaperScissorsGame()

    while True:
        # Get player's choice
        player_choice = input("Please enter your choice (rock, paper, scissors): ")

        # Play a round
        game.play_round(player_choice)
        game.display_score()

        # Ask if player wants to play again
        play_again = input("Would you like to play again? (y/n): ")
        if play_again.lower() != "y":
            # Display final score
            game.display_score()
            break
    
    print("Thanks for playing!")