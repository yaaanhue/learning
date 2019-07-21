from flask import Flask, request
from flask_restful import  Resource, Api
from habilidades import Habilidades
import json


app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id':'0',
        'nome':'Yan',
        'habilidades': ['Python', 'Flask']
     },
    {
        'id':'1',
        'nome':'Luiz',
        'habilidades':['Python', 'Django']
    }
]
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            responda  = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} nao existe'.format(id)
            responda = {'status': 'error', 'mensagem': mensagem}
        except Exception:
            mensagem = 'erro desconhecido'
            responda = {'status': 'erro', 'mensagem': mensagem}
        return responda

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return ({'status':'sucesso', 'mensagem':'registro excluido'})

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return (desenvolvedores[posicao])

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades,'/habilidades/')
if __name__ == '__main__':
    app.run(debug=True)
