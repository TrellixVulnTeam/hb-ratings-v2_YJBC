"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String,
                        nullable=False, 
                        unique=True)
    password = db.Column(db.String,
                        nullable=False)

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Rating(db.Model):
    """A user."""

    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key= True)
    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.user_id'))
    movie_id = db.Column(db.Integer,  
                        db.ForeignKey('movies.movie_id'))
    rating = db.Column(db.Integer,
                        nullable=False)

    def __repr__(self):
        return f'<Rating rating_id={self.rating_id} movie_id={self.movie_id} rating={self.rating}>'

class Movie(db.Model):
    """A user."""

    __tablename__ = 'movies'

    movie_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    title = db.Column(db.String,
                        nullable=False)
    description = db.Column(db.String)
    rating_id = db.Column(db.Integer,
                        db.ForeignKey('ratings.rating_id'))

    def __repr__(self):
        return f'<Rating rating_id={self.rating_id} movie_id={self.movie_id} rating={self.rating} title={self.title} description={self.description}>'


def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
