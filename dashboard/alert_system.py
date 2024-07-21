from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def send_alert():
    data = request.get_json()
    # Send alert to users or administrators
    return jsonify({'message': 'Alert sent successfully'})
