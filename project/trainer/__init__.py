from flask import Flask

def create_app():
    app = Flask(__name__)

    from .functions import main_fc, multi_instances, single_instance
    app.register_blueprint(main_fc.bp)
    app.register_blueprint(single_instance.bp)
    app.register_blueprint(multi_instances.bp)
    
    return app