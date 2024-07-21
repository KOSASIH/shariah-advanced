from flask import Flask, request, jsonify
from shariah_compliance_model import ShariahComplianceModel

app = Flask(__name__)

model = ShariahComplianceModel()

@app.route('/compliance', methods=['POST'])
def check_compliance():
    data = request.get_json()
    prediction = model.predict(data)
    return jsonify({'compliance': prediction})

if __name__ == '__main__':
    app.run(debug=True)
