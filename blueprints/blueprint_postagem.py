from flask import Blueprint, jsonify, request
import datetime
from Map2Rest import models

postagem = Blueprint("postagem", __name__)

@postagem.route('/postagens')
def lista_postagens():
    #postagens = models.Postagem.query.all()[0]
    #print(postagens.categoria.descricao)
    b = models.ReviewsModel.query.all()
    for boo in b:
        if boo.livro_id == 2:
            print(boo.revisor_name)
    return 'ok'
    #return jsonify(result=[dict(id_postagem=postagem.id_postagem, titulo=postagem.categoria) for postagem in postagens])

@postagem.route('/onetoone')
def testeonetoone():
    #postagens = models.Postagem.query.all()[0]
    #print(postagens.categoria.descricao)
    b = models.UsersModel.query.all()[0]
    print(b)
    return 'ok'


@postagem.route('/manytomany')
def testemanytomany():
    #postagens = models.Postagem.query.all()[0]
    #print(postagens.categoria.descricao)
    b = models.TagModel.query.all()[0]
    print(b.entries)
    return 'ok'
