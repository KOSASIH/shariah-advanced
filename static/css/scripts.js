// scripts.js

// Ensure that the DOM is fully loaded before running scripts
document.addEventListener("DOMContentLoaded", function() {

    // Form validation
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        // Fetch form elements
        const smartContractName = document.getElementById('smart_contract_name');
        const smartContractVersion = document.getElementById('smart_contract_version');

        // Simple validation checks
        if (smartContractName.value.trim() === "") {
            alert("Please select a smart contract.");
            smartContractName.focus();
            event.preventDefault();
            return false;
        }
        if (smartContractVersion.value.trim() === "") {
            alert("Please enter a version.");
            smartContractVersion.focus();
            event.preventDefault();
            return false;
        }

        // If everything is okay, allow form submission
        return true;
    });

    // Optional: Enhance user experience by showing a loading spinner or message during form submission
    form.addEventListener('submit', function(event) {
        const submitButton = form.querySelector('button[type="submit"]');
        submitButton.disabled = true;
        submitButton.innerHTML = 'Checking...';
    });

    // Optional: Add functionality to dynamically load and display the contents of the selected smart contract file
    const smartContractSelect = document.getElementById('smart_contract_name');
    smartContractSelect.addEventListener('change', function() {
        const selectedFile = smartContractSelect.value;
        if (selectedFile) {
            fetch(`/contracts/${selectedFile}`)
                .then(response => response.text())
                .then(data => {
                    // Display the smart contract content or a snippet if necessary
                    const contractContentDiv = document.getElementById('contractContent');
                    if (contractContentDiv) {
                        contractContentDiv.textContent = data;
                    }
                })
                .catch(error => console.error('Error fetching smart contract content:', error));
        }
    });

});
