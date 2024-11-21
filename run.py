from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=int(app.config.get("FLASK_PORT")))
