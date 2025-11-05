from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_login import logout_user, LoginManager
from flask_wtf import CSRFProtect

from infrastructure.CRUD import get_user_by_username, create_user, get_by_id
from forms.LoginForm import LoginForm
from forms.RegisterForm import RegisterForm
from helper_functions import decrypt_password, encrypt_password

app = Flask(__name__)
app.secret_key = 'CookQuestApp001'

csrf = CSRFProtect(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            username_input = form.username.data
            password_input = form.password.data

            user_exist = get_user_by_username(db_session, username_input)

            if user_exist:
                decrypted_password = decrypt_password(user_exist.password)
                if decrypted_password == password_input:
                    login_user(user_exist)
                    flash("You Have been Logged In", "success")
                    return render_template('game/dashboard.html')
            flash("Incorrect email or Password", "danger")
    return render_template('')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        email = form.email.data

        encrypted_password = encrypt_password(password)

        # TODO: Commit Changes
        new_user = create_user(session=db_session, username=username, hashed_password=encrypted_password, email=email)

        print(new_user)


        flash("You have been registered", "success")
        return redirect(url_for('game_dashboard'))
    return render_template('auth/register.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    session.clear()
    flash("You have been logged out", "success")
    return redirect(url_for('landing'))

@login_manager.user_loader
def load_user(user_id):
    return get_by_id(db_seesion, user_id)

if __name__ == "__main__":
    app.run(debug=True)

# hello :D