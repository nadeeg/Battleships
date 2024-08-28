
# Battleship Game

This is a Python-based, simplified version of the Battleship game that can be played between two players over a network. Only one game session can be active at a time, and the game supports a maximum of two concurrent players. Each ship is limited to a maximum length of 1.

The number of ships, rows, and columns (i.e., the battleship map configuration) can be customized by modifying the `Constants.py` file.

## How to Start the Game

1. **Start the Server:**
   Navigate to the `server` directory and run the following command:
   ```bash
   python3 Server.py

2. Start the Clients:
   Each client can be started by navigating to the client directory and running the following command:
   ```bash
   python3 Client.py
