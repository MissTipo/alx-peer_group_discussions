# Tic-tac-toe game project using ES6 Basics, Promises, Classes, and Data Manipulation

## Project Overview

This project involves creating a Tic-tac-toe game using ES6 Basics, Promises, Classes, and Data Manipulation. The game will allow users to play against the computer and use ES6 data manipulation techniques to check for winning moves and keep track of the game state.

## Project Structure

1. Set up the game board:
- Create a class called `GameBoard` that initializes a 3x3 grid with empty squares.
- Use the class constructor to create an array of arrays representing the game board, where each inner array represents a row.
- Render the game board on the page using HTML and CSS.

2. Create game logic:
- Create a class called `Game` that manages the state of the game, including whose turn it is and if the game is over.
- Use ES6 data manipulation techniques to check for winning moves, such as using a nested loop to check for three in a row.
- Add methods to the `Game` class to handle user moves and computer moves.
- Use the `Game` class to update the game state and determine if the game is over.

3. Allow users to play against the computer:
- Add an event listener to the game board that allows users to make a move.
- Use Promises to handle API requests for game data, such as determining the computer's move.
- Create a class called `Computer` that generates a move based on the current game state, such as choosing a random empty square.

4. Display game results:
- Display a message when the game is over, such as "You won!", "Computer won!", or "It's a tie!".
- Use the `Game` class to determine the game result and display the appropriate message.

## How to Play Tic-tac-toe

Tic-tac-toe is a two-player game where each player takes turns placing either an X or an O on a 3x3 grid. The goal is to get three in a row (horizontally, vertically, or diagonally) before the other player does. The game ends in a tie if all nine squares are filled without a winner.

To play Tic-tac-toe:
1. Draw a 3x3 grid on a piece of paper or use a digital version of the game board.
2. Decide which player will be X and which will be O.
3. The player with X goes first and places an X on any empty square on the grid.
4. The player with O goes next and places an O on any empty square on the grid.
5. Players continue taking turns until either one player gets three in a row or all nine squares are filled.
6. If a player gets three in a row, they win the game.
7. If all nine squares are filled without a winner, the game ends in a tie.
