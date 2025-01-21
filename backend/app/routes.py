from flask import Flask, render_template, request
from .database import db
from .models.Movie import Movie


def register_routes(app: Flask):

    @app.route("/")
    def home():
        movies = Movie.query.all()
        return render_template('index.html', movies=movies)

    @app.route("/search")
    def search():
        query = request.args.get('q', '')
        results = Movie.query.filter(Movie.title.ilike(f"%{query}%")).all()
        return render_template('search.html', results=results)

    @app.route("/addMovie/<id_par>")
    def add_movie(id_par):
        temp_movie = Movie(id = int(id_par), title = f"movie{id_par}", release_date = 2024, genre = 'action')
        db.session.add(temp_movie)
        db.session.commit()
        return "Movie added!"