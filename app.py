from flask import Flask, request, redirect, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import Cupcake, db, connect_db
# from forms import AnimalForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ihaveasecret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolabar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


def serialize_cupcakes(cupcake):
    """Serialize a dessert SQLAlchemy obj to dictionary."""

    return {
        "id": cupcake.id,
        "name": cupcake.name,
        "calories": cupcake.calories,
    }

@app.route("/cupcakes")
def list_all_cupcakes():
    """Return JSON {'desserts': [{id, name, calories}, ...]}"""

    cupcakes = Cupcake.query.all()
    serialized = [serialize_cupcakes(d) for d in cupcakes]

    return jsonify(cupcakes=serialized)

@app.route('/api/cupcakes/<id>')
def list_cupcake(id):
    """Return JSON {'dessert': {id, name, calories}}"""

    cupcake = Cupcake.query.get(id)
    serialized = serialize_cupcakes(cupcake)

    return jsonify(cupcake=serialized)