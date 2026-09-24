import random


class RockPaperScissors:
    """Manage a game of Rock, Paper, Scissors."""

    choices = ("rock", "paper", "scissors")
    winning_choices = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    def __init__(self) -> None:
        self._computer_choice = ""

    def choose_computer_choice(self) -> str:
        """Return a randomly selected computer choice."""
        self._computer_choice = random.choice(self.choices)
        return self._computer_choice

    def play_round(self, user_choice: str) -> str:
        """Play one round and return ``win``, ``lose``, or ``tie``."""
        user_choice = user_choice.strip().lower()

        if user_choice not in self.choices:
            raise ValueError(
                f"Invalid choice: {user_choice!r}. "
                f"Choose one of: {', '.join(self.choices)}."
            )

        computer_choice = self.choose_computer_choice()
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            return "tie"

        if self.winning_choices[user_choice] == computer_choice:
            return "win"

        return "lose"

    def main(self) -> None:
        """Run the interactive game until the user chooses to stop."""
        print("Welcome to Rock, Paper, Scissors!")

        while True:
            user_choice = input("Choose rock, paper, or scissors: ")

            try:
                result = self.play_round(user_choice)
            except ValueError as error:
                print(error)
                continue

            if result == "win":
                print("You win!")
            elif result == "lose":
                print("You lose!")
            else:
                print("It is a tie!")

            play_again = input("Play again? (yes/no): ").strip().lower()
            if play_again not in {"yes", "y"}:
                print("Thanks for playing!")
                break


if __name__ == "__main__":
    RockPaperScissors().main()
