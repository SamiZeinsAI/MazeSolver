from tkinter import Tk, BOTH, Canvas
class Window():
    def __init__(self,width: int,height: int):
        self.__root = Tk()
        self.__root.title = 'Maze Solver'
        self.canvas = Canvas(self.__root, bg="white",height=height,width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.__isRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    def wait_for_close(self):
        self.__isRunning = True
        while self.__isRunning:
            self.redraw()
    def close(self):
        self.__isRunning = False
    def draw_line(self,line,fill_color='black'):
        line.draw(self.canvas,fill_color)


class Point():
    def __init__(self,x:int,y:int):
        self.x = x
        self.y = y
class Line():
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self,canvas:Canvas,fill_color:str):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
        canvas.pack()