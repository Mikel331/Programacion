import requests
from EjercicioConecta4 import Conecta4

def enviarAPI(self):
    url = "http://192.168.25.133:8000/guardar"
    data= {
       "nombre": "Mikel",
       "apellido": "Suarez",
       "api_url": "http://192.168.25.225:5000/guardar",
       "sudoku": a.tablero
}
    a = Conecta4() 
    response = requests.post(url, json=data) 
    print(response.status_code, response.text)

