from flask import Blueprint, render_template, redirect, session, url_for, request

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")


@main.route("/app_01", methods=["GET", "POST"])
def app_01():
    return render_template("app1.html")

# TOGGLE THEME -------------------------------------------------------------

@main.get("/toggle_theme")
def toggle_theme():
    current_theme = session.get('theme', 'emerald')
    new_theme = 'business' if current_theme == 'emerald' else 'emerald'
    session['theme'] = new_theme
    return redirect(request.args.get("current_page"))
