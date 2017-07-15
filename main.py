from tkinter import *

canvas_width = 500
canvas_height = 500


class Screen:
    def __init__(self, tkmaster, width, height):
        self.canvas = Canvas(tkmaster, width=width, height=height)
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        self.canvas.bind("<B1-Motion>", paint)
        self.canvas.config(highlightbackground="black")


class ColorFrame:
    def __init__(self, tkmaster):
        self.frame = Frame(tkmaster)
        self.frame.grid(row=0, column=1)
        self.colors = ["black", "white", "red", "green", "blue", "yellow"]
        buttons = []
        for i in range(0, len(self.colors)):
            buttons.append(Color(self.frame, self.colors[i], i))


class Color:
    def __init__(self, tkmaster, bcolor, row):
        self.color = bcolor
        self.button = Button(tkmaster, text="      ", command=self.changecolor)
        self.button.config(background=bcolor)
        self.button.grid(row=row, column=0)

    def changecolor(self):
        global color
        color = self.color


def paint(event):
    global canvas, canvas_height, canvas_width
    x, y = event.x, event.y
    dx = canvas_width - x
    dy = canvas_height - y
    canvas.canvas.create_rectangle(x, y, (x + 1), (y + 1), outline=color)
    canvas.canvas.create_rectangle(dx, y, (dx + 1), (y + 1), outline=color)
    canvas.canvas.create_rectangle(x, dy, (x + 1), (dy + 1), outline=color)
    canvas.canvas.create_rectangle(dx, dy, (dx + 1), (dy + 1), outline=color)


def deleteall():
    canvas.canvas.delete("all")

color = "black"

master = Tk()
master.title("lets draw something")

canvas = Screen(master, canvas_width, canvas_height)

colorframe = ColorFrame(master)

message = Label(master, text="press and drag the mouse to draw")
message.grid(row=1, column=0)

delete = Button(master, text="Delete", command=deleteall)
delete.grid(row=1, column=1)
mainloop()
