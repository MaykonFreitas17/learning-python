# importando o modulo http
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Criando um Request Handler
class SimpleHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    # criando a rota com metodo GET - http://localhost:8000/
    if self.path == '/':
      self.send_response(200) # definindo o status code da response
      self.end_headers() # declarando que não existe headers
      self.wfile.write("Hello World".encode()) # Retornando para o usuário
    
    # criando a rota com metodo GET - http://localhost:8000/estudantes
    if self.path == '/estudantes':
      self.send_response(200) # definindo o status code da response
      self.send_header("Context-Type", "application/json; charset=utf-8")
      self.end_headers() # declarando que não existe headers
      data = [
        {
          "id": 1,
          "name": "Maykon Freitas",
          "email": "exemple123@gmail.com"
        },
        {
          "id": 2,
          "name": "Maykon Freitas",
          "email": "exemple123@gmail.com"
        },
        {
          "id": 3,
          "name": "Maykon Freitas",
          "email": "exemple123@gmail.com"
        },
      ]

      self.wfile.write(json.dumps(data).encode())

server = HTTPServer(('localhost', 8000), SimpleHandler) # Definindo o host e a porta onde vai rodar o servidor da aplicação -> http://localhost:8000/
# rodando o servidor
server.serve_forever() # rodando em loop