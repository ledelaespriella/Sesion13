from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class formEstudiante(FlaskForm):
    documento=StringField('Documento', validators=[DataRequired(message='No dejar vacio')],render_kw={'placeholder':'Identificación', 'class':'form_control'})
    nombre=StringField('Nombre', validators=[DataRequired(message='No dejar vacio')],render_kw={'placeholder':'Nombre', 'class':'form_control'})
    ciclo=SelectField('Ciclo', choices=[('python'),('Java'),('Web')])
    sexo=StringField('Sexo', validators=[DataRequired(message='No dejar vacio')],render_kw={'placeholder':'M/F', 'class':'form_control'})
    estado=BooleanField('Estado')
    
    enviar=SubmitField('Enviar',render_kw={'onmouseover':'guardarEst()','class':'form_boton'})
    consultar=SubmitField('Consultar', validators=None,render_kw={'onmouseover':'consultarEst()','class':'form_boton'})
    listar=SubmitField('Listar',render_kw={'onmouseover':'listarEst()','class':'form_boton'})
    actualizar=SubmitField('Actualizar',render_kw={'onmouseover':'actualizarEst()','class':'form_boton'})
    eliminar=SubmitField('Eliminar',render_kw={'onmouseover':'eliminarrEst()','class':'form_boton'})
    
class formLogin(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacio')], render_kw={'placeholder':'Usuario'} )
    clave = PasswordField('Clave', validators=[DataRequired(message='No dejar vacio')], render_kw={'placeholder':'Contraseña', 'id':'password'} )
    enviar = SubmitField('Enviar', render_kw={'class':'form_boton'} )