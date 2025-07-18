from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
import os
import datetime
from functools import wraps

app = Flask(__name__)
app.secret_key = 'linux_quiz_secret_key'  # Change this to a secure random key in production

# Admin credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'linuxquiz123'  # Change this to a secure password in production

# Admin authentication decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_logged_in' not in session:
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

# Linux quiz questions
questions = [
    {
        "question": "Which command is used to list files in a directory?",
        "options": ["dir", "ls", "list", "show"],
        "answer": "ls"
    },
    {
        "question": "Which command is used to change file permissions?",
        "options": ["chmod", "chperm", "perm", "attrib"],
        "answer": "chmod"
    },
    {
        "question": "Which command displays the current working directory?",
        "options": ["pwd", "cd", "cwd", "path"],
        "answer": "pwd"
    },
    {
        "question": "Which command is used to create a new directory?",
        "options": ["md", "mkdir", "makedir", "create"],
        "answer": "mkdir"
    },
    {
        "question": "Which command is used to remove a file?",
        "options": ["rm", "del", "remove", "erase"],
        "answer": "rm"
    },
    {
        "question": "Which command is used to display the contents of a file?",
        "options": ["cat", "show", "display", "type"],
        "answer": "cat"
    },
    {
        "question": "Which command is used to find a file in the filesystem?",
        "options": ["search", "find", "lookup", "where"],
        "answer": "find"
    },
    {
        "question": "Which command is used to check network connectivity?",
        "options": ["ping", "connect", "network", "check"],
        "answer": "ping"
    },
    {
        "question": "Which command is used to display system processes?",
        "options": ["ps", "proc", "process", "tasks"],
        "answer": "ps"
    },
    {
        "question": "Which command is used to change ownership of a file?",
        "options": ["chown", "owner", "setowner", "chmod"],
        "answer": "chown"
    },
    {
        "question": "Which command is used to display disk usage?",
        "options": ["du", "disk", "space", "usage"],
        "answer": "du"
    },
    {
        "question": "Which command is used to display free disk space?",
        "options": ["df", "free", "space", "avail"],
        "answer": "df"
    },
    {
        "question": "Which command is used to search for text in files?",
        "options": ["grep", "find", "search", "lookup"],
        "answer": "grep"
    },
    {
        "question": "Which command is used to display the manual for a command?",
        "options": ["man", "help", "manual", "info"],
        "answer": "man"
    },
    {
        "question": "Which command is used to compress files?",
        "options": ["zip", "compress", "tar", "gzip"],
        "answer": "gzip"
    },
    {
        "question": "Which command is used to extract tar archives?",
        "options": ["untar", "extract", "tar -x", "unzip"],
        "answer": "tar -x"
    },
    {
        "question": "Which command is used to display system information?",
        "options": ["uname", "sysinfo", "system", "info"],
        "answer": "uname"
    },
    {
        "question": "Which command is used to display the last few lines of a file?",
        "options": ["tail", "end", "last", "bottom"],
        "answer": "tail"
    },
    {
        "question": "Which command is used to display the first few lines of a file?",
        "options": ["head", "start", "first", "top"],
        "answer": "head"
    },
    {
        "question": "Which command is used to sort lines in a file?",
        "options": ["sort", "order", "arrange", "line"],
        "answer": "sort"
    },
    {
        "question": "Which command is used to count lines, words, and characters in a file?",
        "options": ["wc", "count", "wordcount", "lines"],
        "answer": "wc"
    },
    {
        "question": "Which command is used to display the current user?",
        "options": ["whoami", "user", "me", "currentuser"],
        "answer": "whoami"
    },
    {
        "question": "Which command is used to change the current directory?",
        "options": ["cd", "chdir", "goto", "move"],
        "answer": "cd"
    },
    {
        "question": "Which command is used to display network interfaces?",
        "options": ["ifconfig", "netstat", "network", "interfaces"],
        "answer": "ifconfig"
    },
    {
        "question": "Which command is used to display running processes?",
        "options": ["top", "ps", "proc", "tasks"],
        "answer": "top"
    },
    {
        "question": "Which command is used to kill a process?",
        "options": ["kill", "end", "terminate", "stop"],
        "answer": "kill"
    },
    {
        "question": "Which command is used to create a symbolic link?",
        "options": ["ln -s", "link", "symlink", "mklink"],
        "answer": "ln -s"
    },
    {
        "question": "Which command is used to display the calendar?",
        "options": ["cal", "calendar", "date", "time"],
        "answer": "cal"
    },
    {
        "question": "Which command is used to display the current date and time?",
        "options": ["date", "time", "now", "datetime"],
        "answer": "date"
    },
    {
        "question": "Which command is used to display disk partitions?",
        "options": ["fdisk -l", "partitions", "disks", "mount"],
        "answer": "fdisk -l"
    }
]

@app.route('/')
def index():
    # Get leaderboard data for the home page
    scores_file = 'scores.json'
    leaderboard = []
    
    if os.path.exists(scores_file):
        try:
            with open(scores_file, 'r') as f:
                scores = json.load(f)
                # Get top 5 scores for leaderboard
                leaderboard = sorted(scores, key=lambda x: x['score'], reverse=True)[:5]
        except json.JSONDecodeError:
            leaderboard = []
    
    return render_template('index.html', leaderboard=leaderboard)

@app.route('/progression')
def progression():
    # Get scores data for the progression page
    scores_file = 'scores.json'
    scores = []
    total_score = 0
    basic_score = 0
    file_score = 0
    system_score = 0
    
    if os.path.exists(scores_file):
        try:
            with open(scores_file, 'r') as f:
                scores = json.load(f)
                # Calculate total scores across all users
                for score in scores:
                    total_score += score['score']
                    
                # Estimate category scores based on total
                if scores:
                    avg_score = total_score / len(scores)
                    basic_score = int(avg_score * 10)  # Estimate for basic commands
                    file_score = int(avg_score * 10)   # Estimate for file management
                    system_score = int(avg_score * 10) # Estimate for system admin
        except json.JSONDecodeError:
            pass
    
    return render_template('progression.html', 
                           total_score=total_score,
                           basic_score=basic_score,
                           file_score=file_score,
                           system_score=system_score)

@app.route('/leaderboard')
def leaderboard():
    # Get all scores for the leaderboard page
    scores_file = 'scores.json'
    all_scores = []
    
    if os.path.exists(scores_file):
        try:
            with open(scores_file, 'r') as f:
                scores = json.load(f)
                # Sort all scores
                all_scores = sorted(scores, key=lambda x: x['score'], reverse=True)
        except json.JSONDecodeError:
            all_scores = []
    
    return render_template('leaderboard.html', leaderboard=all_scores, total=len(questions))

@app.route('/quiz', methods=['POST'])
def quiz():
    player_name = request.form.get('player_name')
    if not player_name:
        return redirect(url_for('index'))
    return render_template('quiz.html', questions=questions, player_name=player_name)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    player_name = request.form.get('player_name')
    wrong_questions = []
    
    # Category scores
    basic_commands_score = 0
    file_management_score = 0
    system_admin_score = 0
    
    for i in range(len(questions)):
        user_answer = request.form.get(f'q{i}')
        correct_answer = questions[i]['answer']
        
        # Calculate category scores (10 questions per category)
        if user_answer == correct_answer:
            score += 1
            if i < 10:
                basic_commands_score += 1
            elif i < 20:
                file_management_score += 1
            else:
                system_admin_score += 1
        else:
            wrong_questions.append({
                'question': questions[i]['question'],
                'user_answer': user_answer,
                'correct_answer': correct_answer
            })
    
    # Save score to JSON file
    scores_file = 'scores.json'
    scores = []
    
    if os.path.exists(scores_file):
        try:
            with open(scores_file, 'r') as f:
                scores = json.load(f)
        except json.JSONDecodeError:
            scores = []
    
    # Add current date to the score entry
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    scores.append({"name": player_name, "score": score, "date": current_date})
    
    with open(scores_file, 'w') as f:
        json.dump(scores, f)
    
    # Get top 5 scores for leaderboard
    leaderboard = sorted(scores, key=lambda x: x['score'], reverse=True)[:5]
    
    return render_template('result.html', 
                           score=score, 
                           total=len(questions), 
                           leaderboard=leaderboard, 
                           player_name=player_name,
                           wrong_questions=wrong_questions,
                           basic_commands_score=basic_commands_score,
                           file_management_score=file_management_score,
                           system_admin_score=system_admin_score)

# Admin routes
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            error = 'Invalid credentials. Please try again.'
    
    return render_template('admin_login.html', error=error)

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

@app.route('/admin')
@admin_required
def admin_dashboard():
    # Get user data
    scores_file = 'scores.json'
    users = []
    
    if os.path.exists(scores_file):
        try:
            with open(scores_file, 'r') as f:
                users = json.load(f)
                # Add date if not present (for older entries)
                for user in users:
                    if 'date' not in user:
                        user['date'] = 'N/A'
        except json.JSONDecodeError:
            users = []
    
    # Calculate badge statistics
    total_users = len(users)
    linux_guru_count = sum(1 for user in users if user['score'] == len(questions))
    power_user_count = sum(1 for user in users if 15 <= user['score'] <= 25)
    beginner_count = sum(1 for user in users if user['score'] < 10)
    no_badge_count = total_users - linux_guru_count - power_user_count - beginner_count
    
    badge_stats = {
        'linux_guru': linux_guru_count,
        'power_user': power_user_count,
        'beginner': beginner_count,
        'no_badge': no_badge_count,
        'linux_guru_percent': round((linux_guru_count / total_users) * 100) if total_users > 0 else 0,
        'power_user_percent': round((power_user_count / total_users) * 100) if total_users > 0 else 0,
        'beginner_percent': round((beginner_count / total_users) * 100) if total_users > 0 else 0,
        'no_badge_percent': round((no_badge_count / total_users) * 100) if total_users > 0 else 0
    }
    
    # Mock question statistics (in a real app, you would track this data)
    question_stats = []
    for i, q in enumerate(questions):
        # Generate mock statistics
        correct = total_users - (i % 5)  # Just a mock formula
        if correct < 0:
            correct = 0
        incorrect = total_users - correct
        success_rate = round((correct / total_users) * 100) if total_users > 0 else 0
        
        question_stats.append({
            'question': q['question'],
            'correct': correct,
            'incorrect': incorrect,
            'success_rate': success_rate
        })
    
    return render_template('admin_dashboard.html', 
                           questions=questions,
                           users=users,
                           question_stats=question_stats,
                           badge_stats=badge_stats)

@app.route('/admin/questions')
@admin_required
def admin_questions():
    return render_template('admin_questions.html', questions=questions)

@app.route('/admin/users')
@admin_required
def admin_users():
    # Get user data
    scores_file = 'scores.json'
    users = []
    
    if os.path.exists(scores_file):
        try:
            with open(scores_file, 'r') as f:
                users = json.load(f)
                # Add date if not present (for older entries)
                for user in users:
                    if 'date' not in user:
                        user['date'] = 'N/A'
        except json.JSONDecodeError:
            users = []
    
    return render_template('admin_users.html', users=users, questions=questions)

@app.route('/admin/users/delete', methods=['POST'])
@admin_required
def admin_delete_user():
    user_index = int(request.form.get('user_index'))
    
    # Get user data
    scores_file = 'scores.json'
    users = []
    
    if os.path.exists(scores_file):
        try:
            with open(scores_file, 'r') as f:
                users = json.load(f)
                
            # Delete user if index is valid
            if 0 <= user_index < len(users):
                users.pop(user_index)
                
                # Save updated users list
                with open(scores_file, 'w') as f:
                    json.dump(users, f)
        except json.JSONDecodeError:
            pass
    
    return redirect(url_for('admin_users'))

@app.route('/admin/badges')
@admin_required
def admin_badges():
    # Get user data for badge statistics
    scores_file = 'scores.json'
    users = []
    
    if os.path.exists(scores_file):
        try:
            with open(scores_file, 'r') as f:
                users = json.load(f)
        except json.JSONDecodeError:
            users = []
    
    # Calculate badge statistics
    total_users = len(users) if users else 1  # Avoid division by zero
    linux_guru_count = sum(1 for user in users if user['score'] == len(questions))
    power_user_count = sum(1 for user in users if 15 <= user['score'] <= 25)
    beginner_count = sum(1 for user in users if user['score'] < 10)
    no_badge_count = total_users - linux_guru_count - power_user_count - beginner_count
    
    badge_stats = {
        'linux_guru': linux_guru_count,
        'power_user': power_user_count,
        'beginner': beginner_count,
        'no_badge': no_badge_count,
        'linux_guru_percent': round((linux_guru_count / total_users) * 100),
        'power_user_percent': round((power_user_count / total_users) * 100),
        'beginner_percent': round((beginner_count / total_users) * 100),
        'no_badge_percent': round((no_badge_count / total_users) * 100)
    }
    
    return render_template('admin_badges.html', badge_stats=badge_stats)

@app.route('/admin/badges/edit', methods=['POST'])
@admin_required
def admin_edit_badge():
    badge_type = request.form.get('badge_type')
    badge_name = request.form.get('badge_name')
    badge_description = request.form.get('badge_description')
    badge_color = request.form.get('badge_color')
    badge_icon = request.form.get('badge_icon')
    
    # In a real application, you would save these settings to a database
    # For this example, we'll just redirect back to the badges page
    # You could also use Flask's flash messages to show a success message
    
    # Update badge criteria based on type
    if badge_type == 'linux-guru':
        perfect_score = request.form.get('perfect_score')
        # In a real app, you would save this value
    elif badge_type == 'power-user':
        min_score = request.form.get('min_score')
        max_score = request.form.get('max_score')
        # In a real app, you would save these values
    elif badge_type == 'beginner':
        max_beginner_score = request.form.get('max_beginner_score')
        # In a real app, you would save this value
    
    return redirect(url_for('admin_badges'))

@app.route('/admin/questions/add', methods=['POST'])
@admin_required
def admin_add_question():
    question_text = request.form.get('question')
    category = request.form.get('category')
    options = [
        request.form.get('option1'),
        request.form.get('option2'),
        request.form.get('option3'),
        request.form.get('option4')
    ]
    correct_index = int(request.form.get('correct'))
    
    new_question = {
        'question': question_text,
        'options': options,
        'answer': options[correct_index]
    }
    
    # In a real app, you would save this to a database
    # For this example, we'll just add it to the questions list
    questions.append(new_question)
    
    # Save questions to a file (optional)
    # with open('questions.json', 'w') as f:
    #     json.dump(questions, f)
    
    return redirect(url_for('admin_questions'))

@app.route('/admin/questions/edit', methods=['POST'])
@admin_required
def admin_edit_question():
    question_id = int(request.form.get('question_id'))
    question_text = request.form.get('question')
    category = request.form.get('category')
    options = [
        request.form.get('option1'),
        request.form.get('option2'),
        request.form.get('option3'),
        request.form.get('option4')
    ]
    correct_index = int(request.form.get('correct'))
    
    # Update the question
    questions[question_id]['question'] = question_text
    questions[question_id]['options'] = options
    questions[question_id]['answer'] = options[correct_index]
    
    # Save questions to a file (optional)
    # with open('questions.json', 'w') as f:
    #     json.dump(questions, f)
    
    return redirect(url_for('admin_questions'))

@app.route('/admin/questions/delete', methods=['POST'])
@admin_required
def admin_delete_question():
    question_id = int(request.form.get('question_id'))
    
    # In a real app with a database, you would delete from the database
    # For this example, we'll just remove it from the list
    if 0 <= question_id < len(questions):
        questions.pop(question_id)
    
    # Save questions to a file (optional)
    # with open('questions.json', 'w') as f:
    #     json.dump(questions, f)
    
    return redirect(url_for('admin_questions'))

if __name__ == '__main__':
    app.run(debug=True)