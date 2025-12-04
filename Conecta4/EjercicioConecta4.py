import json
class Conecta4:
    turno = "x"
    tablero = [[" " , " " , " " , " " , " ", " "],
            [" " , " " , " " , " " , " ", " "],
            [" " , " " , " " , " " , " ", " "],
            [" " , " " , " " , " " , " ", " "],
            [" " , " " , " " , " " , " ", " "],
            [" " , " " , " " , " " , " ", " "],
            ]
     

          
    def mostrarTablero(self):
        for row in self.tablero:
            print(row)

            
    def Elegir_opciones(self):
        
        while(True):
           
           if(self.turno=="x"):
               print("Turno jugador 1")
               fila = int(input("Selecciona la fila: "))
               columna = int(input("Selecciona la columna"))
           
           if (self.turno=="O"):
               print("Turno jugador 2")
               fila = int(input("Selecciona la fila: "))
               columna = int(input("Selecciona la columna"))
               
           
           if(self.tablero[fila][columna] == " "):
               self.tablero[fila][columna] = self.turno
               self.mostrarTablero()
               self.guardarJSON()
               self.turno = "O" if self.turno == "x" else "x"
         

              
    def guardarJSON(self,archivo="Conecta4\Conecta4.json"):
        juego = {
            "turno": self.turno,
            "tablero": self.tablero
        }
             
        with open(archivo, "w+" , encoding="utf-8") as Json:
            json.dump(juego,Json, indent=4) 
            
               
            
        
        
        
        
    