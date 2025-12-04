import json
class TresEnRaya:
    turno = "x"
    tablero = [["", " " , " "],
               ["", " " , " "],
               ["", " " , " "],]
    
    
    def mostrarTablero(self):
        for row in self.tablero:
            print(row)
            
    def elegir(self):
       
        while (True) :
            if(self.turno=="x"):
                print("Turno jugador 1")
                fila = int(input("Selecciona la fila: "))
                columna = int(input("Selecciona la columna: "))
                
            if(self.turno=="O"):
                ("Turno jugador 2")
                fila = int(input("Selecciona la fila: "))
                columna = int(input("Selecciona la columna: "))
                
            
            if(self.tablero[fila][columna] == " "):
                self.tablero[fila][columna] = self.turno
                self.mostrarTablero()
                self.Json_Guardar()
                
            if self.turno=="x":
                self.turno = "O"
            else :
               self.turno= "x"
                
    def Json_Guardar(self,archivo="TresEnRaya\TresEnraya.json"):
        
        data = {
            "turno" : self.turno,
            "tablero": self.tablero
        }
        
        with open(archivo, "w+" , encoding="utf-8") as juego:
            json.dump(data, juego, indent=4)
                
                
        
        
    