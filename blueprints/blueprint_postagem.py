from flask import Blueprint, jsonify, request
import datetime
from DB2Rest import models

postagem = Blueprint("postagem", __name__)

@postagem.route('/postagens')
def lista_postagens():
    postagens = models.Postagem.query.all()
    return jsonify(result=[dict(id_postagem=p.id_postagem, titulo=p.titulo,
                                data=str(p.data_postagem),hora=str(p.hora_postagem),
                                categoria = str(p.categoria)) for p in postagens])
