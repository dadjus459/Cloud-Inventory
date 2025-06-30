from flask import Flask, jsonify, request
from flask_cors import CORS
import boto3
import json
import uuid

app = Flask(__name__)
CORS(app)

# AWS S3 Configuration
s3 = boto3.client('s3', aws_access_key_id='YOUR_ACCESS_KEY', aws_secret_access_key='YOUR_SECRET_KEY')
BUCKET_NAME = 'your-bucket-name'

def load_inventory():
    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key='inventory.json')
        return json.loads(response['Body'].read().decode('utf-8'))
    except s3.exceptions.NoSuchKey:
        return []
    except Exception as e:
        print(f"Error loading inventory: {e}")
        return []

def save_inventory(inventory):
    try:
        s3.put_object(Bucket=BUCKET_NAME, Key='inventory.json', Body=json.dumps(inventory))
    except Exception as e:
        print(f"Error saving inventory: {e}")

@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    inventory = load_inventory()
    return jsonify(inventory)

@app.route('/api/inventory', methods=['POST'])
def add_item():
    data = request.json
    inventory = load_inventory()
    new_item = {
        'id': str(uuid.uuid4()),
        'name': data['name'],
        'quantity': data['quantity'],
        'price': data['price']
    }
    inventory.append(new_item)
    save_inventory(inventory)
    return jsonify({'message': 'Item added'}), 201

@app.route('/api/inventory/<id>', methods=['DELETE'])
def delete_item(id):
    inventory = load_inventory()
    inventory = [item for item in inventory if item['id'] != id]
    save_inventory(inventory)
    return jsonify({'message': 'Item deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)