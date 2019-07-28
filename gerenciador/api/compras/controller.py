from gerenciador.database.orm_gerenciador import Gerenciador
from gerenciador.utils.conector.mysql import MySqlDBContext
from gerenciador.database import engine
from datetime import datetime
import json

class GerenciadorFinanceiro(object):

    def __init__(self, dados):
        if dados is not None:
            self.descricao = dados.get('descricao')
            self.data_compra = dados.get('data_compra')
            self.valor = dados.get('valor')
            self.vencimento = dados.get('vencimento')
            self.observacoes = dados.get('observacoes')
        else:
            pass

    def cadastrar_contas(self):
        """
        Cadastra contas 
        """
        data = datetime.now()
        try:
            with MySqlDBContext(engine) as db:
                cad = Gerenciador()
                cad.descricao = self.descricao
                cad.data_compra = self.data_compra
                cad.valor = self.valor
                cad.vencimento = self.vencimento
                cad.data_criacao = data.strftime('%Y-%m-%d')
                cad.observacoes = self.observacoes
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

    def listar_contas(self):
        """
        Lista cadastros efetuados
        """

        try:
            lista = []
            with MySqlDBContext(engine) as db:
                contas = db.session.query(Gerenciador).all()
                db.session.close()

                for conta in contas:
                    dict_ = {
                        'id': conta.id,
                        'descricao': conta.descricao,
                        'data_compra': conta.data_compra,
                        'valor': conta.valor,
                        'vencimento': conta.vencimento,
                        'data_criacao': conta.data_criacao,
                        'observacoes': conta.observacoes
                    }
                    lista.append(dict_)
                response = lista

        except Exception as e:
            response = {
                "status": False,
                "erro": str(e),
                "msg": 'Consulta não pode ser Efetuada.',
            }
        
        return response

if __name__ == "__main__":
    r = GerenciadorFinanceiro(dados=None)
    r.listar_contas()
        