#include <iostream>
#include <vector>

std::vector<std::vector<std::string>> emptyBoard = {{"   ", "   ", "   "},
                                                    {"   ", "   ", "   "},
                                                    {"   ", "   ", "   "}};

                                                        
int playerSpotNum;
std::string player;
std::string playerOneName = "Ahmed";
std::string playerTwoName = "Dhan";
int counter = 0;
std::string X = " X ";
std::string O = " O ";
int iPos;
int jPos;

// This function prints out the introduction and allows players to enter their names.
void introduction() {
  std::cout << "Welcome to Tic-Tac-Toe! The players can play as many rounds as they want. If you want to exit the game press Ctrl + C. \n\n";
  // std::cout << "Player 1 is assigned X >> Enter your name: ";
  // std::cin >> playerOneName;
  // std::cout << "\n";
  // std::cout << "Player 2 is assigned O >> Enter your name: ";
  // std::cin >> playerTwoName;
  std::cout << "\n";
  std::cout << "Let's begin!\n\n";
}

// This function draws the initial board and the initial available positions.
void drawBoard(std::vector<std::vector<std::string>> gameBoard) {
  std::cout << "     |     |     \n";
  for (int i = 0; i < gameBoard.size(); i++) {
    for (int j = 0; j < gameBoard[i].size(); j++) {
      if (j == 1 || j == 2) {
        std::cout << " |";
      }
      std::cout << " " << gameBoard[i][j];
      if (j > 1 and j % 2 == 0) {
        std::cout << "\n";
        if ((j > 1 and j % 2 == 0) && i != 2) {
          std::cout << "-----|-----|-----\n";
        } else if (i == 2) {
          std::cout << "     |     |     \n";
        }
      }
    }
  }
}

// This function redraws the board after each turn.
void updateBoardDrawing(std::vector<std::vector<std::string>> gameBoard, std::vector<std::vector<std::string>> gameBoardPositions) {
  std::cout << "Available Spots: \n\n";
  drawBoard(gameBoardPositions); // draws the board.
  std::cout << "\n";
  std::cout << "Game Board: \n\n";
  drawBoard(gameBoard); // draws the available positions on the board.
  std::cout << "\n";
}

// This function asks the player to input their X or O choice.
void askPlayer() {
  std::cout << "\n";
  std::cout << "Enter the spot number: ";
  std::cin >> playerSpotNum;
}

// This function returns a vector (list) which stores the i,j indices that ensures the right spot on the board (as in boardPositions above) is selected.
std::vector<int> boardPosition(int spotNum) {
  int i;
  int j;
  if (spotNum == 1) {
    i = 0;
    j = 0;
  } else if (spotNum == 2) {
    i = 0;
    j = 1;
  } else if (spotNum == 3) {
    i = 0;
    j = 2;
  } else if (spotNum == 4) {
    i = 1;
    j = 0;
  } else if (spotNum == 5) {
    i = 1;
    j = 1;
  } else if (spotNum == 6) {
    i = 1;
    j = 2;
  } else if (spotNum == 7) {
    i = 2;
    j = 0;
  } else if (spotNum == 8) {
    i = 2;
    j = 1;
  } else if (spotNum == 9) {
    i = 2;
    j = 2;
  }
  return {i, j};
}

// This function checks that the player has entered a valid spot number.
bool checkSpotNumIsCorrect (int playerSpotNum) {
  if (playerSpotNum >= 1 && playerSpotNum <= 9) {
    return true; // spot number is within correct range.
  } else {
    return false; // spot number is not within correct range.
  }
}

// This function re-checks that the player has entered a valid spot number if the player selected a spot number that is already occupied.
void checkSpotNumIsCorrectAgain() {
  std::cout << "\n";
  std::cout << "You have entered an invalid spot number. Please enter a spot number from 1 - 9. \n";
  askPlayer();
}

// This function checks if a spot is already occupied.
bool checkSpotIsOccupied (std::vector<std::vector<std::string>> gameBoard, int playerSpotNum) {
  int i = boardPosition(playerSpotNum)[0];
  int j = boardPosition(playerSpotNum)[1];
  if (gameBoard[i][j] == X || gameBoard[i][j] == O) {
    return true; // spot is occupied.
  }
  return false; // spot is available.
}

// This function asks the player to choose a different spot.
void spotIsOccupied() {
  std::cout << "\n";
  std::cout << "This spot is already occupied! Select another one. \n";
  askPlayer();
}

// This updates the board and the available spots on the board.
std::vector<std::vector<std::string>> updateBoard(std::vector<std::vector<std::string>> gameBoard) {

  // This if-else block keeps track of the players name and input after each turn.
  if (counter % 2 == 0) {
      player = X;
      std::cout << "It's player 1 (" << playerOneName << "'s) turn! \n";
    } else {
      player = O; // set to O.
      std::cout << "It's player 2 (" << playerTwoName << "'s) turn! \n";    
    }

  askPlayer();

  // These nested while loops ensure the player has entered a valid spot number ensuring that the spot itself is also not occupied.
  while ((checkSpotNumIsCorrect(playerSpotNum) == false) && playerSpotNum != 0) {
    checkSpotNumIsCorrectAgain();
  } 

  while (checkSpotIsOccupied(gameBoard, playerSpotNum) == true) {
    spotIsOccupied();    
    while ((checkSpotNumIsCorrect(playerSpotNum) == false) && playerSpotNum != 0)
    {
      checkSpotNumIsCorrectAgain();
    } 
  } 

  // Update playing board with player selection.
  iPos = boardPosition(playerSpotNum)[0];
  jPos = boardPosition(playerSpotNum)[1];
  gameBoard[iPos][jPos] = player;
  counter++;
  std::cout << "\n";
  return gameBoard;
}

// This function checks if the player (X or O) won.
bool checkWin (std::vector<std::vector<std::string>> gameBoard) {

  // horizontal check.
  for (int i = 0; i < gameBoard.size(); i++) {
    if (gameBoard[i][0] == player && gameBoard[i][1] == player && gameBoard[i][2] == player) {
      if (player == X) {
        std::cout << "Game Ended! Player 1 (" << playerOneName << ") wins!";
        return true;
      } else {
        std::cout << "Game Ended! Player 2 (" << playerTwoName << ") wins!";
        return true;
      }
    }
  }

  // vertical check.
  for (int j = 0; j < gameBoard.size(); j++) {
    if (gameBoard[0][j] == player && gameBoard[1][j] == player && gameBoard[2][j] == player) {
    if (player == X) {
        std::cout << "Game Ended! Player 1 (" << playerOneName << ") wins!";
        return true;
      } else {
        std::cout << "Game Ended! Player 2 (" << playerTwoName << ") wins!";
        return true;
      }
    }
  }

  // diagonal check.
  if ((gameBoard[0][0] == player && gameBoard[1][1] == player && gameBoard[2][2] == player) || (gameBoard[0][2] == player && gameBoard[1][1] == player && gameBoard[2][0] == player)) {
  if (player == X) {
      std::cout << "Game Ended! Player 1 (" << playerOneName << ") (X) wins!";
      return true;
    } else {
      std::cout << "Game Ended! Player 2 (" << playerTwoName << ") (O) wins!";
      return true;
    }
  }
  return false;
}

// prints Game Over!
void End() {
  std::cout << "\n\n";
  std::cout << "Game Over! \n\n";
  std::cout << "New Game! \n";
}

// This function resets the boards for another new game.
std::vector<std::vector<std::string>> resetGameBoard(std::vector<std::vector<std::string>> gameBoard) {
  gameBoard = emptyBoard;
  counter = 0;
  return gameBoard;
}
