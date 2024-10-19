
# ResumeCreation

> A web-based resume creation platform that helps users build and download professional resumes with ease.

![License](https://img.shields.io/badge/License-MIT-blue.svg) ![Version](https://img.shields.io/badge/Version-1.0-green.svg)

## Table of Contents

- [ResumeCreation](#resumecreation)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Demo](#demo)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Technologies Used](#technologies-used)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Project Overview

**ResumeCreation** is a web application that allows users to quickly generate and download personalized resumes in PDF format. Users can select different templates, customize sections, and store resumes for future edits.

## Features

- 🎨 **Multiple Templates**: Choose from a variety of professionally designed resume templates.
- 📄 **Download as PDF**: Download resumes in PDF format with a single click.
- ☁️ **Cloud Storage**: Store your resumes online for future editing and updates.
- 🔒 **Privacy Protection**: All data is securely stored and accessible only to the user.
- 💻 **Responsive Design**: Works on both desktop and mobile devices.

## Demo

A live demo of the project can be accessed [here](#).

_Screenshot of the platform:_

![Screenshot](path_to_screenshot.png)

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone git@github.sydney.edu.au:haff0939/ResumeCreation.git
   cd ResumeCreation
   ```

2. **Install dependencies:**

   Ensure you have Python and `pip` installed. Then run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MySQL database:**

   - Create a MySQL database named `resume_creation`.
   - Update the `DATABASES` configuration in `settings.py` to match your local MySQL setup:
   
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'resume_creation',
           'USER': 'your_mysql_username',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

4. **Apply migrations:**

   Run the following command to apply the Django migrations:

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**

   Start the server and access the app at `http://127.0.0.1:8000/`:

   ```bash
   python manage.py runserver
   ```

## Usage

1. **Create a New Resume**:  
   Click on "Create Resume" to start building your resume. You can choose from various templates and customize sections like work experience, education, skills, and more.

2. **Save and Edit**:  
   You can save your resume online and come back later to edit and download it as a PDF.

3. **Download PDF**:  
   Once satisfied, download your resume as a PDF file.

## Technologies Used

- **Frontend**: HTML, CSS, Bootstrap 5, JavaScript
- **Backend**: Django (Python)
- **Database**: MySQL
- **PDF Generation**: `WeasyPrint`
- **Authentication**: Django's built-in authentication system

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or issues, feel free to contact:

- **Harry Xu**  
  Email: haff0939@uni.sydney.edu.au

---

Thank you for using **ResumeCreation**! We hope it helps you create the perfect resume. 🌟
