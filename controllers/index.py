from flask import Blueprint

index = Blueprint(__name__, "index")


@index.route("/")
def index_page():
    return "<body>index</body>"
