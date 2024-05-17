
### `README.md`

```markdown
# Shariah Compliance Checker

This project is an initiative to help Muslims who are looking for AI-based audits of smart contracts to ensure their compliance with Shariah principles. It leverages the OpenAI GPT-4 model and Llama3 via Ollama to evaluate Solidity smart contracts for compliance. The examples provided are generated using the GPT-4 model and are for educational purposes only. They have not been tested or approved by Shariah committees.

## Features

- Upload and evaluate Solidity smart contracts for Shariah compliance.
- Process Solidity examples one by one and perform a full audit.
- Choose between different AI models (GPT-3, GPT-4, Llama3).
- View and download audit results.
- User-friendly web interface with navigation and file management.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Flask
- OpenAI API key
- Ollama API key (for Llama3)

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/shariah-compliance-checker.git
   cd shariah-compliance-checker
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Create a `.env` file:**

   Copy the contents of `.env.sample` to a new file named `.env` and populate it with your API keys and other settings.

5. **Run the application:**

   ```sh
   python app.py
   ```

6. **Access the web interface:**

   Open your web browser and navigate to `http://127.0.0.1:5000`.

### Directory Structure

```
shariah-compliance-checker/
│
├── app.py
├── requirements.txt
├── config.json
├── criteria.txt
├── contracts/
│   └── (Uploaded Solidity files)
├── solidityExamples/
│   └── (Example Solidity files for checking)
├── output/
│   └── (Output audit files)
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── scripts.js
├── templates/
│   ├── index.html
│   ├── upload.html
│   ├── solidity_examples.html
│   ├── solidity_results.html
│   └── result.html
└── .env.sample
```

### Usage

1. **Upload Smart Contracts:**

   Use the web interface to upload Solidity smart contract files for compliance checking.

2. **Check Compliance:**

   Select a smart contract and check its compliance with Shariah principles using the chosen AI model.

3. **Process Solidity Examples:**

   Use the "Process Solidity Examples" feature to evaluate pre-defined Solidity examples one by one.

4. **View and Download Results:**

   View the results of the compliance checks and download the audit files for further review.

### Configuration

You can configure the AI model used for evaluation by modifying the `config.json` file:

```json
{
  "model": "gpt-4"  // Options: "gpt-3", "gpt-4", "llama3"
}
```

### Disclaimer

- The examples provided are generated using the GPT-4 model and are for educational purposes only.
- These examples have not been tested or approved by any Shariah committees.
- This project is intended to serve as an initiative for public contribution and to help Muslims seeking AI-based audit solutions.
- Users are advised to consult qualified Shariah scholars or committees to verify the compliance of their smart contracts.
- The authors and contributors of this project do not hold any responsibility for the misuse or misinterpretation of the provided examples or audit results.

### Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgements

Designed by Dr. Mohammed Al-Jefairi.
```
