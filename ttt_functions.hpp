void introduction();
void drawBoard(std::vector<std::vector<std::string>> gameBoard);
void updateBoardDrawing(std::vector<std::vector<std::string>> gameBoard, std::vector<std::vector<std::string>> gameBoardPositions);
void askPlayer();
std::vector<int> boardPosition(int spotNum) ;
bool checkSpotNumIsCorrect (int playerSpotNum);
void checkSpotNumIsCorrectAgain();
bool checkSpotIsOccupied (std::vector<std::vector<std::string>> gameBoard, int playerSpotNum);
std::vector<std::vector<std::string>> updateBoard(std::vector<std::vector<std::string>> gameBoard); 
std::vector<std::vector<std::string>> updateBoardPositions(std::vector<std::vector<std::string>> gameBoardPositions);
bool checkWin (std::vector<std::vector<std::string>> gameBoard);
std::vector<std::vector<std::string>> resetGameBoard(std::vector<std::vector<std::string>> gameBoard);