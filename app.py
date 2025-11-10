import base64
import os

from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify
from flask_login import logout_user, LoginManager, login_user, current_user, login_required
from flask_wtf import CSRFProtect
from fontTools.subset import closure_glyphs
from werkzeug.utils import secure_filename

from APIs.api_recipes_call import load_more_recipes_with_difficulty, load_difficulties, get_all_recipes, \
    load_more_recipes, load_specific_recipe
from APIs.api_recipes_call import load_more_recipes
from application.services import create_user_ser, get_user_by_username_ser, get_user_by_id_ser
from client.forms.ImageUploadForm import ImageUploadForm
from application.services import create_user_ser, get_user_by_username_ser, get_user_by_id_ser, save_user_avatar_ser
from domain.DTOs import CreateUserDto
from client.forms.LoginForm import LoginForm
from client.forms.RegisterForm import RegisterForm
from helper_functions import decrypt_password, encrypt_password, get_recipe_image
from image_analyzer import analyze_image, compare_images
from helper_functions import decrypt_password, encrypt_password, get_json_data_recipe, game_screen_data

app = Flask(__name__, template_folder='client/templates')

app = Flask(__name__, template_folder='client/templates')
UPLOAD_FOLDER = 'client/static/avatars'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app = Flask(__name__, template_folder='client/templates', static_folder='client/static')
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB
app.secret_key = 'CookQuestApp001'
app.config['UPLOAD_FOLDER'] = 'client/static/uploads'

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
                    return redirect(url_for("home"))
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
        return redirect(url_for('home'))
    return render_template('auth/register.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    session.clear()
    flash("You have been logged out", "success")
    return redirect(url_for('home'))

@app.route('/profile')
@login_required
def profile():
    render_template('profile/index.html', user=get_user_by_id_ser(current_user.id))


@app.route('/compare_images/<int:cuisine_id>', methods=['GET', 'POST'])
def upload_page(cuisine_id):
    form = ImageUploadForm()
    results = None
    similarity = None

    if form.validate_on_submit():
        print("Hi welcome to comparing Images")
        file = form.image.data
        filename = secure_filename(file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(image_path)

        # Example API call to get reference image
        # Getting Image from API
        reference_path = get_recipe_image(cuisine_id)


        # Analyze and compare
        results = analyze_image(image_path)
        similarity = compare_images(image_path, reference_path)

        print("References: ", reference_path)
        print("Results: ", results)
        print("Similarity: ", similarity)

    return render_template('game/upload.html', form=form, results=results, similarity=similarity)


@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return "No file uploaded", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(image_path)

    results = analyze_image(image_path)

    return render_template('result.html', results=results, filename=file.filename)

@app.route('/upload')
def upload():
    return render_template('game/uploadtest.html')

@app.route('/compare', methods=['POST'])
def compare():
    img1 = request.files['image1']
    img2 = request.files['image2']

    path1 = os.path.join(app.config['UPLOAD_FOLDER'], img1.filename)
    path2 = os.path.join(app.config['UPLOAD_FOLDER'], img2.filename)

    img1.save(path1)
    img2.save(path2)

    similarity = compare_images(path1, path2)

    return render_template('result.html', similarity=similarity)

@csrf.exempt
@app.route('/save-avatar', methods=['POST'])
@login_required
def save_avatar():
    try:
        data = request.get_json(force=True)  # force parsing
    except Exception as e:
        return {"error": str(e)}, 400

    if not data or 'image' not in data:
        return {"error": "Missing 'image' field"}, 400

    image_data = data['image']

    # Remove the 'data:image/png;base64,' part
    header, encoded = image_data.split(",", 1)
    binary_data = base64.b64decode(encoded)


    # save_folder = os.path.join(app.root_path, 'static', 'avatars')
    # os.makedirs(save_folder, exist_ok=True)

    # Save with a unique filename
    filename = f"user_{current_user.id}.png"  # you can add user_id here
    filepath = os.path.join(UPLOAD_FOLDER, filename)



    print("File Path: " + filepath)
    with open(filepath, "wb") as f:
        f.write(binary_data)

        # Save the path or URL in your database linked to the user
    user_id = current_user.id  # Example: replace with logged-in user's ID
    save_user_avatar_ser(user_id, filepath)

    # Return URL to frontend
    return jsonify({"url": '/' + filepath})

@app.route('/dashboard/game')
@login_required
def game_dashboard():
    return render_template('game/dashboard.html')

@app.route('/game/campaign')
@login_required
def campaign():
    return render_template('game/campaign.html')

@app.route('/game/campaign/<difficulty>')
@login_required
def campaign_difficulty(difficulty):
    if (difficulty == 'all'):
        get_all_cuisines = get_all_recipes()
        render_template('game/level_select.html', cuisine=get_all_cuisines)
    get_cuisines = load_difficulties(difficulty)
    #print(get_cuisines)
    return render_template('game/level_select.html', cuisine=get_cuisines)

@app.route('/game/campaign/<difficulty>/<cuisine>')
@login_required
def select(difficulty, cuisine):
    if difficulty == 'all':
        get_cuisines = load_more_recipes(cuisine)
        return render_template('game/select.html', cuisine=get_cuisines)
    get_cuisines = load_more_recipes_with_difficulty(difficulty, cuisine)
    return render_template('game/select.html', cuisine=get_cuisines)

@app.route('/avatar-create')
@login_required
def avatar_create():
    return render_template('profile/avatar_maker/index.html')

@app.route('/game/game_screen/<id>')
@login_required
def game_screen(id):
    specific_recipe = load_specific_recipe(id)
    print(specific_recipe)

    return render_template('game/game_screen.html', recipe=specific_recipe)

@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id_ser(user_id)


if __name__ == "__main__":
    app.run(debug=True)

# hello :D