# Linux Command Quiz

A Flask web application that tests users' knowledge of basic Linux commands with a terminal-style interface. This interactive quiz helps users learn and test their understanding of essential Linux terminal commands in an engaging way.

## Created By

- Matad0r
- mlad014

## Features

- **Comprehensive Quiz**: 30 carefully selected multiple-choice questions covering basic Linux commands, file management, and system administration
- **Terminal-Style Interface**: Authentic terminal look with dark theme, green text, monospace font, and CRT screen effects
- **Interactive Animations**: Typing animations, blinking cursor, and glitch effects for an immersive experience
- **User Tracking System**: Records user scores and displays them on a leaderboard
- **Achievement Badges**: Three different badges awarded based on performance:
  - "Linux Guru" badge for perfect scores (30/30)
  - "Power User" badge for good performance (15-25 points)
  - "Beginner" badge for those starting their Linux journey (<10 points)
- **Performance Analysis**: Detailed breakdown of correct and incorrect answers
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Admin Dashboard**: Complete management system for questions, users, and badges
- **Social Sharing**: Share results on social media platforms

## Setup

1. Install dependencies:
   ```
   pip install flask
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Access the quiz:
   ```
   http://127.0.0.1:5000/
   ```

## Admin Access

Access the admin panel at `/admin/login` with:
- Username: `admin`
- Password: `linuxquiz123`

The admin panel provides the following capabilities:

- **Dashboard**: View statistics about quiz usage and performance
- **Question Management**: Add, edit, or delete quiz questions
- **User Management**: View and manage user records with filtering options
- **Badge Management**: Customize badges, criteria, and appearance

## Technical Implementation

- **Backend**: Python Flask framework for routing and server-side logic
- **Data Storage**: JSON file storage for questions and user scores
- **Frontend**: HTML, CSS, and JavaScript with terminal-inspired design
- **Authentication**: Simple session-based admin authentication
- **Responsive Design**: CSS media queries for mobile compatibility

## Project Structure

- `app.py`: Main application file with routes and quiz logic
- `templates/`: HTML templates for all pages
  - `index.html`: Welcome page
  - `quiz.html`: Quiz questions interface
  - `result.html`: Results and badge display
  - `admin_*.html`: Admin panel interfaces
- `scores.json`: User score data storage

## Future Enhancements

- Database integration for better data management
- User authentication system
- More question categories and difficulty levels
- Timed quiz mode with countdown timer
- Expanded badge and achievement system

## Screenshots

- Quiz interface with terminal-style theme
- Results page with badges
- Admin dashboard for managing content