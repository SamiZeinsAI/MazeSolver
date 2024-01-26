from graphics import Line, Point
class Cell():
    def __init__(self,win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None       
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__win = win
        self.visited = False

    



    def draw(self,x1,y1,x2,y2):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        sides = [(x1,y1,x1,y2),(x1,y1,x2,y1),(x2,y1,x2,y2),(x1,y2,x2,y2)]
        hasSides = [self.has_left_wall,  self.has_top_wall, self.has_right_wall,self.has_bottom_wall]
        for i in range(len(sides)):
            start = (sides[i][0],sides[i][1])
            end = (sides[i][2],sides[i][3])
            line = Line(Point(*start),Point(*end))
            if hasSides[i]:
                self.__win.draw_line(line)
            else:
                self.__win.draw_line(line,"white")

    def draw_move(self, to_cell, undo=False):
        if self.__win is None:
            return
        x1 = (self.__x1+self.__x2)//2
        y1 = (self.__y1+self.__y2)//2
        x2 = (to_cell.__x1+to_cell.__x2)//2
        y2 = (to_cell.__y1+to_cell.__y2)//2
        line = Line(Point(x1,y1),Point(x2,y2))
        self.__win.draw_line(line,'grey' if undo else 'red')
