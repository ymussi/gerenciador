from gerenciador.database.orm_gerenciador import Gerenciador
from gerenciador.utils.conector.mysql import MySqlDBContext
from gerenciador.database import engine
from datetime import datetime
import json

class GerenciadorFinanceiro(object):

    def cadastrar_contas(self, descricao, data_compra, valor, vencimento):
        """
        Cadastra contas 
        """
        data = datetime.now()
        try:
            with MySqlDBContext(engine) as db:
                cad = Gerenciador()
                cad.descricao = descricao
                cad.data_compra = data_compra
                cad.valor = valor
                cad.vencimento = vencimento
                cad.data_criacao = data.strftime('%Y-%m-%d')
                db.session.add(cad)
                db.session.commit()

                response = {
                    "status": True,
                    "msg": 'Cadastro Efetuado com sucesso.'
                }

        except Exception as e:
            response = {
                "status": False,
                "erro": str(e),
                "msg": 'Cadastro não Efetuado.',
            }

        return response