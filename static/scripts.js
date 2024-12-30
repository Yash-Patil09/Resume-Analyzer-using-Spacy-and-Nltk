document.getElementById('resumeForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const fileInput = document.getElementById('resume');
    const statusDiv = document.getElementById('status');

    // Check if a file is selected
    if (fileInput.files.length === 0) {
        statusDiv.innerHTML = '<p style="color: red;">Please select a file to upload.</p>';
        return;
    }

    // Clear previous messages
    statusDiv.innerHTML = '<p>Uploading...</p>';

    // Create FormData for the file
    const formData = new FormData();
    formData.append('resume', fileInput.files[0]);

    // Fetch request to Flask backend
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            statusDiv.innerHTML = `<p style="color: red;">Error: ${data.error}</p>`;
        } else {
            window.location.href = '/result'; // Redirect to the result page
        }
    })
    .catch(error => {
        console.error('Error:', error);
        statusDiv.innerHTML = '<p style="color: red;">An error occurred while uploading the resume.</p>';
    });
});
