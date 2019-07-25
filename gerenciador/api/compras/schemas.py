from flask_restplus import fields
from gerenciador.api import api


schemaCadastro = api.model('Cadastro', {
    'descricao': fields.String(required=True, description='Descrição da compra.'),
    'data_compra': fields.String(required=True, description='Data da compra.'),
    'valor': fields.Float(required=True, description='Valor da compra.'),
    'vencimento': fields.String(required=True, description='Vencimento da fatura do cartao.')
})

schemaResponseCadastro = api.model('Response Cadastro', {
    'id': fields.Integer(description='Id do cadastro.'),
    'descricao': fields.String(description='Descrição da compra.'),
    'data_compra': fields.String(description='Data da compra.'),
    'valor': fields.Float(description='Valor da compra.'),
    'vencimento': fields.String(description='Vencimento da fatura do cartao.'),
    'data_criacao': fields.DateTime(description='Data do cadastro.')
})