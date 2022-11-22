# para importar modulos, se usa a sintaxe = import nome_module
# para importar modulos, se usa a sintaxe = from nome_arquivo import nome_module
from heranca import Estudante

# Podemos importar Modulos já existente dentro do Python
import json

# Criando uma função que recebe um objeto (Dict) e retorna o objeto no formatado JSON
def show_json(object):
  return json.dumps(object)

e1 = Estudante('Bruno Sousa', 18, "000.000.000-00", "Ciência da Computação")
e1.show_informations()

# Imprimindo o retorno do show_json
print(show_json(e1.get_study()))