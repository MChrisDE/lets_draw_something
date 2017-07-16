import os
from tkinter import *
from PIL import ImageGrab

color = 'black'
canvas_width = 500
canvas_height = 500


class DrawCanvas(Canvas):
	def __init__(self, tkmaster, **kw):
		super().__init__(tkmaster, **kw)
		self.grid(row=0, column=0, padx=10, pady=10)
		self.bind('<B1-Motion>', self.line_paint)
		self.bind('<ButtonRelease-1>', lambda event: self.init(False))
		self.config(highlightbackground='black')
		self.lines = []
		self.init()

	def init(self, clear=True):  # create the lines, 'clear' resets the current lines
		global color
		if clear:
			self.lines = []
		for x in range(4):  # save the canvas 'id' in [0]
			self.lines.append([self.create_line(0, 0, 0, 0, width=2, fill=color)])

	def paint(self, event):
		global canvas_height, canvas_width
		x, y = event.x, event.y
		dx = canvas_width - x
		dy = canvas_height - y
		self.create_rectangle(x, y, (x + 1), (y + 1), outline=color)
		self.create_rectangle(dx, y, (dx + 1), (y + 1), outline=color)
		self.create_rectangle(x, dy, (x + 1), (dy + 1), outline=color)
		self.create_rectangle(dx, dy, (dx + 1), (dy + 1), outline=color)

	def line_paint(self, event):
		global canvas_height, canvas_width
		x, y = event.x, event.y
		dx = canvas_width - x
		dy = canvas_height - y
		self.lines[-4] += x, y, (x + 1), (y + 1)  # access the list
		self.lines[-3] += dx, y, (dx + 1), (y + 1)  # elements from behind
		self.lines[-2] += x, dy, (x + 1), (dy + 1)  # to make changing the
		self.lines[-1] += dx, dy, (dx + 1), (dy + 1)  # line color possible
		for i in range(-4, 0):  # change the path of the last 4 lines
			self.coords(self.lines[i][0], *self.lines[i][1:])

	def clear(self):  # reset the canvas
		self.delete(ALL)
		self.init()

	def save(self, **kwargs):
		kwargs['path'] = kwargs.get('path', os.path.join(os.environ['USERPROFILE'], r'Desktop\\drawing.jpg'))
		x = self.master.winfo_rootx() + self.winfo_x()
		y = self.master.winfo_rooty() + self.winfo_y()
		x1 = x + self.winfo_width()
		y1 = y + self.winfo_height()
		ImageGrab.grab().crop((x, y, x1, y1)).save(kwargs['path'])


class ColorFrame:
	colors = ['black', 'white', 'red', 'green', 'blue', 'yellow']

	def __init__(self, tkmaster):
		self.frame = Frame(tkmaster)
		self.frame.grid(row=0, column=1)
		buttons = []
		for i in range(len(self.colors)):
			buttons.append(Color(self.frame, self.colors[i], i))


class Color:
	def __init__(self, tkmaster, bcolor, row):
		self.color = bcolor
		self.button = Button(tkmaster, text=8 * ' ', command=self.change_color)
		self.button.config(background=bcolor)
		self.button.grid(row=row, column=0)

	def change_color(self):
		global color, canvas
		color = self.color
		canvas.init(False)  # we don't want to reset the lines, passing 'False' will only create new lines


master = Tk()
master.title('lets draw something')

canvas = DrawCanvas(master, width=canvas_width, height=canvas_height)

colorframe = ColorFrame(master)

message = Label(master, text='press and drag the mouse to draw')
message.grid(row=1, column=0)

delete = Button(master, text='delete', command=canvas.clear)
delete.grid(row=1, column=1)

save = Button(master, text='save', command=canvas.save)
save.grid(row=1, column=2)
mainloop()
