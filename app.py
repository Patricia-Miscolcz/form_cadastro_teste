# import pyodbc
import mysql.connector
from flask import Flask, render_template, request



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="gi2703**",
    database="projeto_matematica",
)

# cria um cursor para executar consultas SQL
my_cursor = mydb.cursor()
print("Conexão Bem Sucedida")


# define uma função para inserir os dados no banco de dados
def inserir_dados(form_data):
    sql = "INSERT INTO form_prof (cep, endereco, numero, complemento, bairro, cidade, nome_completo, telefone, email, genero, data_nascimento, area_atuacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (form_data['cep'], form_data['endereco'], form_data['numero'], form_data['complemento'], form_data['bairro'], form_data['cidade'], form_data['nome'], form_data['telefone'], form_data['email'], form_data['genero'], form_data['data_nascimento'], form_data['area_atuacao'])
    
    print("Valores a serem inseridos no banco de dados:", val)  # Adicione esta linha
    my_cursor.execute(sql, val)
    mydb.commit()

# código Flask para lidar com o envio do formulário
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_data = request.form
        inserir_dados(form_data)
        return 'Dados inseridos com sucesso!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)