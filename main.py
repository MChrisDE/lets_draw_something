from tkinter import *

canvas_width = 250
canvas_height = 250


class Screen:
    def __init__(self, tkmaster, width, height):
        self.canvas = Canvas(tkmaster, width=width, height=height)
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        self.canvas.bind("<B1-Motion>", paint)
        self.canvas.config(highlightbackground="black")
        self.counter = 0

    def draw(self, x, y):
        global color
        self.counter += 1
        print(self.counter)
        self.canvas.create_rectangle(x, y, (x + 1), (y + 1), outline=color)


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
        print(color)


def paint(event):
    # fixme: less often called when there are more objects
    x, y = event.x, event.y
    canvas.draw(x, y)
    dx = 250 - x
    dy = 250 - y
    canvas.draw(x, y)
    canvas.draw(dx, y)
    canvas.draw(x, dy)
    canvas.draw(dx, dy)


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
