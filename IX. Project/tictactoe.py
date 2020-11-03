import tkinter

from tictactoe_game_engine import TIctactoeGameEngine

class Tictactoe:
    def __init__(self):
        self.game_engine = TIctactoeGameEngine()

    def play(self):
        print(self.game_engine) #show board

        #무한반복
        while True:

            #input row, col
            row = int(input('row : '))
            col = int(input('col : '))

            #set
            self.game_engine.set(row, col)

            #show board
            print(self.game_engine)

            winner = self.game_engine.check_winner()

            #check_winner 승패가 결정나면, break
            if winner != None: #in "OXd"
                break

        #결과 출력
        if winner == 'O':
            print('O 이김')
        elif winner == 'X':
            print('X 이김')
        elif winner == 'd':
            print('무승부')

class TictactoeGUI:
    def __init__(self):
        self.geme_engine = TIctactoeGameEngine()
        self.init_ui()

    def init_ui(self):
        self.CANVAS_SIZE = 300
        self.root = tkinter.Tk()
        self.root.title(' 틱 택 토 ')
        self.root.geometry(str(self.CANVAS_SIZE)+'x'+str(self.CANVAS_SIZE)) #'300x300'
        self.canvas = tkinter.Canvas(self.root, bg='white', width=self.CANVAS_SIZE, height=self.CANVAS_SIZE)
        self.canvas.pack()

        #{'0' : PhotoImage객체, 'X' : PhotoImage객체}
        self.images = {}    #dict
        self.images['O'] = tkinter.PhotoImage(file = 'O.gif')
        self.images['X'] = tkinter.PhotoImage(file = 'X.gif')

    def play(self):
        self.canvas.create_image(0, 0, anchor='nw', image=self.images['O'])
        self.canvas.create_image(200, 200, anchor='nw', image=self.images['X'])
        self.root.mainloop()


if __name__ == '__main__':
    ttt = TictactoeGUI()
    ttt.play()