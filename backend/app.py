from flask import Flask
from flask_restful import Api
from config.config_db import config_db
from routes import initialize_routes

app = Flask(__name__)
api = Api(app)

# Configurar o banco de dados
config_db(app)

# Inicializar as rotas
initialize_routes(api)

# Adicionar uma rota padrão para o caminho raiz
@app.route('/')
def home():
    return "Bem-vindo à API!"

if __name__ == '__main__':
    app.run(debug=True)
