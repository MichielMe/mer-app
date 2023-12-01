from app import create_app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    
# TODO - integrate app 7 in app 3
# TODO - refactor and clean up code