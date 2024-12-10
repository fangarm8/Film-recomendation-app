from flask import Flask

def register_routes(app: Flask):

    @app.route("/", methods=["GET"])
    def home():
        return "Started!"

    @app.route("/recommend", methods=["GET"])
    def recommend():
        return "Your recommendations will come soon!"