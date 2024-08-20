from flask import Flask, Blueprint, jsonify
import ssl
from flask_restx import Api
from ma import ma
from db import db

from resources.book import Book, BookList, book_ns
from marshmallow import ValidationError

from server.instance import server

api = server.api
app = server.app

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('certificate.crt', 'private.key')

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource
@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


api.add_resource(Book, '/books/<int:id>')
api.add_resource(BookList, '/books')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()
