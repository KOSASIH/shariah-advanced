import openai
import os
import json
from flask import Flask, request, render_template, send_from_directory, redirect, url_for, flash
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set your API keys securely
openai.api_key = os.getenv('OPENAI_API_KEY')
ollama_api_key = os.getenv('OLLAMA_API_KEY')

# Constants
UPLOAD_FOLDER = 'contracts'
SOLIDITY_FOLDER = 'solidityExamples'
OUTPUT_FOLDER = 'output'
ALLOWED_EXTENSIONS = {'sol'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max file size

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
app.secret_key = os.getenv('SECRET_KEY')  # Ensure you set this in your .env file

# Load criteria from criteria.txt
with open('criteria.txt', 'r') as file:
    criteria = file.read()

# Load model configuration from config.json
with open('config.json', 'r') as file:
    config = json.load(file)
model_choice = config.get('model', 'gpt-4')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def evaluate_smart_contract(smart_contract_name, smart_contract_version, smart_contract_content):
    if model_choice in ['gpt-3', 'gpt-4']:
        prompt = f"""
        Evaluate the following smart contract for Shariah compliance based on the criteria provided:
        {criteria}

        Smart Contract:
        {smart_contract_content}

        Provide a detailed evaluation and conclude if the contract is Shariah compliant or not.
        """
        response = openai.Completion.create(
            model=model_choice,
            prompt=prompt,
            max_tokens=6000,
            temperature=0.7,
        )
        evaluation = response.choices[0].text.strip()
    elif model_choice == 'llama3':
        # Implement Llama3 (Ollama) API call here
        # Placeholder for Llama3 API integration
        evaluation = "Llama3 evaluation not implemented yet."
    
    # Save the result to /audit/{smart_contract_name}+{smart_contract_version}.txt
    audit_filename = secure_filename(f"{smart_contract_name}+{smart_contract_version}.txt")
    audit_path = os.path.join('audit', audit_filename)
    with open(audit_path, 'w') as audit_file:
        audit_file.write(evaluation)
    
    return evaluation, audit_filename

@app.route('/')
def home():
    contract_files = os.listdir(app.config['UPLOAD_FOLDER'])
    contract_files = [f for f in contract_files if allowed_file(f)]
    return render_template('index.html', contract_files=contract_files)

@app.route('/check', methods=['POST'])
def check_shariah_compliance():
    smart_contract_name = request.form['smart_contract_name']
    smart_contract_version = request.form['smart_contract_version']
    smart_contract_path = os.path.join(app.config['UPLOAD_FOLDER'], smart_contract_name)
    
    if not os.path.exists(smart_contract_path):
        flash(f"Error: The smart contract file {smart_contract_name} does not exist.")
        return redirect(url_for('home'))
    
    with open(smart_contract_path, 'r') as file:
        smart_contract_content = file.read()
    
    try:
        result, audit_filename = evaluate_smart_contract(smart_contract_name, smart_contract_version, smart_contract_content)
    except Exception as e:
        flash(f"An error occurred: {str(e)}")
        return redirect(url_for('home'))
    
    return redirect(url_for('result', result=result, audit_filename=audit_filename))

@app.route('/result')
def result():
    result = request.args.get('result', '')
    audit_filename = request.args.get('audit_filename', '')
    return render_template('result.html', result=result, audit_filename=audit_filename)

@app.route('/audit/<filename>')
def download_audit(filename):
    return send_from_directory('audit', filename)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            return redirect(url_for('home'))
        else:
            flash('Allowed file types are .sol')
            return redirect(request.url)
    
    return render_template('upload.html')

@app.route('/solidity_examples', methods=['GET', 'POST'])
def solidity_examples():
    if request.method == 'POST':
        # Process Solidity examples
        solidity_files = os.listdir(SOLIDITY_FOLDER)
        results = []
        for filename in solidity_files:
            if allowed_file(filename):
                with open(os.path.join(SOLIDITY_FOLDER, filename), 'r') as file:
                    smart_contract_content = file.read()
                result, _ = evaluate_smart_contract(filename, '1.0', smart_contract_content)
                output_filename = f"{filename.split('.')[0]}_output.txt"
                with open(os.path.join(OUTPUT_FOLDER, output_filename), 'w') as output_file:
                    output_file.write(result)
                results.append((filename, output_filename))
        flash('Solidity examples processed successfully')
        return render_template('solidity_results.html', results=results)
    return render_template('solidity_examples.html')

@app.route('/update_model', methods=['POST'])
def update_model():
    data = request.get_json()
    model = data.get('model', 'gpt-4')
    config['model'] = model
    with open('config.json', 'w') as file:
        json.dump(config, file)
    return {'status': 'success', 'model': model}

if __name__ == '__main__':
    if not os.path.exists('audit'):
        os.makedirs('audit')
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    if not os.path.exists(SOLIDITY_FOLDER):
        os.makedirs(SOLIDITY_FOLDER)
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    app.run(debug=True)
