from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from config import config

bootstrap = Bootstrap()
moment = Moment()


#import logging
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #from .auth import auth as auth_blueprint
    #app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    return app

