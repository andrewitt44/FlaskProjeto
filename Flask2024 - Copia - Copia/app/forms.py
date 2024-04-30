from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

from app import db
from app.models import Contato, Comentario

class contatoForm (FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    assunto = StringField('Assunto', validators=[DataRequired()])
    mensagem = StringField('Mensagem', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')
    def save(self):
        contato = Contato (
            nome = self.nome.data,
            email = self.email.data,
            assunto = self.assunto.data,
            mensagem = self.mensagem.data
        )
        db.session.add(contato)
        db.session.commit()

class comentarioForm (FlaskForm):
    comentario = StringField('Comentario', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')
    def save(self):
        comentario = Comentario (
            comentario = self.comentario.data
        )
        db.session.add(comentario)
        db.session.commit()
