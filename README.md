# Password-Strength-Analyzes-Project
Project- Password analyzer with strong password suggestions and downloadable custom wordlists.

# Password Strength Analyzer & Custom Wordlist Generator

## Overview

A Flask-based Python tool that evaluates password strength and generates custom wordlists. It provides actionable feedback, suggests stronger passwords, and allows users to download tailored wordlists for cybersecurity testing or educational purposes.

---

## Features

- **Password Strength Analysis:** Uses `zxcvbn` to analyze password length, complexity, and entropy.
- **Password Suggestions:** Automatically suggests strong, random passwords for weak entries.
- **Custom Wordlist Generator:** Generates personalized wordlists using user-provided data (e.g., names, dates, pet names).
- **Downloadable Wordlists:** Save wordlists in `.txt` format for penetration testing.
- **Web Interface:** Built with Flask, styled with CSS, and easy to use.

---

## Technologies Used

- **Backend:** Python 3.x, Flask
- **Frontend:** HTML, CSS
- **Password Analysis:** zxcvbn library
- **Development Tools:** VS Code, Git, GitHub

---

## Project Structure

```
password_analyzer/
├── app.py
├── analyzer.py
├── wordlist_gen.py
├── utils.py
├── templates/
│   ├── index.html
│   └── about.html
├── static/
│   └── style.css
├── wordlists/
│   └── web_wordlist.txt
└── requirements.txt
```

---

## Installation

```bash
pip install -r requirements.txt
python app.py
```

Then, open: `http://127.0.0.1:5000/`

---

## How to Use

1. **Enter a password** to analyze its strength.
2. **Review feedback** and view estimated crack times.
3. **Get strong password suggestions** for weak inputs.
4. **Provide custom inputs** (e.g., "anushka 0410 cat") to generate a tailored wordlist.
5. **Download the generated wordlist** for testing or research.
