from tkinter import *

canvas_width = 500
canvas_height = 500


class DrawCanvas(Canvas):
	def __init__(self, tkmaster, **kw):
		super().__init__(tkmaster, **kw)
		self.grid(row=0, column=0, padx=10, pady=10)
		self.bind("<B1-Motion>", self.paint)
		self.config(highlightbackground="black")

	def paint(self, event):
		global canvas_height, canvas_width
		x, y = event.x, event.y
		dx = canvas_width - x
		dy = canvas_height - y
		self.create_rectangle(x, y, (x + 1), (y + 1), outline=color)
		self.create_rectangle(dx, y, (dx + 1), (y + 1), outline=color)
		self.create_rectangle(x, dy, (x + 1), (dy + 1), outline=color)
		self.create_rectangle(dx, dy, (dx + 1), (dy + 1), outline=color)

	def clear(self):
		self.delete("all")


class ColorFrame:
	colors = ["black", "white", "red", "green", "blue", "yellow"]

	def __init__(self, tkmaster):
		self.frame = Frame(tkmaster)
		self.frame.grid(row=0, column=1)
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


color = "black"

master = Tk()
master.title("lets draw something")

canvas = DrawCanvas(master, width=canvas_width, height=canvas_height)

colorframe = ColorFrame(master)

message = Label(master, text="press and drag the mouse to draw")
message.grid(row=1, column=0)

delete = Button(master, text="Delete", command=canvas.clear)
delete.grid(row=1, column=1)
mainloop()
