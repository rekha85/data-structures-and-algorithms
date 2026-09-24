import sys
import unittest
from pathlib import Path
from unittest.mock import patch


SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from leetcode.algorithms.common.rockpaperscissor import RockPaperScissors


class TestRockPaperScissors(unittest.TestCase):
    def setUp(self):
        self.game = RockPaperScissors()

    @patch(
        "leetcode.algorithms.common.rockpaperscissor.random.choice",
        return_value="scissors",
    )
    def test_choose_computer_choice(self, mock_choice):
        self.assertEqual(self.game.choose_computer_choice(), "scissors")
        mock_choice.assert_called_once_with(self.game.choices)

    @patch(
        "leetcode.algorithms.common.rockpaperscissor.random.choice",
        return_value="scissors",
    )
    def test_rock_beats_scissors(self, _mock_choice):
        self.assertEqual(self.game.play_round("rock"), "win")

    @patch(
        "leetcode.algorithms.common.rockpaperscissor.random.choice",
        return_value="rock",
    )
    def test_paper_beats_rock(self, _mock_choice):
        self.assertEqual(self.game.play_round("paper"), "win")

    @patch(
        "leetcode.algorithms.common.rockpaperscissor.random.choice",
        return_value="paper",
    )
    def test_scissors_beats_paper(self, _mock_choice):
        self.assertEqual(self.game.play_round("scissors"), "win")

    @patch(
        "leetcode.algorithms.common.rockpaperscissor.random.choice",
        return_value="rock",
    )
    def test_returns_lose_when_computer_wins(self, _mock_choice):
        self.assertEqual(self.game.play_round("scissors"), "lose")

    @patch(
        "leetcode.algorithms.common.rockpaperscissor.random.choice",
        return_value="paper",
    )
    def test_returns_tie_for_same_choice(self, _mock_choice):
        self.assertEqual(self.game.play_round(" PAPER "), "tie")

    def test_rejects_invalid_choice(self):
        with self.assertRaises(ValueError):
            self.game.play_round("lizard")


if __name__ == "__main__":
    unittest.main()
