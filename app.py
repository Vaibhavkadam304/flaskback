# from flask import Flask, jsonify
# from flask_cors import CORS
# from pymongo import MongoClient
# import os

# app = Flask(__name__)
# CORS(app)

# # Use the online database URL
# DATABASE_URL = 'mongodb+srv://vaibhav:chatrapati@cluster0.yvwdq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
# client = MongoClient(DATABASE_URL)

# # Replace 'mydatabase' with the actual database name
# db = client['mydatabase']

# # Replace 'mycollection' with the actual collection name
# collection = db['mycollection']

# @app.route('/api/data', methods=['GET'])
# def get_data():
#     data = list(collection.find({}, {'_id': 0}))
#     return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# Use the database URL from environment variables
DATABASE_URL = os.getenv('DATABASE_URL')
client = MongoClient(DATABASE_URL)

# Replace 'mydatabase' with the actual database name
db = client['mydatabase']

# Replace 'mycollection' with the actual collection name
collection = db['mycollection']

@app.route('/api/data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {'_id': 0}))
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))  # Default to port 5000 if not specified
    app.run(debug=True, port=port)

