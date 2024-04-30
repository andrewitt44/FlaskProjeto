from app import app, db
from flask import render_template, url_for, request, redirect
from app.forms import contatoForm, comentarioForm
from app.models import Contato, Comentario

@app.route('/')
def homepage():
    usuario = 'Cabecinha'
    idade = 34

    context = {
        'usuario':usuario,
        'idade':idade
    }
    return render_template('index.html', context=context)

@app.route('/contato/', methods =['GET', 'POST'])
def contato():
    form = contatoForm ( )
    context = {}
    if form.validate_on_submit ():
        form.save()
        return redirect (url_for('homepage'))
    return render_template ('contato.html', context=context, form=form)

@app.route('/contato/lista/')
def contatoLista():
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')
    dados = Contato.query.order_by('nome')
    if pesquisa != '':
        dados = dados.filter_by(nome=pesquisa)
    context = {'dados': dados.all()}    
    return render_template('contato_lista.html', context=context)

@app.route('/contato/<int:id>')
def contatoDetail(id):
    obj=Contato.query.get(id)
    return render_template('contato_detail.html' , obj=obj)

@app.route('/comentario/', methods =['GET', 'POST'])
def comentario():
    form = comentarioForm ( )
    context = {}
    if form.validate_on_submit ():
        form.save()
        return redirect (url_for('homepage'))
    return render_template ('comentario.html', context=context, form=form)
    
@app.route('/comentario/<int:id>')
def comentarioDetail(id):
    obj=Comentario.query.get(id)
    return render_template('contato_detail.html' , obj=obj)


#         contato = Contato (
#             nome = nome,
#             email = email,
#             assunto = assunto,
#             mensagem = mensagem
#         )
#         db.session.add(contato)
#         db.session.commit()

#     return render_template ('contato.html', context=context, form=form)


    # if request.method == 'GET':
    #     pesquisa = request.args.get('pesquisa')
    #     print(pesquisa)
    #     context.update({'pesquisa':pesquisa})
    # if request.method == 'POST':
    #     pesquisa = request.form['pesquisa']
    #     print('POST', pesquisa)
    #     context.update({'pesquisa':pesquisa})
    # return render_template('contato.html', context=context)