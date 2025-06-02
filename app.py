import os
from flask import Flask, request, redirect, render_template, session, flash
from flask_wtf.csrf import CSRFProtect      #CSRF
from werkzeug.security import generate_password_hash
from models import db, Fcuser
from forms import RegisterForm, LoginForm

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        session['userid'] = form.userid.data
        return redirect('/')

    userid = session.get('userid')
    return render_template('hello.html', form=form, userid=userid)

@app.route('/register', methods=['GET', 'POST'])    #get -> 회원가입 폼 post -> 정보 DB에 저장 -> 성공시 register_success.html로 이동
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        fcuser = Fcuser()
        fcuser.userid = form.userid.data
        fcuser.username = form.username.data
        fcuser.password = generate_password_hash(form.password.data)

        db.session.add(fcuser)
        db.session.commit()

        return render_template('register_success.html')
    return render_template('register.html', form=form)

@app.route('/logout')       #logout
def logout():
    session.pop('userid', None)
    return redirect('/')

if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir, 'db.sqlite')     #dbsqlite 경로 생성

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile       #SQLAlchmy가 사용할 DB위치 설정
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True      
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'wcsfeufhwiquehfdx'      #세션 보호 비밀키 설정

    csrf = CSRFProtect()    #csrf보호에 필요
    csrf.init_app(app)  

    db.init_app(app)    #sqldb연동

    with app.app_context():
        db.create_all()

    app.run(host='127.0.0.1', port=5000, debug=True)
