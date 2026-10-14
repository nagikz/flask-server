from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    # campo de texto obligatorio para el email del usuario, con validacion formato de
    email = StringField("Correo electronico", validators=[DataRequired(), Email()])

    # campo de contraseña obligatorio y con longitud minima de 6 caracteres.
    password = PasswordField("Contraseña", validators=[DataRequired(), Length(min=6)])

    # boton de envio del formulario
    submit = SubmitField("Iniciar sesión")
