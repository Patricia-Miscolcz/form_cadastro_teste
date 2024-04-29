from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
import logging

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['projeto_matematica']
collection = db['form_prof']

# Configuração do logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    logger.info('Rota index foi acessada')
    
    if request.method == 'POST':
        form_data = request.form
        logger.debug(f'Dados do formulário recebidos: {form_data}')
        
        data = {
            'cep': form_data.get('cep'),
            'endereco': form_data.get('endereco'),
            'numero': form_data.get('numero'),
            'complemento': form_data.get('complemento'),
            'bairro': form_data.get('bairro'),
            'cidade': form_data.get('cidade'),
            'nome': form_data.get('nome'),
            'telefone': form_data.get('telefone'),
            'email': form_data.get('email'),
            'genero': form_data.get('genero'),
            'data_nascimento': form_data.get('data_nascimento'),
            'area_atuacao': form_data.get('area_atuacao')
        }
        logger.debug(f'Dados a serem inseridos no MongoDB: {data}')
        
        collection.insert_one(data)
        logger.info('Dados inseridos no MongoDB com sucesso')
        
        return redirect(url_for('index'))
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)