from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from models import Fcuser
from werkzeug.security import check_password_hash

class RegisterForm(FlaskForm): 
    userid = StringField('userid', validators=[DataRequired()])        #id
    username = StringField('username', validators=[DataRequired()])    #이름 
    password = PasswordField('password', validators=[
        DataRequired(), EqualTo('re_password', message='비밀번호가 일치하지 않습니다.')
    ])
    re_password = PasswordField('re_password', validators=[DataRequired()])     #비밀번호 일치

class LoginForm(FlaskForm):
    userid = StringField('userid', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

    def validate_password(self, field):
        userid = self.userid.data
        password = field.data
        fcuser = Fcuser.query.filter_by(userid=userid).first()

        if not fcuser or not check_password_hash(fcuser.password, password):
            raise ValidationError('아이디 또는 비밀번호가 올바르지 않습니다.') 

#LoginForm에서 form.validate_on_submit()이 실행될 때, validate_password()가 자동 호출되어 비밀번호를 직접 비교

#check_password_hash()는 저장된 해시값과 입력값을 비교해서 로그인 가능 여부 판단

#실패하면 ValidationError 발생 -> 템플릿에 자동으로 에러 메시지 출력

