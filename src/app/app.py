import logging
import os

from application.exceptions import WrongFileStructureException
from controller.exceptions import BadRequestException
from configuration import (configure_application, configure_inject)
from flask import (Flask, jsonify)
from controller.hr_management import create_blueprint

def create_application() -> Flask:
    application = Flask(__name__)
    configure_application(application)
    configure_inject(application)
    
    @application.errorhandler(BadRequestException)
    @application.errorhandler(WrongFileStructureException)
    def handle_bad_request(error):
        response = jsonify(error.to_dict())
        response.status_code = 400
        return response
    
    application.register_blueprint(create_blueprint(), url_prefix='/api')

    return application





# @app.teardown_appcontext
# def teardown_db(exception=None):
#     db_con = g.pop('db_con', None)
#     if db_con is not None:
#         close_db_connection(db_con)
