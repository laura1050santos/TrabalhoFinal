from model import Campeao
from database import db

class CampeaoDAO:

    @staticmethod
    def get_Campeao(id):
        return Campeao.query.get(id)
    
    @staticmethod
    def get_all_campeoes():
        return Campeao.query.all()
    
    @staticmethod
    def add_Campeao(nome, dificuldade, lancamento, funcao, classe, regiao):#????
        try:
            campeao= Campeao(nome=nome, dificuldade=dificuldade,lancamento=lancamento, funcao=funcao,classe=classe,regiao=regiao)
            db.session.add(campeao)
            db.session.commit()
            return True,campeao
        except Exception as e:
            db.session.rollback()
            return e 
    @staticmethod
    def delete_Campeao(id):
        try:
            campeao = CampeaoDAO.get_Campeao(id)
            db.session.delete(campeao)
            db.session.commit()
            return True,campeao
        except Exception as e:
            db.session.rollback()
            return e 
        
    @staticmethod
    def update_Campeao(nome, dificuldade, lancamento, funcao, classe, regiao):
        try:
            campeao = CampeaoDAO.get_Campeao(id)
            campeao.nome = nome
            campeao.dificuldade = dificuldade
            campeao.lancamento = lancamento
            campeao.funcao = funcao 
            campeao.classe = classe
            campeao.regiao = regiao
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e