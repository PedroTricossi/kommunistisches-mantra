import flask
from routes.routes_bp import frases_bp

app = flask.Flask(__name__)

app.register_blueprint(frases_bp)

if __name__ == "__main__":
    app.run()