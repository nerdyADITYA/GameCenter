# 🎮 GameCenter

**GameCenter** is a Python-based collection of classic card games, offering an interactive command-line experience. The project includes implementations of popular games such as Blackjack, War, and Old Maid, providing users with a nostalgic gaming experience.

---

## 📁 Repository Structure

```
GameCenter/
├── BlackJack.py     # Implementation of the Blackjack game
├── War.py           # Implementation of the War card game
├── OldMaid.py       # Implementation of the Old Maid game
├── GameCenter.py    # Main script to launch and navigate between games
├── __pycache__/     # Compiled Python files (auto-generated)
└── README.md        # Project documentation
```

### Detailed Breakdown

* **`BlackJack.py`**: Contains the logic for the Blackjack game, including card dealing, score calculation, and game flow control.

* **`War.py`**: Implements the War card game mechanics, handling card distribution, comparison, and determining the winner.

* **`OldMaid.py`**: Features the Old Maid game, managing player turns, card matching, and the elimination process.

* **`GameCenter.py`**: Serves as the entry point for the application, presenting a menu for users to select and play any of the available games.

* **`__pycache__/`**: Directory where Python stores compiled bytecode files. This folder is auto-generated and can be ignored or added to `.gitignore`.

* **`README.md`**: Provides an overview of the project, setup instructions, and other relevant information.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed on your system.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/nerdyADITYA/GameCenter.git
   cd GameCenter
   ```

2. **Run the Game Center**

   ```bash
   python GameCenter.py
   ```

   Follow the on-screen prompts to select and play a game.

---

## 🎯 Gameplay Overview

* **Blackjack**: Play against the dealer, aiming to get as close to 21 as possible without going over.

* **War**: Compete against an opponent by drawing cards; the higher card wins each round.

* **Old Maid**: Match pairs and avoid being left with the unmatchable "Old Maid" card.

Each game is designed for single-player interaction, simulating opponents through programmed logic.

---

## 🛠️ Contributing

Contributions are welcome! If you'd like to enhance the games, fix bugs, or add new features:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

Please ensure your code adheres to Python best practices and includes appropriate documentation.

---

Feel free to customize this `README.md` further to align with any additional features or structural changes in your project.
