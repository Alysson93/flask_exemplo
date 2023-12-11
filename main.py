from flask import Flask, render_template, request
from dtos.DadosDTO import DadosDTO

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/dados', methods=['POST'])
def tratar_dados():
    return f'Dados tratados: {request.form['email']}' 

app.run(
    debug=True,
    port=8000
)