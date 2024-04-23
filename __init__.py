from flask import Flask
from . import main
from .AppLayer.Controllers import guardsController, worksController

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main.main_blueprint)
    app.register_blueprint(guardsController.guardController_blueprint)
    app.register_blueprint(worksController.worksController_blueprint)

    return app


app = create_app()

