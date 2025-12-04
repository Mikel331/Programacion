from SudokuEjercicio2 import Sudoku

escribirArchivo = "Sudoku\Sudoku.txt";
sudoku = Sudoku()

while (True):
    sudoku.mostrarTablero()
    sudoku.Elegir()

    with open(escribirArchivo, "w+" , encoding="utf-8") as escribir:
        escribir.write(sudoku.ObtenerTablero())
        

    
