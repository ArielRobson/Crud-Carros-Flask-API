from flask import Flask, make_response, jsonify, request
from conection import conn

app = Flask(__name__)  # instancia o flask na variavel App
app.json.sort_keys = False


@app.route('/carros', methods=['GET'])
def get_carros(): #usado o make e jsonify para mostrar o resultado conforme o curo, porem aqui retornou sem necessidade das duas funções

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Carro')
    meus_carros = cursor.fetchall()

    car = list()
    for carro in meus_carros:
        car.append(
            {'id': carro[0],
             'marca': carro[1],
             'modelo': carro[2],
             'ano': carro[3]
             }
        )
    return make_response(
        jsonify(
            mensagem='Lista de Carros,',
            dados=car)
    )


@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json

    cursor = conn.cursor()
    conSql = f"INSERT INTO CARRO (marca, modelo, ano) values ('{carro['marca']}', '{carro['modelo']}', {carro['Ano']})"
    cursor.execute(conSql)
    conn.commit()
    return make_response(
        jsonify(
            mensagem='Carro cadastro com sucesso.',
            carro=carro)
    )


@app.route('/carros/<int:id>', methods=['PUT'])
def att_carro(id):
    carro_atualizado = request.json
    cursor = conn.cursor()
    conSql = f"select count(*) from carro where id = {id}"
    cursor.execute(conSql)
    res = cursor.fetchall()
    if res[0][0] > 0:
        if 'marca' in carro_atualizado:
            consql = f"update carro set marca = '{carro_atualizado['marca']}' where id = {id}"
            cursor.execute(consql)
            conn.commit()
        if 'modelo' in carro_atualizado:
            consql = f"update carro set modelo = '{carro_atualizado['modelo']}' where id = {id}"
            cursor.execute(consql)
            conn.commit()
        if 'ano' in carro_atualizado:
            consql = f"update carro set ano = {carro_atualizado['ano']} where id = {id}"
            cursor.execute(consql)
            conn.commit()
        return 'Dados atualizados com sucesso!'
    else:
        return 'ID não encontrado.'


@app.route('/carros/<int:id>', methods=['DELETE'])
def del_carro(id):
    cursor = conn.cursor()
    conSql = f"select count(*) from carro where id = {id}"
    cursor.execute(conSql)
    res = cursor.fetchall()
    if res[0][0] > 0:
        condel = f"DELETE FROM CARRO WHERE ID = {id}"
        cursor.execute(condel)
        conn.commit()
        return 'Carro deletado com sucesso.'
    else:
        return 'ID não encontrado, verifica o ID e tente novamente.'


if __name__ == '__main__':
    app.run(debug=True)  # start na aplicação flask