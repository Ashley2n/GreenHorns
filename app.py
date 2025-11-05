from flask import Flask, render_template
from models import *
from seed_data import campaigns_hc

app = Flask(__name__)
app.secret_key = 'BasicFlashSetup'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

hello :D