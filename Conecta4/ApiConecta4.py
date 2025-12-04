from flask import Flask, request, jsonify

app = Flask(__name__)


juego = {"turno": "x", "tablero": [[" "]*6 for _ in range(6)]}

@app.route("/guardar", methods=["POST"])
def guardar_juego():
    data = request.get_json()  
    print("JSON recibido:", data)
    if not data:
        return jsonify({"error": "No se envió JSON"}), 400

  
    juego["turno"] = data.get("turno", juego["turno"])
    juego["tablero"] = data.get("tablero", juego["tablero"])

    return jsonify({"mensaje": "Juego recibido correctamente"}), 200

if __name__ == "__main__":
    app.run(debug=True , port=5000,host="0.0.0.0")
