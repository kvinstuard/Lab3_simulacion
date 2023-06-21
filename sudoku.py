import random

class Sudoku:

    def __init__(self):
        self.failures = 0
        self.filled_cells = 0

    def is_valid(self, board, row, col, num):
        # Verificar si el número es válido en la fila
        for i in range(9):
            if board[row][i] == num:
                self.failures += 1
                return False
        
        # Verificar si el número es válido en la columna
        for i in range(9):
            if board[i][col] == num:
                self.failures += 1
                return False
        
        # Verificar si el número es válido en el subcuadro 3x3
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    self.failures += 1
                    return False
        
        return True

    def solve_sudoku(self, board):
        if self.is_complete(board):
            return board

        row, col = self.find_empty_cell(board)
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(numbers)
        
        for num in numbers:
            if self.is_valid(board, row, col, num):
                board[row][col] = num
                self.filled_cells += 1 
                if self.solve_sudoku(board):
                    return board
                board[row][col] = 0

        return None

    def is_complete(self, board):
        for row in board:
            if 0 in row:
                return False
        return True

    def find_empty_cell(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None


    def generate_sudoku(self):
        board = [[0] * 9 for _ in range(9)]
        self.solve_sudoku(board)
        
        # Remover números aleatoriamente para generar un Sudoku parcialmente resuelto
        empty_cells = random.randint(30, 50)
        for _ in range(empty_cells):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            board[row][col] = 0
        
        return board

    def print_sudoku(self, board):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - -")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                if j == 8:
                    print(board[i][j])
                else:
                    print(board[i][j], end=" ")