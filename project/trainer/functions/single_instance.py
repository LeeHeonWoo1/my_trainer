from flask import Blueprint

bp = Blueprint("single_instance", __name__, url_prefix="/single")

@bp.route("/classification")
def classification():
    return "<h2 align=center> here is classification page </h2>"


@bp.route("/transfer_learning")
def transfer_learning():
    return "<h2 align=center> here is classification with transfer learning page </h2>"