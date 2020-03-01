from flask import Flask, request, Response, jsonify
from bson.json_util import dumps
from pymongo import MongoClient
import json
import uuid
import os

app = Flask(__name__)

if "MONGO_DB_DKR" in os.environ.keys():
    mongo_url = os.environ["MONGO_DB_DKR"]
else:
    mongo_url = "mongodb://localhost:27017/"

client = MongoClient(mongo_url)
db = client.zinobedb

regions = db.countries
tokens = db.tokens
users = db.users

users.insert_one({'email': 'admin@zinobe.com'})

@app.route('/api/regions/', methods=['GET'])
def listregions():
    owner = request.headers.get('owner')
    token = request.headers.get('token')
    t = tokens.find_one({'owner': owner})
    if t == None:
        return Response("No existe un token de autorización para el usuario")
    if t['token_id'] == token:
        return jsonify({'result': dumps(regions.find())})
    else:
        return Response("Token inválido", mimetype='application/json', status=200)
    

@app.route('/api/token/', methods=['POST'])
def createToken():
    email = request.form.get('owner')
    token_id = str(uuid.uuid1())
    token = tokens.insert_one({
        'owner': email,
        'token_id': token_id
    })
    return token_id, 201

@app.route('/api/public/', methods=['GET'])
def publicRegions():
    return jsonify({'result': dumps(regions.find())})


if __name__ == "__main__":    
    app.run()   