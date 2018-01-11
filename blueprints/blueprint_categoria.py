from flask import Blueprint, jsonify, request
import datetime
from Map2Rest import models

categoria = Blueprint("categoria", __name__)

@categoria.route('/categorias')
def lista_categorias():
    categorias = models.Categoria.query.get(1)
    print(categorias.postagens)

    return ('ok')
    #return jsonify(result=[dict(id_categoria=categoria.id_categoria, description=categoria.descricao) for categoria in categorias])
