#add/excluir/editar/mostrar todos/mostrar por id ou nome
from flask import Flask, jsonify, render_template, Blueprint, redirect, url_for,request
from flask_sqlalchemy import SQLAlchemy
from database import init_app, db
from DAO.campeoes import *
from repository.campeaoRepository import CampeaoRepository

campeoes_repository = CampeaoRepository()

campeoesController = Blueprint("campeao", __name__)

@campeoesController.route('/ver-campeoes')
def ver_campeao():
    campeao= CampeaoRepository.get_all_campeoes()
    return render_template('get_id_campeao.html', campeao=campeao)

@campeoesController.route('/add_campeao')
def add_campeao():
    if request.method == 'POST':
        nome = request.form.get('nome')
        dificuldade = request.form.get('dificuldade')
        campeoes_repository.create_campeao(nome,dificuldade) #chama a função do repository que 
        return redirect(url_for('campeoesController.ver_todos'))
    return render_template('add_campeao.html')

    
