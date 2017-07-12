from tkinter import *

canvas_width = 500
canvas_height = 500


class Screen:
    def __init__(self, tkmaster, width, height):
        self.canvas = Canvas(tkmaster, width=width, height=height)
        self.canvas.pack(expand=YES, fill=BOTH, padx=10, pady=10)
        self.canvas.bind("<B1-Motion>", paint)
        self.canvas.config(highlightbackground="black")

    def draw(self, x, y):
        self.canvas.create_rectangle(x, y, (x + 1), (y + 1), fill="black")


def paint(event):
    x, y = event.x, event.y
    canvas.draw(x, y)
    dx = canvas_width - x
    dy = canvas_height - y
    canvas.draw(x, y)
    canvas.draw(dx, y)
    canvas.draw(x, dy)
    canvas.draw(dx, dy)


master = Tk()
master.title("lets draw something")

canvas = Screen(master, canvas_width, canvas_height, )

message = Label(master, text="press and drag the mouse to draw")
message.pack(side=TOP)

mainloop()
