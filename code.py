class Game():
    def __init__(self):
        self.game_board = [["","",""],["","",""],["","",""]]
        self.status = True
        self.move = 0

    def play(self):
        if self.move % 2 == 0:
            pass
        else:
            pass

        self.move += 1

    def p1chose(self):
        self.game_board_wiev()
        print("Player 1,")
        line = int(input("Enter a line: "))
        column = int(input("Enter a column: "))
    def p2chose(self):
        pass

    def dolumu(self):
        pass

    def game_board_wiev(self):
        for i in self.tahta:
            for j in i:
                print(j,end=" ")

            print("\n")

    def game_control(self):
        pass

game = Game()

while game.status()
