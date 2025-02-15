import tkinter as tk
import time

board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]

class SudokuApp(tk.Tk):
    def __init__(self, board):
        super().__init__()
        self.title("Sudoku Solver")
        self.geometry("800x600")    
        self.canvas_size = 450
        self.cell_size = self.canvas_size // 9
        self.board = board
        
        # Create canvas
        self.canvas = tk.Canvas(width=self.canvas_size, height=self.canvas_size)
        self.canvas.pack(padx=10, pady=10)
        
        # Store cell text objects for updating
        self.cell_texts = [[None for _ in range(9)] for _ in range(9)]
        
        # Draw initial board
        self._draw_grid()
        self.update_board(board)
        self.bind("<Escape>", self.solve)

    def _draw_grid(self):
        """Draw the grid lines of the Sudoku board"""
        for i in range(10):
            # Determine line width (thicker for 3x3 box borders)
            line_width = 3 if i % 3 == 0 else 1
            
            # Draw vertical lines
            x = i * self.cell_size
            self.canvas.create_line(x, 0, x, self.canvas_size, width=line_width)
            
            # Draw horizontal lines
            y = i * self.cell_size
            self.canvas.create_line(0, y, self.canvas_size, y, width=line_width)

    def update_board(self, board):
        """
        Update the board with new values
        Args:
            board: 9x9 list of lists containing the new Sudoku numbers
        """
        for i in range(9):
            for j in range(9):
                x = j * self.cell_size + self.cell_size // 2
                y = i * self.cell_size + self.cell_size // 2
                
                # Delete existing number if present
                if self.cell_texts[i][j] is not None:
                    self.canvas.delete(self.cell_texts[i][j])
                    self.cell_texts[i][j] = None
                
                # Add new number if not zero
                if board[i][j] != 0:
                    self.cell_texts[i][j] = self.canvas.create_text(
                        x, y,
                        text=str(board[i][j]),
                        font=('Arial', 16, 'bold')
                    )     

    def find_empty(self):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (j, i)  # row, col
            
    def check(self, x, y, v):
        for i in range(len(board[0])):
            if board[y][i] == v and x != i:
                return False

        for i in range(len(board)):
            if board[i][x] == v and y != i:
                return False

        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[y0 + i][x0 + j] == v and (y0 + i, x0 + j) != (y, x):
                    return False

        return True

    def solve(self, event=None):
        try:
            print('solving')
            find = self.find_empty()
            if not find:
                return True
            else:
                x, y = find
                
            for i in range(1, 10):
                if self.check(x, y, i):
                    self.board[y][x] = i
                    self.update_board(self.board)
                    self.update()  # Use update() instead of update_idletasks()
                    time.sleep(0.05)  # Reduced sleep time further
                    
                    if self.solve():
                        return True
                    
                    self.board[y][x] = 0
                    self.update_board(self.board)
                    self.update()  # Use update() here too
                    time.sleep(0.05)
            
            return False
        except tk.TclError:  # Handle case where window is closed during solving
            return False             

if __name__ == '__main__':
    app = SudokuApp(board)
    app.mainloop()