import openai
import os
from flask import Flask, request, render_template, send_from_directory, jsonify

# Set your OpenAI API key
openai.api_key = 'your-openai-api-key'

app = Flask(__name__)

# Load criteria from criteria.txt
with open('criteria.txt', 'r') as file:
    criteria = file.read()

def evaluate_smart_contract(smart_contract_name, smart_contract_version, smart_contract_content):
    prompt = f"""
    Evaluate the following smart contract for Shariah compliance based on the criteria provided:
    {criteria}

    Smart Contract:
    {smart_contract_content}

    Provide a detailed evaluation and conclude if the contract is Shariah compliant or not.
    """
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=6000,
        temperature=0.7,
    )
    evaluation = response.choices[0].text.strip()

    # Save the result to /audit/{smart_contract_name}+{smart_contract_version}.txt
    audit_filename = f"{smart_contract_name}+{smart_contract_version}.txt"
    audit_path = os.path.join('audit', audit_filename)
    with open(audit_path, 'w') as audit_file:
        audit_file.write(evaluation)
    
    return evaluation, audit_filename

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_shariah_compliance():
    try:
        smart_contract_name = request.form['smart_contract_name']
        smart_contract_version = request.form['smart_contract_version']
        smart_contract_path = os.path.join('contracts', f"{smart_contract_name}.sol")
        
        if not os.path.exists(smart_contract_path):
            return jsonify({"error": f"The smart contract file {smart_contract_name}.sol does not exist."}), 404
        
        with open(smart_contract_path, 'r') as file:
            smart_contract_content = file.read()
        
        result, audit_filename = evaluate_smart_contract(smart_contract_name, smart_contract_version, smart_contract_content)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    return jsonify({"result": result, "audit_filename": audit_filename})

@app.route('/audit/<filename>')
def download_audit(filename):
    return send_from_directory('audit', filename)

if __name__ == '__main__':
    if not os.path.exists('audit'):
        os.makedirs('audit')
    app.run(debug=True)
