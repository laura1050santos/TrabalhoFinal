from DAO import CampeaoDAO

class CampeaoRepository:
    def __init__(self) -> None:
        self.campeaoDAO = CampeaoDAO()

    def get_all_users(self):
        return self.campeaoDAO.get_all_users()

    def get_user_by_id(self, campeao_id):
        return self.campeaoDAO.get_user_by_id(campeao_id)

#     def create_user(self, name, classe, funcao):
#         return self.campeaoDAO.create_user(nome )

#     def update_user(self, campeao_id, name, classe, funcao):
#         return self.campeaoDAO.update_user(campeao_id,nome, classe, funcao)

#     def delete_user(self, campeao_id):
#         return self.campeaoDAO.delete_user(campeao_id)