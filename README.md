# 🎲 20x2 Board Game: Python Multiplayer Dice Adventure

## 🌟 Project Overview

A dynamic, interactive two-player board game developed in Python, featuring strategic dice-based movement, black hole challenges, and engaging gameplay mechanics.

## ✨ Game Features

- 🎮 Two-player game (Human vs Computer)
- 🎲 Dice-based movement system
- 🕳️ Black hole challenges
- 📊 Game statistics tracking
- 🏆 Win condition based on reaching or passing the 20th block
- 📝 Automatic game summary file generation

## 🚀 Technologies Used

- Python 3.x
- `random` module for dice rolling
- `tabulate` for creating game board
- `datetime` for timestamp and file naming

## 📋 Game Rules

1. Game starts when a player rolls a 6
2. Players move based on half the dice value
3. Black holes at positions 8 and 15 send players back to start
4. First player to reach or pass block 20 wins
5. Game generates a summary text file after each match

## 🛠️ Setup and Installation

### Prerequisites
- Python 3.x
- `tabulate` library
  ```bash
  pip install tabulate
  ```

### Running the Game
```bash
python board_game.py
```

## 📦 Project Structure
```
20x2-board-game/
│
├── board_game.py       # Main game script
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

## 🎮 Gameplay Mechanics

### Player Movement
- Dice roll determines movement
- Black holes at positions 8 and 15
- Strategic decision-making required

### Winning Conditions
- Reach or pass the 20th block
- First player to achieve wins

## 📊 Game Statistics

After each game, a timestamped text file is generated containing:
- Total moves for each player
- Black hole hits
- Game outcome

## 🔧 Customization

- Easily modify game board size
- Adjust black hole positions
- Implement additional game rules

## 🤝 Contribution

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

MIT License

## 🎯 Future Enhancements

- [ ] Multiplayer support
- [ ] Difficulty levels
- [ ] Enhanced UI
- [ ] Persistent scoring system
