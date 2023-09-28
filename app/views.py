import uuid
from flask import Blueprint, render_template, redirect, session, url_for, request
from app.forms import MovieForm
from app.pyscripts.supa_handler import create_supa, Movie, read_supa, select_from_id
from dataclasses import asdict
from app.pyscripts.movie_api import get_movie

main = Blueprint("main", __name__)

@main.route("/")
def index():
    movie_data = read_supa()
    movies = [Movie(**movie) for movie in movie_data]
    return render_template("index.html", title="Movies Watchlist", movies_data=movies)


@main.route("/add", methods=["GET", "POST"])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        get_info = get_movie(form.title.data)
        movie = Movie(
            _id=uuid.uuid4().hex,
            title=get_info["Title"],
            director=get_info["Director"],
            year=get_info["Year"],
            cast=get_info["Actors"],
            tags=get_info["Genre"],
            description=get_info["Plot"]
            )
        
        create_supa(asdict(movie))
        
        return redirect(url_for(".index"))

    return render_template(
        "new_movie.html", title="Movies Watchlist - Add Movie", form=form
    )


@main.get("/get/<string:_id>")
def movie(_id: str):
    movie_data = select_from_id(_id)
    movie = Movie(**movie_data)
    return render_template("movie_details.html", movie=movie)




# TOGGLE THEME -------------------------------------------------------------

@main.get("/toggle_theme")
def toggle_theme():
    current_theme = session.get('theme', 'emerald')
    new_theme = 'business' if current_theme == 'emerald' else 'emerald'
    session['theme'] = new_theme
    # return redirect(url_for('main.index'))
    return redirect(request.args.get("current_page"))