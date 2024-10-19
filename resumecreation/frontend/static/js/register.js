import {CONFIG} from "./config.js";  // 导入配置

// Ensure the script runs only after DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Get the form element
    const form = document.querySelector('form');

    // Attach event listener for form submission
    form.addEventListener('submit', async function (event) {
        // Prevent default form submission (page refresh)
        event.preventDefault();

        // Get the form input values
        const firstName = document.getElementById('inputFirstName').value.trim();
        const lastName = document.getElementById('inputLastName').value.trim();
        const email = document.getElementById('inputEmail').value.trim();
        const password = document.getElementById('inputPassword').value.trim();
        const confirmPassword = document.getElementById('inputPasswordConfirm').value.trim();

        // Basic validation checks
        if (!firstName || !lastName || !email || !password || !confirmPassword) {
            alert('All fields are required.');
            return;
        }

        if (password !== confirmPassword) {
            alert('Passwords do not match.');
            return;
        }

        // Construct the request payload (assuming JSON format)
        const payload = {
            firstName: firstName,
            lastName: lastName,
            fullName: `${firstName}_${lastName}`, // 合并 firstName 和 lastName
            username: email,
            email: email,
            password: password
        };

        try {
            // Call the backend API to register the user
            const response = await fetch(`${CONFIG.API_URL}/api/register/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });

            // Handle the response
            if (response.ok) {
                const result = await response.json();

                // If the registration is successful, redirect to the login page
                if (result.success) {
                    alert('Registration successful! Redirecting to login page...');
                    window.location.href = 'login.html';
                } else {
                    alert(result.message || 'Registration failed.');
                }
            } else {
                const result = await response.json();
                // If response is not okay, handle errors
                alert(result.error || 'Error occurred while registering. Please try again.');
            }
        } catch (error) {
            // Catch network or other unexpected errors
            console.error('Error during registration:', error);
            alert('An error occurred. Please try again later.');
        }
    });
});