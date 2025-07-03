from flask import Flask, jsonify, request

app = Flask(__name__)

pizzas = [
    {
        'id': 1, 
        'sabor': 'Frango com Catupiry',
        'preço': 40,
        'ingredientes': 'Frango Desfiado, Catupiry e Queijo'
    },
    {
        'id': 2, 
        'sabor': 'Calabresa',
        'preço': 35,
        'ingredientes': 'Calabresa em rodelas, Presunto e Queijo'
        
    },
    {
        'id': 3, 
        'sabor': 'Pepperoni',
        'preço': 40,
        'ingredientes': 'Pepperoni, Molho de Tomate e Queijo'
    },
    {
        'id': 4, 
        'sabor': 'Marguerita',
        'preço': 45,
        'ingredientes': 'Presunto, Queijo, Molho de Tomate e Azeitonas '
    },
    
]


#Consultar Pizzas
@app.route('/pizzas',methods=['GET'])
def obter_pizzas():
    return jsonify(pizzas)


#Consultar (Id)
@app.route('/pizzas/<int:id>', methods=['GET'])
def obter_pizza_por_id(id):
    for pizza in pizzas:    
        if pizza.get('id') == id:
            return jsonify(pizza)
        

       
#sugestão
@app.route('/pizzas', methods = ['POST'])
def incluir_nova_pizza():
    nova_pizza = request.get_json()
    pizzas.append(nova_pizza)

    return jsonify(
        mensagem = 'Sugestão de Cliente Enviada!',
        pizzas = nova_pizza) 

#Editar Ingredientes
@app.route('/pizzas/<int:id>', methods = ['PUT'])
def editar_ingredientes_por_id(id):
    pizza_alterada = request.get_json()
    for indice,pizza in enumerate(pizzas):
        if pizza.get('id') == id:
            pizzas [indice].update(pizza_alterada)
            return jsonify(pizzas[indice])

#Excluir
@app.route('/pizzas/<int:id>', methods = ['DELETE'])
def excluir_pizza(id):
    for indice,pizza in enumerate(pizzas):
        if pizza.get('id') == id:
            del pizzas [indice]

            return jsonify(pizzas)

app.run(port=5000,host='localhost',debug=True)