from flask import Blueprint, jsonify, request
import datetime
from Map2Rest import models

relationships = Blueprint("relationships", __name__)

#One-to-Many: Livro>>>Revisão
@relationships.route('/livros')
def lista_livros():
    livros = models.Livro.query.all()
    return jsonify(result=[dict(id_livro=l.id, titulo=l.titulo, revisao= str(l.revisao)) for l in livros])


@relationships.route('/revisoes')
def lista_revisoes():
    revisoes = models.Revisao.query.all()
    return jsonify(result=[dict(id_revisor=r.id, nome_revisor=r.revisor_name, livro= str(r.livro_id)) for r in revisoes])

#One-to-One: Usuario>>>Endereço
@relationships.route('/usuarios')
def lista_usuarios():
    usuarios = models.Usuario.query.all()
    return jsonify(result=[dict(id_usuario=u.id_usuario, nome=u.nome, endereco= str(u.endereco)) for u in usuarios])


@relationships.route('/enderecos')
def lista_enderecos():
    enderecos = models.Endereco.query.all()
    return jsonify(result=[dict(id_endereco=e.id_endereco, cidade=e.cidade,UF=e.estado, usuario= str(e.usuario)) for e in enderecos])

#Many-to-Many: Entry>>>Tag
@relationships.route('/entries')
def lista_entries():
    entries = models.EntryModel.query.all()
    return jsonify(result=[dict(id_entry=entry.id_entry, titulo=entry.titulo, tags= str(entry.tags)) for entry in entries])


@relationships.route('/tags')
def lista_tags():
    tags = models.TagModel.query.all()
    return jsonify(result=[dict(id=t.id_tag, descricao=t.nome, entries= str(t.entries)) for t in tags])
