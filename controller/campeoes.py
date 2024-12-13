#add/excluir/editar/mostrar todos/mostrar por id ou nome
from flask import Flask, jsonify, render_template, Blueprint, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from database import init_db, db
from DAO import *
from repository import CampeaoRepository

campeoes_repository = CampeaoRepository()

campeoesController = Blueprint("campeao", __name__)

@campeoesController.route('/ver-campeoes')
def ver_campeao():
    campeao= CampeaoRepository.get_all_campeoes()
    return render_template('ex.html', campeao=campeao)

@campeoesController.route('/add')
def add_campeao():
    
    return render_template('ex.html')
