# 🐧 Linux Command Quiz
### *An Interactive Terminal-Style Linux Learning Experience*

A **Flask-based web application** designed to test and improve users' knowledge of fundamental Linux commands. With an **authentic terminal-style interface**, this quiz offers an engaging way for beginners and enthusiasts to practice essential commands in a fun, gamified environment.

---

## 👨‍💻 Created By

- **Matad0r**
- **mlad014**

---

## ✨ Features

- ✅ **Comprehensive Quiz**  
  30 carefully selected multiple-choice questions on Linux basics: file management, permissions, navigation, and system administration.

- ✅ **Terminal-Style Interface**  
  Dark CRT-themed UI with **green monospace text**, **typing animations**, **blinking cursor**, and subtle **glitch effects** for a hacker-like experience.

- ✅ **Gamified Learning (Achievement Badges)**  
  - 🏆 **Linux Guru** – Perfect score (30/30)  
  - ⚡ **Power User** – Solid performance (15–25 points)  
  - 🌱 **Beginner** – Starting your Linux journey (<10 points)

- ✅ **Leaderboard & User Tracking**  
  Scores saved and ranked to encourage competitive learning.

- ✅ **Performance Analysis**  
  Detailed breakdown of correct and incorrect answers at the end of the quiz.

- ✅ **Admin Dashboard**  
  Secure panel to manage questions, users, and badges.

- ✅ **Responsive Design**  
  Works seamlessly on **desktop, tablet, and mobile** devices.

- ✅ **Social Sharing**  
  Share quiz results and badges directly on social media.

---

## 🚀 Setup & Installation

1. **Install dependencies**  
   ```bash
   pip install flask
   ```

2. **Run the application**  
   ```bash
   python app.py
   ```

3. **Access the quiz**  
   Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

---

## 🔑 Admin Access

Access the admin panel at:
```
/admin/login
```

**Default Credentials**
- Username: `admin`
- Password: `linuxquiz123`

The admin panel provides the following capabilities:

- **Dashboard**: View statistics about quiz usage and performance
- **Question Management**: Add, edit, or delete quiz questions
- **User Management**: View and manage user records with filtering options
- **Badge Management**: Customize badges, criteria, and appearance

---

## 🔐 Tech Stack

- **Backend**: [Flask](https://flask.palletsprojects.com/) (Python)  
- **Frontend**: HTML, CSS, JavaScript (Terminal-inspired theme)  
- **Data Storage**: JSON files for questions and user scores  
- **Authentication**: Session-based admin login  
- **Responsive UI**: CSS media queries

---

## 📂 Project Structure

```
Linux-Command-Quiz/
├── app.py           # Main Flask application with routes & logic
├── scores.json      # User scores & leaderboard data
├── templates/       # HTML templates
│   ├── index.html    # Welcome page
│   ├── quiz.html     # Quiz interface
│   ├── result.html   # Results & badges
│   └── admin_*.html  # Admin panel templates
└── static/         # CSS, JS, and images (terminal effects)
```

---

## 🌟 Future Enhancements

- Database integration (MySQL/PostgreSQL) for better scalability
- User authentication system
- More question categories & difficulty levels
- Timed quiz mode with countdown
- Expanded badges & achievements system

---

## 📸 Screenshots

- Terminal-Style Quiz Interface
- Result Page with Badges
- Admin Dashboard

*(Add screenshots here when available)*

---

Happy Learning & Keep Hacking the Terminal! 🐧💻
