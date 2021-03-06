# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request
import datetime
from DB2Rest import models

categoria = Blueprint("categoria", __name__)

@categoria.route('/categorias')
def lista_categorias():
    categorias = models.Categoria.query.all()
    return jsonify(result=[dict(id_categoria=categoria.id_categoria,
                                description=categoria.descricao, postagens=str(categoria.postagens)) for categoria in categorias])
