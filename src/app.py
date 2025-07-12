"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, send_from_directory
from flask_migrate import Migrate
from flask_swagger import swagger
from api.utils import APIException, generate_sitemap
from api.models import db, User, Farm, NDVI_images, Aereal_images
from api.routes import api
from api.admin import setup_admin
from api.commands import setup_commands
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from base64 import b64encode
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

# from models import Person

ENV = "development" if os.getenv("FLASK_DEBUG") == "1" else "production"
static_file_dir = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '../dist/')

app = Flask(__name__)

# CORS(app)

app.url_map.strict_slashes = False

# database condiguration
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db, compare_type=True)
db.init_app(app)
CORS(app)

# add the admin
setup_admin(app)

# add the admin
setup_commands(app)

# Add all endpoints form the API with a "api" prefix
app.register_blueprint(api, url_prefix='/api')

# Handle/serialize errors like a JSON object

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints

@app.route('/')
def sitemap():
    if ENV == "development":
        return generate_sitemap(app)
    return send_from_directory(static_file_dir, 'index.html')

# any other endpoint will try to serve it like a static file
@app.route('/<path:path>', methods=['GET'])
def serve_any_other_file(path):
    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = 'index.html'
    response = send_from_directory(static_file_dir, path)
    response.cache_control.max_age = 0  # avoid cache memory
    return response

"""[GET] /users Listar todos los registros de usuario en la base de datos."""
@app.route('/users', methods=['GET'])
def get_all_users():

    users = User.query.all()
    return jsonify([item.serialize() for item in users]), 200

"""[GET] /user/<int:user_id> Muestra la información de un solo usuario según su id."""

@app.route('/user/<int:user_id>', methods=['GET'])
# @jwt_required()
def get_user():
    user_id = User.id
    single_user = User.query.get(user_id)

    if single_user is None:
        return jsonify({"error": "Person not found"}), 404
    else:
        return jsonify(single_user.serialize()), 200


"[GET] /ndvi Listar todos los registros de url NDVI en la base de datos."

@app.route('/ndvi', methods=['GET'])
def get_ndvi_images():
    all_ndvi = NDVI_images.query.all()
    return jsonify([item.serialize() for item in all_ndvi]), 200


"[GET] /aereal Listar todos los registros de url aereos en la base de datos."

@app.route('/aereal', methods=['GET'])
def get_ndvi_images():
    all_aereal = Aereal_images.query.all()
    return jsonify([item.serialize() for item in all_aereal]), 200


"[GET] /user-ndvi/<int:user_id> Muestra la información ndvi de un solo usuario según su id."

@app.route('/user-ndvi/<int:user_id>', methods=['GET'])
def get_ndvi_per_user():
    user_id = User.id
    ndvi_per_user = NDVI_images.query.get(user_id)

    if ndvi_per_user is None:
        return jsonify({"error": "NDVI images for this user does not exist"}), 404
    else:
        return jsonify(ndvi_per_user.serialize()), 200

"""Adicionalmente, necesitamos crear los siguientes endpoints para que podamos tener usuarios y favoritos en nuestro blog:
"""

"[GET] /user-aereal/<int:user_id> Listar todas las imagenes aereas que pertenecen al usuario actual."

@app.route('/user-aereal/<int:user_id>', methods=['GET'])
def get_aereal_per_user():
    user_id = User.id
    aereal_per_user = Aereal_images.query.get(user_id)

    if aereal_per_user is None:
        return jsonify({"error": "Aereal images for this user does not exist"}), 404
    else:
        return jsonify(aereal_per_user.serialize()), 200

""" [POST] /aereal_images/url_aereal/<int:user_id> Añade una nueva imagen aerea al usuario actual"""
   
@app.route('/user/<int:user_id>/aereal_images', methods=['POST'])
def post_new_aereal(user_id):
    body = request.json

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
        farm_location = farm_location,
        farm_name = farm_name,
        aereal_url = aereal_url,
        user_id = user_id  # clave foránea
    )

    try:
        db.session.add(new_aereal)
        db.session.commit()
        return jsonify({"message": "Aereal image added for successfully"}), 201
    
    except Exception as error:
        db.session.rollback()
        return jsonify({"error": str(error)}), 500   


"[POST] /favorite/ndvi_image/<int:people_id> Añade un nuevo ndvi al usuario actual."

@app.route('/user/<int:user_id>/ndvi_images', methods=['POST'])
def post_new_aereal(user_id):
    body = request.json

    farm_location = body.get("farm_location")
    farm_name = body.get("farm_name")
    ndvi_url = body.get("ndvi_url")
    user_id = body.get("user_id")

    # Verifica que el usuario exista
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    if not all([farm_location, farm_name, ndvi_url, user_id]):
        return jsonify({"error": "Missing required fields"}), 400
    
    # Defino nuevo registro
    
    new_ndvi = NDVI_images(
        farm_location = farm_location,
        farm_name = farm_name,
        ndvi_url = ndvi_url,
        user_id = user_id  # clave foránea
    )

    try:
        db.session.add(new_ndvi)
        db.session.commit()
        return jsonify({"message": "NDVI image added for successfully"}), 201
    
    except Exception as error:
        db.session.rollback()
        return jsonify({"error": str(error)}), 500
    

"[DELETE] /favorite/planet/<int:planet_id> Elimina una imagen con el id = ndvi_images_id. de un usuario determinado"

@app.route('/users/<int:user_id>/ndvi/<int:ndvi_images_id>', methods=['DELETE'])
def delete_ndvi_image(user_id, ndvi_images_id):

    # Buscar la imagen y verificar que pertenezca al usuario
    ndvi_to_delete = NDVI_images.query.filter_by(id = ndvi_images_id, user_id = user_id).first()

    if not ndvi_to_delete:
        return jsonify({"error": "NDVI image not found for this user"}), 404

    try:
        db.session.delete(ndvi_to_delete)
        db.session.commit()
        return jsonify({"message": "NDVI image deleted successfully"}), 200
    
    except Exception as error:
        db.session.rollback()
        return jsonify({"error": str(error)}), 500


@app.route('/ndvi_images/<int:ndvi_images_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):

    
    favorite = Favorite.query.filter_by(planet_id=planet_id).first()

    if not favorite:
        return jsonify({"error": "Favorite planet not found"}), 404

    
    db.session.delete(favorite)

    try:
        db.session.commit()
        return jsonify({"message": "Planet removed from favorites"}), 200
    except Exception as error:
        db.session.rollback()
        return jsonify({"error": str(error)}), 500

"[DELETE] /favorite/people/<int:people_id> Elimina un people favorito con el id = people_id."

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(people_id):

    
    favorite = Favorite.query.filter_by(people_id = people_id).first()

    if not favorite:
        return jsonify({"error": "Favorite people not found"}), 404

    
    db.session.delete(favorite)

    try:
        db.session.commit()
        return jsonify({"message": "People removed from favorites"}), 200
    except Exception as error:
        db.session.rollback()
        return jsonify({"error": str(error)}), 500
    
"[DELETE] /favorite/planet/<int:planet_id> Elimina una imagen con el id = aereal_images_id. de un usuario determinado"

@app.route('/users/<int:user_id>/ndvi/<int:aereal_images_id>', methods=['DELETE'])
def delete_ndvi_image(user_id, aereal_images_id):

    # Buscar la imagen y verificar que pertenezca al usuario
    aereal_to_delete = Aereal_images.query.filter_by(id = aereal_images_id, user_id = user_id).first()

    if not aereal_to_delete:
        return jsonify({"error": "NDVI image not found for this user"}), 404

    try:
        db.session.delete(aereal_to_delete)
        db.session.commit()
        return jsonify({"message": "Aereal image deleted successfully"}), 200
    
    except Exception as error:
        db.session.rollback()
        return jsonify({"error": str(error)}), 500

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)