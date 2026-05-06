from flask import Blueprint, render_template, session

student_bp = Blueprint('student', __name__)

# ⚠️ Import mysql from app (lazy import to avoid circular issue)
def get_mysql():
    from app import mysql
    return mysql

@student_bp.route('/')
def index():
    mysql = get_mysql()
    cur = mysql.connection.cursor()

    cur.execute("""
    SELECT * FROM companies
    WHERE deadline >= NOW()
    ORDER BY drive_date ASC
    """)
    data = cur.fetchall()

    updated_data = []

    for c in data:
        status = "Login Required"

        if 'student_id' in session:
            if (
                session['student_cgpa'] >= c[4] and
                session['student_backlogs'] <= c[6] and
                session['student_branch'] in c[5]
            ):
                status = "Eligible"
            else:
                status = "Not Eligible"

        updated_data.append(list(c) + [status])

    return render_template('index.html', companies=updated_data)