from flask import Flask, jsonify, make_response

from controller.auth_controller import auth_app
from controller.user_controller import user_app
from controller.admin_controller import admin_app

application = Flask(__name__)
application.config['SECRET_KEY'] = 'ForYou'


@application.route("/")
def hello_from_root():
    return jsonify(message='Hello, Hope you are doing well!')


@application.route("/hello")
def hello():
    return jsonify(message='Hello from path!')


@application.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)


application.register_blueprint(user_app, url_prefix='/rest/user')
application.register_blueprint(admin_app, url_prefix='/rest/admin')
application.register_blueprint(auth_app, url_prefix='/rest/auth')

if __name__ == '__main__':
    application.run(host="localhost", port=8080, debug=False)
    # application.run(host="127.0.0.1", port=5000, debug=True)
