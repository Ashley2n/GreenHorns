from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_login import logout_user, LoginManager, login_user
from flask_wtf import CSRFProtect

from APIs.api_recipes_call import load_more_recipes
from application.services import create_user_ser, get_user_by_username_ser, get_user_by_id_ser
from domain.DTOs import CreateUserDto
from client.forms.LoginForm import LoginForm
from client.forms.RegisterForm import RegisterForm
from helper_functions import decrypt_password, encrypt_password

app = Flask(__name__, template_folder='client/templates', static_folder='client/static')

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

            user_exist = get_user_by_username_ser(username_input)

            if user_exist:
                decrypted_password = decrypt_password(user_exist.password_hash)
                if decrypted_password == password_input:
                    login_user(user_exist)
                    flash("You Have been Logged In", "success")
                    return redirect(url_for("game_dashboard"))
            flash("Incorrect email or Password", "danger")
    return render_template('auth/login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST':

        username = form.username.data
        password = form.password.data
        email = form.email.data

        encrypted_password = encrypt_password(password)

        if get_user_by_username_ser(username):
            flash("Username already taken", "danger")
            return render_template('auth/register.html', form=form)


        # TODO: Commit Changes
        new_user = create_user_ser(
            CreateUserDto(
                username=username,
                password=encrypted_password,
                email=email
            ))

        print(new_user)


        flash("You have been registered", "success")
        return redirect(url_for('game_dashboard'))
    return render_template('auth/register.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    session.clear()
    flash("You have been logged out", "success")
    return redirect(url_for('home'))

@app.route('/dashboard/game')
def game_dashboard():
    return render_template('game/dashboard.html')

@app.route('/game/game_screen')
def game_screen():
    return render_template('game/game_screen.html')

@app.route('/game/level_select')
def level_select():
    return render_template('game/level_select.html')

@app.route('/game/campaign/<cuisine>')
def campaign(cuisine):
    get_cuisines = load_more_recipes(cuisine)

    print(cuisine)
    return render_template('game/campaign.html', cuisine=get_cuisines)

@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id_ser(user_id)


if __name__ == "__main__":
    app.run(debug=True)

# hello :D