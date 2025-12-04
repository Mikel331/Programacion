class Sudoku:
    
    tablero = [
    [" ", " ", " " , " " ," ", " " , " " , " " , " "],
    [" ", " ", " " , " " ," ", " " , " " , " " , " "],
    [" ", " ", " " , " " ," ", " " , " " , " " , " "],
    [" ", " ", " " , " " ," ", " " , " " , " " , " "],
    [" ", " ", " " , " " ," ", " " , " " , " " , " "],
    [" ", " ", " " , " " ," ", " " , " " , " " , " "],
    [" ", " ", " " , " " ," ", " " , " " , " " , " "],
    [" ", " ", " " , " " ," ", " " , " " , " " , " "],
    [" ", " ", " " , " " ," ", " " , " " , " " , " "],
]
    
    
    
    def mostrarTablero(self):
     for row in self.tablero:
        print(row) 
        
    def Elegir(self):
        
        numero = 0
        
        while(True):
            
            if(numero> 0 and numero<10):
                break;
            numero = int(input("Introduce el numero:"))
            
        fila = 0
        
        while(True):
            
            if(fila> 0 and fila<10):
                break;
            fila = int(input("Introduce la fila:"))
            
        columna = 0
        
        while(True):
            
            if(columna> 0 and columna<10):
                break;
            columna = int(input("Introduce la columna:"))
        
        if(self.tablero[fila][columna]== " "):
           self.tablero[fila][columna] = str(numero)
           self.mostrarTablero()
           
    def ObtenerTablero(self):
        resultado = ""
        for fila in self.tablero:
            resultado += " " . join(str(numero) for numero in fila) + "\n"
        return resultado
        
           
           
    
                
                
           
    
    
        
        
        
    
        
    
   