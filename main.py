import os
from flask import Flask, render_template, redirect
from forms.loginform import LoginForm
from data import db_session
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db_session.global_init(f'root:{os.getenv("PASSWORD_DATABASE")}@127.0.0.1:3306/{os.getenv("NAME_DATABASE")}')


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('index.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
