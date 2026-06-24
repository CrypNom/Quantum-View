# QuantumView

A modern Flask-powered web dashboard built with HTML, CSS, JavaScript, and Python.

## Features

- Clean modern UI
- Multi-page dashboard navigation
- Flask backend integration
- URL input system
- Duration and target count configuration
- Real-time frontend to backend communication using Fetch API
- Responsive design

## Tech Stack

- HTML5
- CSS3
- JavaScript
- Python
- Flask

## Project Structure

```text
QuantumView/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/CrypNom/Quantum-View.git
cd Quantum-View
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Deployment

### Render

Build Command:

```bash
pip install -r requirements.txt
```

Start Command:

```bash
gunicorn app:app
```

### Requirements

```text
flask
gunicorn
```

## Screenshots

Add screenshots of your dashboard here.

## Author

Prem Sharma

GitHub: https://github.com/CrypNom

## License

This project is licensed under the MIT License.
