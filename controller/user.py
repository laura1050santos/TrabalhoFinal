#add/excluir/editar/mostrar todos/mostrar por id ou nome
from flask import Flask, jsonify, render_template, Blueprint, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from database import init_db, db
from DAO import *
from repository import UserRepository

user_repository = UserRepository()

userController = Blueprint("User", __name__)

@userController.route('/ver-user')
def ver_user():
    user = user_repository.get_all_user()
    return render_template('lista_usuarios.html', user=user)

@userController.route('/add', methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        nome = request.form.get('register-nome')
        email = request.form.get('register-email')
        senha = request.form.get('register-senha')
        confirmar_senha = request.form.get('confirmar-senha')
        user_repository.create_user(nome, email, senha,confirmar_senha)
        
    return render_template('cadastro.html')
