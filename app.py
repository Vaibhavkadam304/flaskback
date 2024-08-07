import os
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

DATABASE_URL = os.getenv('DATABASE_URL')
client = MongoClient(DATABASE_URL)

db = client['mydatabase']
collection = db['mycollection']

@app.route('/api/data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {'_id': 0}))
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 4000))  # Use environment variable PORT or default to 4000
    app.run(host='0.0.0.0', port=port, debug=True)  # Ensure host is set to '0.0.0.0'
