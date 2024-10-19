import { CONFIG } from "./config.js";  // 导入配置

// Ensure the script runs only after DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Get the form element
    const form = document.querySelector('form');


    // Attach event listener for form submission
    form.addEventListener('submit', async function (event) {
        // Prevent default form submission (page refresh)
        event.preventDefault();

        // Get the form input values
        const email = document.getElementById('inputEmail').value.trim();
        const password = document.getElementById('inputPassword').value.trim();

        // Basic validation checks
        if (!email || !password) {
            alert('Both fields are required.');
            return;
        }

        // Construct the request payload
        const payload = {
            username: email,
            password: password
        };

        try {
            // Call the backend API to log in the user
            const response = await fetch(`${CONFIG.API_URL}/api/login/`, { // 更新为实际的登录 API URL
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });

            // Handle the response
            if (response.ok) {
                const result = await response.json();

                // Check if the token is present
                if (result.access) {
                    alert('Login successful! Redirecting...');
                    // Store the token for future requests
                    localStorage.setItem('token', result.access);
                    // Redirect to the home page or any other page
                    window.location.href = 'index.html';
                } else {
                    alert(result.message || 'Login failed.');
                }
            } else {
                // Handle error responses
                alert('Error occurred while logging in. Please try again.');
            }
        } catch (error) {
            // Catch network or other unexpected errors
            console.error('Error during login:', error);
            alert('An error occurred. Please try again later.');
        }
    });
});
