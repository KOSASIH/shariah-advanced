# Shariah Compliance Checker

Shariah Compliance Checker is a web application designed to evaluate the Shariah compliance of smart contracts. This tool uses OpenAI's GPT-4 model to analyze smart contracts against a set of predefined Shariah criteria. 

## Features
- Upload and select smart contract files for evaluation.
- Check smart contracts for compliance with Shariah principles.
- Download detailed audit reports of the evaluation.
- User-friendly interface designed with Bootstrap.

## Getting Started

### Prerequisites
- Python 3.6+
- An OpenAI API key

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/shariah-compliance-checker.git
   cd shariah-compliance-checker
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory of the project:
     ```sh
     touch .env
     ```

   - Add your OpenAI API key and Flask secret key to the `.env` file:
     ```env
     OPENAI_API_KEY=your-openai-api-key
     SECRET_KEY=your-secret-key
     ```

5. Ensure the necessary directories exist:
   ```sh
   mkdir -p contracts audit
   ```

6. Place your Shariah compliance criteria in a file named `criteria.txt` in the root directory.

### Usage

1. Run the Flask application:
   ```sh
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Use the interface to upload smart contract files, check their compliance, and download audit reports.

### Project Structure

```
/shariah-compliance-checker
    /templates
        index.html
        result.html
        upload.html
    /static
        /css
            styles.css
        /js
            scripts.js
    /contracts
        example.sol
    /audit
    app.py
    criteria.txt
    .env
    requirements.txt
    README.md
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Designed by Dr. Mohammed Al-Jefairi
```

### LICENSE

```plaintext
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
