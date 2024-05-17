document.addEventListener('DOMContentLoaded', (event) => {
    // Function to update the selected model
    const updateModel = (model) => {
        fetch('/update_model', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ model: model }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    };

    // Handle model selection change
    const modelChoice = document.getElementById('model_choice');
    if (modelChoice) {
        modelChoice.addEventListener('change', (event) => {
            const selectedModel = event.target.value;
            updateModel(selectedModel);
        });
    }

    // Handle form submissions
    const handleFormSubmit = (formId, successMessage, errorMessage) => {
        const form = document.getElementById(formId);
        if (form) {
            form.addEventListener('submit', (event) => {
                event.preventDefault();
                const formData = new FormData(form);
                fetch(form.action, {
                    method: form.method,
                    body: formData,
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        alert(successMessage);
                        window.location.reload();
                    } else {
                        alert(errorMessage);
                    }
                })
                .catch((error) => {
                    console.error('Error:', error);
                    alert(errorMessage);
                });
            });
        }
    };

    // Handle file uploads
    const uploadForm = document.getElementById('uploadForm');
    if (uploadForm) {
        uploadForm.addEventListener('submit', (event) => {
            event.preventDefault();
            const formData = new FormData(uploadForm);
            fetch('/upload', {
                method: 'POST',
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    alert('File successfully uploaded');
                    window.location.reload();
                } else {
                    alert('File upload failed');
                }
            })
            .catch((error) => {
                console.error('Error:', error);
                alert('File upload failed');
            });
        });
    }

    // Handle processing of Solidity examples
    const solidityExamplesForm = document.getElementById('solidityExamplesForm');
    if (solidityExamplesForm) {
        solidityExamplesForm.addEventListener('submit', (event) => {
            event.preventDefault();
            fetch('/solidity_examples', {
                method: 'POST',
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    alert('Solidity examples processed successfully');
                    window.location.href = '/solidity_examples';
                } else {
                    alert('Processing Solidity examples failed');
                }
            })
            .catch((error) => {
                console.error('Error:', error);
                alert('Processing Solidity examples failed');
            });
        });
    }
});
