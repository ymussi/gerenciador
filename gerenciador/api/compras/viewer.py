from flask_restplus import Resource
from flask import request, jsonify
from gerenciador.api import api
from gerenciador.api.compras.schemas import schemaResponseCadastro, schemaCadastro
from gerenciador.api.compras.controller import GerenciadorFinanceiro
import logging
import json


log = logging.getLogger(__name__)

ns = api.namespace(
    'gerenciador', description='Gerenciador Financeiro')


@ns.route('/cadastrar')
class Create(Resource):
    @ns.response(code=400, description="Bad Request")
    @ns.expect(schemaCadastro, validate=True)
    # @ns.marshal_with(schemaResponseCadastro)
    def post(self):
        """
        Cadastra despesas
        """
        dados = request.json
        print(dados)

        cad = GerenciadorFinanceiro(dados)
        resp = cad.cadastrar_contas()

        return resp

@ns.route('/listar')
class List(Resource):
    @ns.response(code=400, description="Bad Request")
    def get(self):
        """
        Lista cadastros efetuados
        """
        cad = GerenciadorFinanceiro(dados=None)
        resp = cad.listar_contas()

        return resp
