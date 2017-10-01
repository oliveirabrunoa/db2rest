from flask import Blueprint, jsonify, request
import datetime
from Map2Rest import models

postagem = Blueprint("postagem", __name__)

@postagem.route('/postagens')
def lista_postagens():
    postagens = models.Postagem.query.all()[0]
    print(postagens.categoria.descricao)
    return 'ok'
    #return jsonify(result=[dict(id_postagem=postagem.id_postagem, titulo=postagem.categoria) for postagem in postagens])
