from flask import Flask
from database import init_db
from controller import campeoesController

app=Flask(__name__)

app.secret_key = 'Chave_mega_secreta' 

app.register_blueprint(campeoesController)
app.register_blueprint(userController)

if __name__ == "__main__":
    init_db(app)
    app.run(debug=False)