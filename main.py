from flask import Flask, jsonify, request
from flask_cors import CORS

from recomendador.gemma.recomendador import formular
from recomendador.buscador import sacar_datos_pelis

app = Flask(__name__)
CORS(app)

@app.route('/recomendador', methods=['GET'])
def recomendar_peli():
    prompt = request.args.get('prompt')
    numero = request.args.get('numero')
    
    respuesta = formular(prompt, numero)

    if respuesta == "":
        return jsonify({})
    else:
        pelis = []
        datos = []       
        resp_clean = respuesta.replace('"', '').replace("\n","").strip()

        pelis = [item.strip() for item in resp_clean.split(',')]
        datos = sacar_datos_pelis(pelis)
        
        return jsonify(datos)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)