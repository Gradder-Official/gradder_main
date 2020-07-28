from flask import Flask, jsonify


def create_app(config_name):
    app = Flask(__name__, static_folder="../build", static_url_path="/")

    @app.route("/")
    def index():
        return app.send_static_file("index.html")

    @app.route("/api")
    def api():
        test_json = {"hello": "world"}
        return jsonify(test_json)

    return app
