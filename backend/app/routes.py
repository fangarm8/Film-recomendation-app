from flask import Flask, render_template, request
from .database import db
from .models.Movie import Movie


def register_routes(app: Flask):

    @app.route("/")
    def home():
        page = request.args.get("page", 1, type=int)
        per_page = 20

        sort_by = request.args.get('sort_by', 'popularity') #popularity - сортировка по умолчанию

        valid_sort_fields = ['title', 'release_date', 'popularity']
        if sort_by not in valid_sort_fields:
            sort_by = 'popularity' #если поле не валидное, то сортировка по popularity

        movies = Movie.query.order_by(getattr(Movie, sort_by).desc()).paginate(page=page, per_page=per_page)
        return render_template('main/index.html', movies=movies, sort_by = sort_by)

    @app.route("/<int:movie_id>")
    def movie_info(movie_id):
        movie = Movie.query.get(movie_id)  # получение фильма, о котором нудны детали
        return render_template('info/base.html', movie=movie)

    @app.route("/search")
    def search():
        query = request.args.get('q', '')
        movies = Movie.query.filter(Movie.keywords.ilike(f"%{query}%")).all()
        return render_template('main/search.html', movies=movies)