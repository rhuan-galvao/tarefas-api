from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tarefas = [
    {
        'id': 0,
        'responsavel': 'Rhuan',
        'tarefa': 'Desenvolver o método GET',
        'status': 'concluido'
    },

    {
        'id': 1,
        'responsavel': 'Nana',
        'tarefa': 'Desenvolver o método POST',
        'status': 'pendente'
    }
]

# Mostra cada tarefa individualmente e exlui tarefas
@app.route('/tarefas/<int:id>/', methods=['GET', 'DELETE', 'PUT'])
def tarefa(id):
    if request.method == 'GET':
        try:
            tarefa = tarefas[id]
            return jsonify(tarefa)
        except IndexError:
            mensagem_erro = f'A tarefa ID {id} não existe'
            tarefa = {'status': 'erro', 'mensagem': mensagem_erro}
        except Exception:
            mensagem_erro = 'Erro desconhecido, procure o administrador da API'
            tarefa = {'status': 'erro', 'mensagem': mensagem_erro}
    elif request.method == 'DELETE':
        tarefas.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'tarefa excluida!'})

# Mostra todas as tarefas, também adiciona novas e edita o status da tarefa
@app.route('/tarefas/', methods=['GET', 'POST', 'PUT'])
def todas_tarefas():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        return jsonify(tarefas[posicao])
    elif request.method == 'GET':
        return jsonify(tarefas)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas[id]['status'] = 'concluido'
        return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)
