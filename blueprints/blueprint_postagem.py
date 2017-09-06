from flask import Blueprint, jsonify, request
import datetime
from Map2Rest import models

postagem = Blueprint("postagem", __name__)

@postagem.route('/postagens')
def lista_postagens():
    postagens = models.Postagem.query.all()
    return jsonify(result=[dict(id_postagem=postagem.id_postagem, titulo=postagem.titulo) for postagem in postagens])
