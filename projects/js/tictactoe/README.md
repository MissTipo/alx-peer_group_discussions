# Tic-tac-toe game

Create a tic-tac-toe game that allows users to play against the computer.
Use ES6 classes to define the game board and move objects, and use Promises to handle API requests for game data. Use ES6 data manipulation techniques to check for winning moves and keep track of the game state.

## General structure for the Tic-tac-toe game project using ES6 Basics, Promises, Classes, and Data Manipulation
- Set up the game board:
  - [ ] Create a class called GameBoard that initializes a 3x3 grid with empty squares.
  - [ ] Use the class constructor to create an array of arrays representing the game board, where each inner array represents a row.
  - [ ] Render the game board on the page using HTML and CSS.
- Create game logic:
  - [ ] Create a class called Game that manages the state of the game, including whose turn it is and if the game is over.
  - [ ] Use ES6 data manipulation techniques to check for winning moves, such as using a nested loop to check for three in a row.
- Add methods to the Game class to handle user moves and computer moves.
  - [ ] Use the Game class to update the game state and determine if the game is over.
- Allow users to play against the computer:
  - [ ] Add an event listener to the game board that allows users to make a move.
- Use Promises to handle API requests for game data, such as determining the computer's move.
- Create a class called Computer that generates a move based on the current game state, such as choosing a random empty square.
- Display game results:
  - [ ] Display a message when the game is over, such as "You won!", "Computer won!", or "It's a tie!".
  - [ ] Use the Game class to determine the game result and display the appropriate message.

Overall, the structure of the Tic-tac-toe game project using ES6 Basics, Promises, Classes, and Data Manipulation involves creating classes for the game board, game logic, and computer, using Promises to handle API requests, and using ES6 data manipulation techniques to check for winning moves and update the game state. The game should allow users to play against the computer and display the game results.
