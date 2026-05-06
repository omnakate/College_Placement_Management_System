from flask import Blueprint, render_template, request, redirect, url_for, session

student_auth_bp = Blueprint('student_auth', __name__, url_prefix='/student')

def get_mysql():
    from app import mysql
    return mysql


# 🔹 REGISTER
@student_auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        mysql = get_mysql()
        data = request.form
        cur = mysql.connection.cursor()

        cur.execute(
            "INSERT INTO students (name, email, password) VALUES (%s,%s,%s)",
            (data['name'], data['email'], data['password'])
        )
        mysql.connection.commit()

        return redirect('/student/login')

    return render_template('student_register.html')


# 🔹 LOGIN
@student_auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mysql = get_mysql()
        data = request.form
        cur = mysql.connection.cursor()

        cur.execute(
            "SELECT * FROM students WHERE email=%s AND password=%s",
            (data['email'], data['password'])
        )
        student = cur.fetchone()

        if student:
            session['student_id'] = student[0]
            session['student_name'] = student[1]
            session['student_email'] = student[2]

            # Temporary default values
            session['student_cgpa'] = 7.0
            session['student_branch'] = "CSE"
            session['student_backlogs'] = 0

            return redirect('/')
        else:
            return render_template('student_login.html', error="Invalid Credentials")
    return render_template('student_login.html')


# 🔹 LOGOUT
@student_auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')