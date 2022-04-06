from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/calculo/", methods=['POST'])
def calculadora():

#Requisições
    valor_a = request.form['valor_a']
    valor_b = request.form['valor_b']
    operacao = request.form['operacao']
    resultado = 0

    valor_a = float(valor_a)
    valor_b = float(valor_b)
    operacao = str(operacao)

#Operações
    if (operacao == "/" and valor_b == 0):
        resultado = 'Não pode dividir por 0.'
    elif (operacao == "*"):
        resultado = valor_a * valor_b
    elif (operacao == "/"):
        resultado = valor_a / valor_b
    elif (operacao == "+"):
        resultado = valor_a + valor_b
    elif (operacao == "-"):
        resultado = valor_a - valor_b

    return str(resultado)

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)