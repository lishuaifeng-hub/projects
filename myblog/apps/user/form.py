from models import User
from flask_wtf import FlaskForm
from wtforms import fields, validators, ValidationError

class LoginForm(FlaskForm):
    """登录表单"""
    username = fields.StringField(validators=[validators.data_required()])
    password = fields.PasswordField(validators=[validators.data_required()])

    def validate_username(self, field):
        """登录校验"""
        user = self.get_user()

        if user is None:
            raise ValidationError('Invalid user')
        if self.password.data != user.password:
            raise ValidationError('Invalid password')

    def get_user(self):
        return User.query.filter_by(id=self.username.data, isAdmin=1).first()
