from flask import Flask, request, jsonify
import csv
import tempfile
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Received JSON payload:", req)

    name = req['queryResult']['parameters']['person']['name']
    email = req['queryResult']['parameters']['email']
    phone = req['queryResult']['parameters']['number']
    city = req['queryResult']['parameters']['geo-city']
    dob = req['queryResult']['parameters']['date-time']

    print("Extracted data:")
    print("Name:", name)
    print("Email:", email)
    print("Phone:", phone)
    print("City:", city)
    print("Date of Birth:", dob)

    # Create a temporary file to write data
    with tempfile.NamedTemporaryFile(delete=False, mode='a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([name, email, phone, city, dob])

    response = {
        "fulfillmentText": "Thank You for the registration. Our team will get in touch with you soon."
    }

    print("Response sent:", response)

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

