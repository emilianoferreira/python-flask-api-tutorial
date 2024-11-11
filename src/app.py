from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


todos = [{ "label": "My first task", "done": False }]

           #endpoint. metodo
@app.route('/todos', methods=['GET'])
#funcion que se lanza cuando se llama al endpoint /myroute
def hello_world():
    return jsonify(todos)



@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position)
    return jsonify(todos)



#evalua si el nombre del archivo es main
if __name__ == '__main__':
 #si es true, levanta un servidor para todas las ip de la red, en el puerto 3245 en modo de depuracion(muestra errores)
    app.run(host='0.0.0.0', port=3245, debug=True)


