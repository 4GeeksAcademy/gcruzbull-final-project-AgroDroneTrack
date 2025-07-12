"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException, send_email
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from base64 import b64encode
import os
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

# api = Blueprint('api', __name__)

# # Allow CORS requests to this API
# CORS(api)


# @api.route('/hello', methods=['POST', 'GET'])
# def handle_hello():

#     response_body = {
#         "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
#     }

#     return jsonify(response_body), 200


api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


# Manejo del Hash de la contraseña creando 2 funciones

def create_password(password, salt):
    return generate_password_hash(f"{password}{salt}")


def check_password(password_hash, password, salt):
    return check_password_hash(password_hash, f"{password}{salt}")

# Acá termina el manejo del Hash.


# Duración de vida del token
expires_token = 20
expires_delta = timedelta(minutes=expires_token)


@api.route('/healt-check', methods=['GET'])
def handle_check():

    response_body = {
        "message": "Todo esta ok"
    }

    return jsonify(response_body), 200


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/signup', methods=['POST'])
def add_user():
    data = request.json

    full_name = data.get("full_name", None)
    email = data.get("email", None)
    phone_number = data.get("phone_number", None)
    farm_location = data.get("farm_location", None)
    farm_name = data.get("farm_name", None)
    avatar = data.get("avatar", None)
    password = data.get("password", None)
    salt = data.get("salt", None) 

    # Creación del usuario:
    if any(field is None for field in [full_name, email, phone_number, farm_location, farm_name, password]):
        return jsonify('Fields full_name, email, phone_number, farm_location, farm_name, and password are mandatory'), 400
    else:
        user = User()
        user.full_name = full_name
        user.email = email
        user.farm_name = farm_name
        user.phone_number = phone_number
        user.avatar = avatar
        user.password = create_password(password)
        user.salt = b64encode(os.urandom(32)).decode("utf-8")

    # Transacción a la BD:
    db.session.add(user)

    try:
        db.session.commit()
        return jsonify("User created successfully"), 201
    except Exception as error:
        db.session.rollback()
        return jsonify(f"Error: {error.args}"), 500


@api.route('/login', methods=['POST'])
def handle_login():
    data = request.json
    email = data.get("email", None)
    password = data.get("password", None)

    if email is None or password is None:
        return jsonify('You must write the email and password'), 400

    # Validamos existencia del usuario
    else:
        user = User.query.filter_by(email=email).one_or_none()
        if user is None:
            return jsonify("Credentials are wrong, try again"), 400
        else:
            if check_password(user.password, password, user.salt):
                token = create_access_token(identity=str(user.id))
                return jsonify({
                    "token": token}), 200
            else:
                return jsonify("Credentials failure"), 400


@api.route("/users", methods=["GET"])
@jwt_required()
def get_all_users():
    users = User.query.all()
    return jsonify(list(map(lambda item: item.serialize(), users))), 200


@api.route("/user-login", methods=["GET"])
@jwt_required()
def one_user_login():
    user_id = get_jwt_identity()

    user = User.query.get(user_id)
    if user is None:
        return jsonify("User not found"), 404
    else:
        return jsonify(user.serialize())


@api.route("/reset-password", methods=["POST"])
def reset_password_user():
    body = request.json

    user = User.query.filter_by(email=body).one_or_none()

    if user is None:
        return jsonify("User not found"), 404
    else:
        create_token = create_access_token(
            identity=body, expires_delta=expires_delta), 200

    message_url = f""" 
    <a href="{os.getenv("FRONTEND_URL")}/reset-password?token={create_token}">Recuperar contraseña</a>
"""
    data = {
        "subject": "Password recovery",
        "to": body,
        "message": message_url
    }

    sended_email = send_email(
        data.get("subject"), data.get("to"), data.get("message"))

    if sended_email:
        return jsonify("Message sent successfully"), 200
    else:
        return jsonify("Error"), 400


@api.route("/update-password", methods=["PUT"])
@jwt_required()
def update_password():
    user_id = get_jwt_identity()
    body = request.get_json()
    user = User.query.filter_by(user_id=user_id).one_or_none()

    if user is not None:
        salt = b64encode(os.urandom(32)).decode("utf-8")
        new_password = body.get("new_password", None)

        if not new_password:
            return jsonify({"Error": "The password was not updated"}), 400

        password = create_password(new_password, salt)

        user.salt = salt
        user.password = password

        try:
            db.session.commit()
            return jsonify("Password changed successfuly"), 201
        except Exception as error:
            db.session.rollback()
            return jsonify(f"Error: {error.args}"), 500
        
    else:
        return jsonify({"Error": "User not found"}), 404


@api.route('/about-us', methods=['GET'])
def get_about_us():
    return jsonify({
        "message": {
            "mission": "Mediante el uso de Inteligencia Artificial...",
            "technology": "Nuestra plataforma utiliza algoritmos...",
            "history": "AgriVision AI nació con la visión..."
        }
    }), 200


@api.route('/dashboard', methods=['PUT'])
def put_dashboard():
    user_id = get_jwt_identity()
    body = request.get_json()
    user = User.query.filter_by(user_id=user_id).one_or_none()

    if user is None:
        return jsonify(
            {"Error": "User not found"}
        ), 404
    else:
        return(
            
        )

    
    return jsonify({
        # "message": {
        #     "mission": "Mediante el uso de Inteligencia Artificial...",
        #     "technology": "Nuestra plataforma utiliza algoritmos...",
        #     "history": "AgriVision AI nació con la visión..."
        # }
    }), 200

@api.route("/update-password", methods=["PUT"])
@jwt_required()
def update_password():
    user_id = get_jwt_identity()
    body = request.get_json()
    user = User.query.filter_by(user_id=user_id).one_or_none()

    if user is not None:
        salt = b64encode(os.urandom(32)).decode("utf-8")
        new_password = body.get("new_password", None)

        if not new_password:
            return jsonify({"Error": "The password was not updated"}), 400

        password = create_password(new_password, salt)

        user.salt = salt
        user.password = password

        try:
            db.session.commit()
            return jsonify("Password changed successfuly"), 201
        except Exception as error:
            db.session.rollback()
            return jsonify(f"Error: {error.args}"), 500
        
    else:
        return jsonify({"Error": "User not found"}), 404
