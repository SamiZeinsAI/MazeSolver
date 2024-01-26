from cell import Cell
import time
import random
class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
        ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = [[Cell(win) for _ in range(num_cols)]for _ in range(num_rows)]
        
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        self._create_cells()


    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self,i,j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.__num_rows - 1 and j == self.__num_cols - 1:
            return True
        dirs = [
            (i+1,j,self._cells[i][j].has_bottom_wall),
            (i-1,j,self._cells[i][j].has_top_wall),
            (i,j+1,self._cells[i][j].has_right_wall),
            (i,j-1,self._cells[i][j].has_left_wall),
            ]
        for r , c, has_wall in dirs:
            if (
                r in range(self.__num_rows) and 
                c in range(self.__num_cols) and 
                not has_wall and
                not self._cells[r][c].visited):

                self._cells[i][j].draw_move(self._cells[r][c])
                if self._solve_r(r,c):
                    return True  
                else:
                    self._cells[i][j].draw_move(self._cells[r][c],True)

        return False


    
    def _reset_cells_visited(self):
        for i in range(self.__num_rows):
            for j in range(self.__num_cols):
                self._cells[i][j].visited = False
    
    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        possible_directions = []
        
        if i > 0 and self._cells[i-1][j].visited == False:
            possible_directions.append((i-1,j))
        if i < self.__num_rows - 1 and self._cells[i+1][j].visited == False:
            possible_directions.append((i+1,j))
        if j > 0 and self._cells[i][j-1].visited == False:
            possible_directions.append((i,j-1))
        if j < self.__num_cols - 1 and self._cells[i][j+1].visited == False:
            possible_directions.append((i,j+1))
        num_dirs = len(possible_directions)
        if num_dirs == 0:
            return
        random.shuffle(possible_directions)
        for direction in possible_directions:
            if self._cells[direction[0]][direction[1]].visited:
                continue
            if direction == (i-1,j):
                self._cells[i][j].has_top_wall = False
                self._cells[i-1][j].has_bottom_wall = False
            if direction == (i+1,j):
                self._cells[i][j].has_bottom_wall = False
                self._cells[i+1][j].has_top_wall = False
            if direction == (i,j+1):
                self._cells[i][j].has_right_wall = False
                self._cells[i][j+1].has_left_wall = False
            if direction == (i,j-1):
                self._cells[i][j].has_left_wall = False
                self._cells[i][j-1].has_right_wall = False
            self._break_walls_r(*direction)

        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
    
    def _create_cells(self):
        for i in range(self.__num_rows):
            for j in range(self.__num_cols):
                self._draw_cell(i,j)
    def _draw_cell(self,i,j):
        if self.__win is None:
            return
        top = self.__y1 + (i*self.__cell_size_y)
        left = self.__x1 + (j*self.__cell_size_x)
        self._cells[i][j].draw(left,top,left+self.__cell_size_x,top+self.__cell_size_y)
        self._animate()

    def _animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(.05)
        