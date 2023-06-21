from sudoku import Sudoku
import time


sudoku = Sudoku()

# Cargar el sudoku del archivo de texto
file = open("pruebas\prueba1.txt", "r")
a_sudoku = []
for index, line in enumerate(file.readlines()):
    a_sudoku.append([int(s) for s in line.split() if s.isdigit()])
file.close()
print("Sudoku cargado:")
sudoku.print_sudoku(a_sudoku)

print("\n")

# Resolver el sudoku
import time
inicio = time.time()
a_solved_sudoku = sudoku.solve_sudoku(a_sudoku)
fin = time.time()

if a_solved_sudoku != None:
    print("Sudoku resuelto:")
    sudoku.print_sudoku(a_sudoku)
    
    print("\n# de fallos: ", sudoku.failures)
    print("\n# de casillas llenadas para la solucion: ", sudoku.filled_cells)
    print(fin-inicio)
else:
    print("No se encontró una solución.")
    print(fin-inicio)