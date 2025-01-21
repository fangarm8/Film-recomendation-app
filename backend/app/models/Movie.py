from ..database import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    budget = db.Column(db.Integer, nullable=True)
    genres = db.Column(db.String(500), nullable=True)
    overview = db.Column(db.String(1000), nullable=True)
    keywords = db.Column(db.String(1000), nullable=True)
    release_date = db.Column(db.Date)
    popularity = db.Column(db.Float, nullable=True)
    runtime = db.Column(db.Float, nullable=True)
    vote_average = db.Column(db.Float, nullable=True)
    poster_path = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<Film> {self.title}"