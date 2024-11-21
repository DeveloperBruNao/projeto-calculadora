from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    if request.method == 'POST':
        expressao = request.form['expressao']
        try:
            resultado = eval(expressao)
        except Exception as e:
            resultado = "Erro" + str(e)
        return render_template('index.html', resultado=resultado, expressao=expressao)

if __name__ == '__main__':
    app.run(debug=True)
