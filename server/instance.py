from flask import Flask, Blueprint
from flask_restx import Api
import ssl
from ma import ma
from db import db

from marshmallow import ValidationError


class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.bluePrint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.bluePrint, doc='/doc', title='Sample Flask-RestPlus Application')
        self.app.register_blueprint(self.bluePrint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['PROPAGATE_EXCEPTIONS'] = True

        self.book_ns = self.book_ns()

        super().__init__()

    def book_ns(self, ):
        return self.api.namespace(name='Books', description='book related operations', path='/')

    def run(self, ):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.load_cert_chain('certificate.crt', 'private.key')
        self.app.run(
            port=443,
            ssl_context=context,
            debug=True,
            host='0.0.0.0'
        )


server = Server()
