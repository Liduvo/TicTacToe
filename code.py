class Game():

    def __init__(self):
        self.game_board = [["[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]"]]
        self.status = True
        self.move = 0

    def play(self):
        if self.move % 2 == 0:
            self.p1chose()
        else:
            self.p2chose()

        self.status = self.game_control()

        self.move += 1

    def p1chose(self):
        self.game_board_wiev()
        print("Player 1,")

        line = int(input("Enter a line: "))
        while line < 1 or line > 3:
            line = int(input("The number value to be entered can be 1 ,2 and 3."))

        column = int(input("Enter a column: "))
        while line < 1 or line > 3:
            line = int(input("The number value to be entered can be 1 ,2 and 3."))

        if self.is_it_full(line,column):
            self.p1chose()
        else:
            self.game_board[line][column] = "X"

    def p2chose(self):
        self.game_board_wiev()
        print("Player 1,")

        line = int(input("Enter a line: "))
        while line < 1 or line > 3:
            line = int(input("The number value to be entered can be 1 ,2 and 3."))

        column = int(input("Enter a column: "))
        while line < 1 or line > 3:
            line = int(input("The number value to be entered can be 1 ,2 and 3."))

        if self.is_it_full(line,column):
            self.p2chose()
        else:
            self.game_board[line][column] = "0"

    def is_it_full(self,line,column):
        if self.game_board[line][column] != "":
            return True
        else:
            return False

    def game_board_wiev(self):
        for i in self.tahta:
            for j in i:
                print(j,end=" ")

            print("\n")

    def game_control(self):
        if [self.game_board[0][0], self.game_board[0][1], self.game_board[0][2]] == ["X","X","X"] or [self.game_board[0][0], self.game_board[0][1],self,game_board[0][2]] == ["O","O","O"]:
            return False
        
        if [self.game_board[1][0], self.game_board[1][1], self.game_board[1][2]] == ["X","X","X"] or [self.game_board[1][0], self.game_board[1][1], self.game_board[1][2]] == ["O","0","0"]:
            return False
            
        if [self.game_board[2][0], self.game_board[2][1], self.game_board[2][2]] == ["X","X","X"] or [self.game_board[2][0], self.game_board[2][1], self.game_board[2][2]] == ["O","O","O"]:
            return False


        if [self.game_board[0][0], self.game_board[0][1], self.game_board[0][2]] == ["X","X","X"] or [self.game_board[0][0], self.game_board[0][1], self.game_board[0][2]] == ["O","O","O"]:
            return False

        if [self.game_board[1][0], self.game_board[1][1], self.game_board[1][2]] == ["X","X","X"] or [self.game_board[1][0], self.game_board[1][1], self.game_board[1][2]] == ["O","O","O"]:
            return False

        if [self.game_board[2][0], self.game_board[2][1], self.game_board[2][2]] == ["X","X","X"] or [self.game_board[2][0], self.game_board[2][1], self.game_board[2][2]] == ["O","O","O"]:
            return False

        
        if [self.game_board[0][0], self.game_board[1][1], self.game_board[2][2]] == ["X","X","X"] or [self.game_board[0][0], self.game_board[0][1], self.game_board[0][2]] == ["O","O","O"]:
            return False

        if [self.game_board[0][2], self.game_board[1][1], self.game_board[2][0]] == ["X","X","X"] or [self.game_board[0][0], self.game_board[0][1], self.game_board[0][2]] == ["O","O","O"]:
            return False

        return True

        

game = Game()

while game.status():
    Game.play()
