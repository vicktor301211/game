from tkinter import *
from menu import *


def set_status(text, color='black'):
    pass
def key_handler(event):
    pass

def check_finish():
    pass


game_width =
game_height =


player_size =
x1, y1 = 50, 50
x2, y2 = x1, y1 + player_size + 100
player1_color =
player2_color =

KEY_PLAYER1 =
KEY_PLAYER2 =

game_over =

SPEED =

x_finish = game_width - 50

game_width =
game_height =
window = Tk()
window.title('Меню игры')

canvas = Canvas(window, width=game_width, height=game_height, bg='white')
canvas.pack()
player1 = canvas.create_rectangle(x1,
                                  y1,
                                  x1 + player_size,
                                  y1 + player_size,
                                  fill=player1_color)
player2 = canvas.create_rectangle(x2,
                                  y2,
                                  x2 + player_size,
                                  y2 + player_size,
                                  fill=player2_color)
finish_id = canvas.create_rectangle(x_finish,
                                    0,
                                    x_finish + 10,
                                    game_height,
                                    fill='black')

text_id = canvas.create_text(x1,
                             game_height - 50,
                             anchor=SW,
                             font=('Arial', '25'),
                             text='Вперед!')


window.bind('<KeyRelease>', key_handler)
window.mainloop()