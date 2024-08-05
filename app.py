from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

DATABASE_URL = os.getenv('DATABASE_URL')
PORT = int(os.getenv('PORT', 5000))

client = MongoClient(DATABASE_URL)

db = client['mydatabase']
collection = db['mycollection']

@app.route('/api/data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {'_id': 0}))
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
