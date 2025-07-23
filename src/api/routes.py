"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Farm, NDVI_images, Aereal_images
from api.utils import generate_sitemap, APIException, send_email
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from base64 import b64encode
import os
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

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
expires_token = 200
expires_delta = timedelta(hours=expires_token)


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


@api.route('/api/register', methods=['POST'])
def add_user():
    data = request.json

    print(data)

    full_name = data.get("full_name", None)
    email = data.get("email", None)
    phone_number = data.get("phone_number", None)
    avatar = data.get("avatar", None)
    password = data.get("password", None)

    # Creación del usuario:
    if any(field is None or field == "" for field in [full_name, email, phone_number, password]):
        return jsonify('Error: Fields full_name, email, phone_number, and password are mandatory'), 400

    # Verificar si el usuario ya existe
    existing_user = User.query.filter_by(email=email).one_or_none()
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    try:
        # Crear el salt antes de crear la contraseña
        salt = b64encode(os.urandom(32)).decode("utf-8")

        # Crear el usuario
        user = User()
        user.full_name = full_name
        user.email = email
        user.phone_number = phone_number
        user.avatar = avatar
        user.salt = salt
        user.password = create_password(password, salt)

        # Transacción a la BD:
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "User created successfully"}), 201

    except Exception as error:
        db.session.rollback()
        return jsonify(f"Error: {error.args}"), 500


@api.route('/login', methods=['POST'])      # agregar jwt autentification
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
                return jsonify("Credentials failure"), 401


# @api.route("/users", methods=["GET"])
# @jwt_required()
# def get_all_users():
#     users = User.query.all()
#     return jsonify(list(map(lambda item: item.serialize(), users))), 200


@api.route("/user-login", methods=["GET"])
@jwt_required()
def one_user_login():
    user_id = get_jwt_identity()

    user = User.query.get(user_id)
    if user is None:
        return jsonify("User not found"), 404
    else:
        return jsonify(user.serialize()), 200


@api.route("/api/reset-password", methods=["POST"])
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


@api.route("/api/update-password", methods=["PUT"])
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


@api.route('/api/about-us', methods=['GET'])
def get_about_us():
    return jsonify({
        "message": {
            "mission": "Mediante el uso de Inteligencia Artificial...",
            "technology": "Nuestra plataforma utiliza algoritmos...",
            "history": "AgriVision AI nació con la visión..."
        }
    }), 200


# @api.route('/dashboard-put', methods=['PUT'])
# def put_dashboard():
#     user_id = get_jwt_identity()
#     body = request.get_json()
#     user = User.query.filter_by(user_id=user_id).one_or_none()

#     if user is None:
#         return jsonify(
#             {"Error": "User not found"}
#         ), 404
#     else:
#         return(

#         ), 200

@api.route('/api/dashboard', methods=['GET'])
def get_dashboard():
    user_id = get_jwt_identity()
    body = request.get_json()
    # user = User.query.filter_by(user_id=user_id).one_or_none()

    user = User.query.get(user_id)

    if user is None:
        return jsonify(
            {"Error": "User not found"}
        ), 404
    else:
        return jsonify(
            {'message': 'Bienvenido a tu dashboard de Agrovision IA! Acá podras ver el análisis del historial de tu huerto, reportes guardados, y configuraciones de cuenta'}
        ), 200

# @api.route("/update-password", methods=["PUT"])
# @jwt_required()
# def update_password():
#     user_id = get_jwt_identity()
#     body = request.get_json()
#     user = User.query.filter_by(user_id=user_id).one_or_none()

#     if user is not None:
#         salt = b64encode(os.urandom(32)).decode("utf-8")
#         new_password = body.get("new_password", None)

#         if not new_password:
#             return jsonify({"Error": "The password was not updated"}), 400

#         password = create_password(new_password, salt)

#         user.salt = salt
#         user.password = password

#         try:
#             db.session.commit()
#             return jsonify("Password changed successfuly"), 201
#         except Exception as error:
#             db.session.rollback()
#             return jsonify(f"Error: {error.args}"), 500

#     else:
#         return jsonify({"Error": "User not found"}), 404


"""[GET] /users Listar todos los registros de usuario en la base de datos."""

@api.route('/api/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([item.serialize() for item in users]), 200


"""[GET] /user/<int:user_id> Muestra la información de un solo usuario según su id."""

@api.route('/user/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user():
    user_id = get_jwt_identity()
    single_user = User.query.get(user_id=user_id)

    if single_user is None:
        return jsonify({"error": "Person not found"}), 404
    else:
        return jsonify(single_user.serialize()), 200


"[GET] /ndvi Listar todos los registros de url NDVI en la base de datos."

@api.route('/ndvi', methods=['GET'])
def get_ndvi_images():
    all_ndvi = NDVI_images.query.all()
    return jsonify([item.serialize() for item in all_ndvi]), 200


"[GET] /aereal Listar todos los registros de url aereos en la base de datos."

@api.route('/aereal', methods=['GET'])
def get_aereal_images():
    all_aereal = Aereal_images.query.all()
    return jsonify([item.serialize() for item in all_aereal]), 200


"[GET] /user-ndvi/<int:user_id> Muestra la información ndvi de un solo usuario según su id."

@api.route('/user-ndvi/<int:user_id>', methods=['GET'])
def get_ndvi_per_user():
    user_id = User.id
    ndvi_per_user = NDVI_images.query.get(user_id)

    if ndvi_per_user is None:
        return jsonify({"error": "NDVI images for this user does not exist"}), 404
    else:
        return jsonify(ndvi_per_user.serialize()), 200

"[GET] /user-aereal/<int:user_id> Listar todas las imagenes aereas que pertenecen al usuario actual."

@api.route('/user-aereal/<int:user_id>', methods=['GET'])
def get_aereal_per_user():
    user_id = User.id
    aereal_per_user = Aereal_images.query.get(user_id)

    if aereal_per_user is None:
        return jsonify({"error": "Aereal images for this user does not exist"}), 404
    else:
        return jsonify(aereal_per_user.serialize()), 200


""" [POST] /aereal_images/url_aereal/<int:user_id> Añade una nueva imagen aerea al usuario actual"""

@api.route('/user/<int:user_id>/aereal_images', methods=['POST'])
def post_new_aereal(user_id):
    body = request.json

    farm_location = Farm.farm_location
    farm_name = Farm.farm_name

    aereal_farm_location = Farm.query.get(farm_location)
    aereal_farm_name = Farm.query.get(farm_name)
    aereal_url = body.get("aereal_url")

    farm_location = body.get("farm_location")
    farm_name = body.get("farm_name")
    aereal_url = body.get("aereal_url")
    user_id = body.get("user_id")

    # Verifica que el usuario exista
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    if not all([farm_location, farm_name, aereal_url, user_id]):
        return jsonify({"error": "Missing required fields"}), 400

    # Defino nuevo registro

    new_aereal = Aereal_images(
        farm_location=farm_location,
        farm_name=farm_name,
        aereal_url=aereal_url,
        user_id=user_id  # clave foránea
    )

    try:
        db.session.add(new_aereal)
        db.session.commit()
        return jsonify({"message": "Aereal image added for successfully"}), 201

    except Exception as error:
        db.session.rollback()
        return jsonify({"error": str(error)}), 500


"[POST] /favorite/ndvi_image/<int:people_id> Añade un nuevo ndvi al usuario actual."

# @api.route('/user/<int:user_id>/ndvi_images', methods=['POST'])
# def post_new_aereal(user_id):
#     body = request.json

#     farm_location = body.get("farm_location")
#     farm_name = body.get("farm_name")
#     ndvi_url = body.get("ndvi_url")
#     user_id = body.get("user_id")

#     # Verifica que el usuario exista
#     user = User.query.get(user_id)
#     if not user:
#         return jsonify({"error": "User not found"}), 404

#     if not all([farm_location, farm_name, ndvi_url, user_id]):
#         return jsonify({"error": "Missing required fields"}), 400

#     # Defino nuevo registro

#     new_ndvi = NDVI_images(
#         farm_location = farm_location,
#         farm_name = farm_name,
#         ndvi_url = ndvi_url,
#         user_id = user_id  # clave foránea
#     )

#     try:
#         db.session.add(new_ndvi)
#         db.session.commit()
#         return jsonify({"message": "NDVI image added for successfully"}), 201

#     except Exception as error:
#         db.session.rollback()
#         return jsonify({"error": str(error)}), 500


"[DELETE] Elimina una imagen con el id = ndvi_images_id. de un usuario determinado"

@api.route('/users/<int:user_id>/ndvi/<int:ndvi_images_id>', methods=['DELETE'])
def delete_ndvi_image(user_id, ndvi_images_id):

    # Buscar la imagen y verificar que pertenezca al usuario
    ndvi_to_delete = NDVI_images.query.filter_by(
        id=ndvi_images_id, user_id=user_id).first()

    if not ndvi_to_delete:
        return jsonify({"error": "NDVI image not found for this user"}), 404

    try:
        db.session.delete(ndvi_to_delete)
        db.session.commit()
        return jsonify({"message": "NDVI image deleted successfully"}), 200

    except Exception as error:
        db.session.rollback()
        return jsonify({"error": str(error)}), 500


# @app.route('/ndvi_images/<int:ndvi_images_id>', methods=['DELETE'])
# def delete_favorite_planet(planet_id):


#     favorite = .query.filter_by(planet_id=planet_id).first()

#     if not favorite:
#         return jsonify({"error": "Favorite planet not found"}), 404


#     db.session.delete(favorite)

#     try:
#         db.session.commit()
#         return jsonify({"message": "Planet removed from favorites"}), 200
#     except Exception as error:
#         db.session.rollback()
#         return jsonify({"error": str(error)}), 500

# "[DELETE] /favorite/people/<int:people_id> Elimina un people favorito con el id = people_id."

# @app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
# def delete_favorite_people(people_id):


#     favorite = Favorite.query.filter_by(people_id = people_id).first()

#     if not favorite:
#         return jsonify({"error": "Favorite people not found"}), 404


#     db.session.delete(favorite)

#     try:
#         db.session.commit()
#         return jsonify({"message": "People removed from favorites"}), 200
#     except Exception as error:
#         db.session.rollback()
#         return jsonify({"error": str(error)}), 500

"[DELETE] Elimina una imagen con el id = aereal_images_id. de un usuario determinado"

# @api.route('/users/<int:user_id>/ndvi/<int:aereal_images_id>', methods=['DELETE'])
# def delete_ndvi_image(user_id, aereal_images_id):

#     # Buscar la imagen y verificar que pertenezca al usuario
#     aereal_to_delete = Aereal_images.query.filter_by(id = aereal_images_id, user_id = user_id).first()

#     if not aereal_to_delete:
#         return jsonify({"error": "NDVI image not found for this user"}), 404

#     try:
#         db.session.delete(aereal_to_delete)
#         db.session.commit()
#         return jsonify({"message": "Aereal image deleted successfully"}), 200

#     except Exception as error:
#         db.session.rollback()
#         return jsonify({"error": str(error)}), 500
