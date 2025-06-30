# Inventory Management System Prototype

## Overview
A web-based inventory management system for tracking items, quantities, and prices, with data stored in AWS S3. Built using React (frontend) and Python Flask (backend), it reflects skills in Python, JavaScript, React, AWS, and Git.

## Setup Instructions
1. **Backend Setup**:
   - Install Python dependencies: `pip install flask flask-cors boto3`
   - Replace `YOUR_ACCESS_KEY`, `YOUR_SECRET_KEY`, and `your-bucket-name` in `app.py` with your AWS credentials and S3 bucket name.
   - Run the Flask server: `python app.py`

2. **Frontend Setup**:
   - Save `index.html` and open it in a browser. Ensure an internet connection for CDN dependencies (React, Axios, Tailwind CSS).
   - The frontend communicates with the backend at `http://localhost:5000`.

3. **AWS Configuration**:
   - Create an S3 bucket and set up IAM user with permissions for S3 read/write.
   - Ensure the bucket has CORS configured:
     ```json
     [
         {
             "AllowedHeaders": ["*"],
             "AllowedMethods": ["GET", "PUT", "POST", "DELETE"],
             "AllowedOrigins": ["http://localhost"],
             "MaxAgeSeconds": 3000
         }
     ]
     ```

## Features
- Add, view, and delete inventory items via a React interface.
- Store data in AWS S3 as a JSON file.
- Calculate total inventory value in real-time.
- Secure data access with AWS IAM principles.

## Usage
- Enter item name, quantity, and price in the form to add items.
- View the inventory table with real-time updates.
- Delete items using the "Delete" button.
- Total inventory value is displayed below the table.

## Notes
- Replace AWS credentials with your own for S3 access.
- Ensure Flask server is running before accessing the frontend.
- Prototype uses in-browser Babel for JSX; for production, set up a build process with Node.js and Babel.
