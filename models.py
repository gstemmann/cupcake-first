from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):

    db.app = app
    db.init_app(app)

defaut_img = 'https://tinyurl.com/demo-cupcake'

class Cupcake(db.Model):
   

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=defaut_img)
    
   
def connect_db(app):
    """Connect this database to provided Flask app.
    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)