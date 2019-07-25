from flask_restplus import Resource
from flask import request, jsonify
from gerenciador.api import api
from gerenciador.api.compras.schemas import schemaResponseCadastro
from gerenciador.api.compras.controller import GerenciadorFinanceiro
import logging
import json


log = logging.getLogger(__name__)

ns = api.namespace(
    'gerenciador', description='Gerenciador Financeiro')


@ns.route('/cadastrar/<string:descricao>/<string:data_compra>/<string:valor>/<string:vencimento>/<string:observacoes>')
# @ns.route('/cadastrar')
@ns.param('descricao', 'Descrição da compra.')
@ns.param('data_compra', 'Data da compra.')
@ns.param('valor', 'Valor da compra.')
@ns.param('vencimento', 'Vencimento do cartão.')
@ns.param('observacoes', 'Observações sobre a compra.')
class Create(Resource):
    @ns.response(code=400, description="Bad Request")
    # @ns.expect(schemaCadastro, validate=True)
    # @ns.marshal_with(schemaResponseCadastro)
    def post(self, descricao, data_compra, valor, vencimento, observacoes):
        """
        Cadastra despesas
        """
        cad = GerenciadorFinanceiro()
        resp = cad.cadastrar_contas(descricao, data_compra, valor, vencimento, observacoes)

        return resp

