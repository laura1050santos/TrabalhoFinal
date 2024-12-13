#add/excluir/editar/mostrar todos/mostrar por id ou nome
from flask import Flask, jsonify, render_template, Blueprint, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from database import init_db
from repository import CampeaoRepository

campeoesController = Blueprint("campeao", __name__)
 
@campeoesController.route('/ver-campeao')
def ver_campeao():
    campeao= CampeaoRepository.get_campeao()

@campeoesController.route('/add')
def add_campeao():
    return 