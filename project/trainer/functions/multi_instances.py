from flask import Blueprint

bp = Blueprint("multi_instances", __name__, url_prefix="/multi")

@bp.route("/object_detection")
def object_detection():
    return "<h2 align=center> here is object_detection page </h2>"

@bp.route("/instance_segmentation")
def instance_segmentation():
    return "<h2 align=center> here is instance segmentation page </h2>"