# importando o Flask - instalando o framework - pip install Flask
from flask import Flask, jsonify, make_response, abort, request
import json

# Pegando os dados do arquivo db.json e armazenando na variavel data
with open("db.json", encoding="utf-8") as databases:
  data = json.load(databases)

# criando um objeto flask
app = Flask(__name__) # passando o nome da aplicação

# Criando rotas
@app.route("/") # Mapeando/definindo a rota para a função index
def index():
  return "<h1>Hello World, Flask!!</h1>"

# Criando um middleware de error padrão
@app.errorhandler(404) # Esse middleware será chamado toda vez que um abort com o statusCode for executado
def not_found(error):
  # erro = { "message": str(error) }
  # return (jsonify(erro), 404)
  return (jsonify(message=str(error)), 404)

# Middleware de error para valores não especificados
@app.errorhandler(400)
def is_required(error):
  return (jsonify(message=str(error)), 400)

# Rota para a listagem de users
@app.route("/api/v1/users/")
def get_all():
  return jsonify(data) # retornando a lista de usuarios

# Rota para a listar um user por id
@app.route("/api/v1/users/<int:id>/") # Informando que a rota vai receber um parametro pela url
def get_by_id(id):
  for user in data:
    if user['id'] == id:
      return jsonify(user)

  abort(404, "User not found") # Uma forma de retornar erros
  #return make_response(jsonify({ "message": "User Not Found" }), 404) # Difinindo a resposta error, caso nenhum usúario seja encontrado, com o StatusCode 404 - Not Found

# Rota para criar um novo user
@app.route("/api/v1/users/", methods=["POST"])
def create():
  body = json.loads(request.data) # recebendo os dados do body da requisição e convertendo para um dict (objeto)
  # body = request.data # Apenas recebendo e armazendo os valores do body da requisição
  name = body.get("name")
  email = body.get("email")
  password = body.get("password")

  # Validando os valores do body
  if not name:
    abort(400, "'name' is required")
  
  if not email:
    abort(400, "'email' is required")
  
  if not password:
    abort(400, "'password' is required")

  # criando o objeto modelo
  user = {
    "id": len(data) + 1,
    "name": name,
    "email": email,
    "password": password
  }

  data.append(user) # Adicionando novo user a lista data

  # Alterando o arquivo db.json - inserindo mais valores
  with open("db.json", "w") as databases:
    databases.write(json.dumps(data, indent=2)) # escrevendo no arquivo db.json
  
  return jsonify(user) # retornando o novo usuarios

# Rota para a deletar um user por id
@app.route("/api/v1/users/<int:id>/", methods=["DELETE"]) # Informando que a rota vai receber um parametro pela url
def delete(id):
  for user in data:
    if user['id'] == id:
      data.remove(user) # removendo o user a lista data
      
      # Alterando o arquivo db.json - deletando um valor valores existente
      with open("db.json", "w") as databases:
        databases.write(json.dumps(data, indent=2)) # escrevendo no arquivo db.json
      
      return jsonify(user)

  abort(404, "User not found") # Uma forma de retornar erros

# Rota para atualizar um user por id
@app.route("/api/v1/users/<int:id>/", methods=["PUT"]) # Informando que a rota vai receber um parametro pela url
def update(id):
  body = json.loads(request.data) # recebendo os dados do body da requisição e convertendo para um dict (objeto)
  
  name = body.get("name")
  email = body.get("email")
  password = body.get("password")

  # Validando os valores do body
  if not name:
    abort(400, "'name' is required")
  
  if not email:
    abort(400, "'email' is required")
  
  if not password:
    abort(400, "'password' is required")

  for user in data:
    if user['id'] == id:
      user["name"] = name
      user["email"] = email
      user["password"] = password
 
      # Alterando o arquivo db.json - modificando um valor existente
      with open("db.json", "w") as databases:
        databases.write(json.dumps(data, indent=2)) # escrevendo no arquivo db.json
      
      return jsonify(user)

  abort(404, "User not found") # Uma forma de retornar erros

# Rota para atualizar (patch) um user por id
@app.route("/api/v1/users/<int:id>/", methods=["PATCH"]) # Informando que a rota vai receber um parametro pela url
def patch(id):
  body = json.loads(request.data) # recebendo os dados do body da requisição e convertendo para um dict (objeto)
  
  if "name" in body.keys():
    name = body.get("name")
    if not name:
      abort(400, "'name' is required")
    
    for user in data:
      if user['id'] == id:
        user["name"] = name
        with open("db.json", "w") as databases:
          databases.write(json.dumps(data, indent=2))
        return jsonify(user)
  
  if "email" in body.keys():
    email = body.get("email")
    if not email:
      abort(400, "'email' is required")

    for user in data:
      if user['id'] == id:
        user["email"] = email
        with open("db.json", "w") as databases:
          databases.write(json.dumps(data, indent=2))
        return jsonify(user)

  if "password" in body.keys():
    password = body.get("password")
    if not password:
      abort(400, "'password' is required")  
 
    for user in data:
      if user['id'] == id:
        user["password"] = password
        with open("db.json", "w") as databases:
          databases.write(json.dumps(data, indent=2))
        return jsonify(user)

  abort(404, "User not found") # Uma forma de retornar erros

# Para rodar o servidor Flask em ambiente de desenvolvimento use:
# FLASK_APP=app.js FLASK_ENV=development flask run
# FLASK_APP=app.js FLASK_DEBUG=true flask run