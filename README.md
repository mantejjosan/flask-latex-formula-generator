# Mini Project: LaTeX Formula Generator

This repository contains a simple **Flask** web application that generates LaTeX formulas. The front end is styled using **Tailwind CSS**, and the app allows you to create and view LaTeX formulas through a user-friendly interface.

## Tech Stack

- **Flask** (Python web framework)
- **Tailwind CSS** (for responsive, utility-first styling)
  
## Prerequisites

Ensure you have the following installed:
- **Python 3.7+**
- **Pip** (Python package installer)

## Installation Instructions

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/mantejjosan/flask-latex-formula-generator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flask-latex-formula-generator
   ```

3. Create and activate a virtual environment (if not already done):

   For **Linux/macOS**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   For **Windows**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. Install the required dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Flask App Locally

To run the Flask app locally on your machine, use the following command:

```bash
flask run
```

This will start the application on your local server at `http://127.0.0.1:5000`.

## Hosting the Flask App on a Public IP

If you want to host the Flask app on a public IP (accessible from other devices), you can use the following command:

```bash
flask run --host=0.0.0.0
```

This will make the app accessible from any device in your local network at `http://<your_public_ip>:5000`.

## Warning

**Security Notice:**
This Flask application is **not secure for production use**. It is intended for development purposes only. The default Flask development server is not suitable for handling production-level traffic and is susceptible to security vulnerabilities, including but not limited to:

- Lack of HTTPS
- Open ports accessible from external networks
- Susceptibility to various attacks such as cross-site scripting (XSS) and cross-site request forgery (CSRF)

If you plan to deploy this app publicly, make sure to:
- Use a production-ready web server such as **Gunicorn** or **uWSGI**
- Configure **SSL/TLS** encryption
- Set up a firewall and other security measures

**Proceed at your own risk.**

## Contributing

We welcome contributions! If you have any suggestions, ideas, or improvements for this project, feel free to contribute in the following ways:

1. **Suggest a solution for obtaining free API keys**: If you know of any free or affordable API key sources that can help with this project, feel free to share your thoughts or submit a pull request.

2. **Propose a lightweight local AI alternative**: If you have any recommendations for lightweight, local AI models that can be used in place of a heavy API or cloud-based solution, please share them with us!

To contribute:
- Fork the repository
- Create a new branch for your feature or fix
- Commit your changes
- Open a pull request

Any help in improving this project is highly appreciated!
