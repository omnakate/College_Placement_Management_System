from flask import Blueprint, render_template, request, redirect, session, url_for
from werkzeug.security import check_password_hash

admin_bp = Blueprint('admin', __name__)


def get_mysql():
    from app import mysql
    return mysql


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Show the login page before allowing access to the admin panel."""
    if 'admin' in session:
        return redirect(url_for('admin.admin_dashboard'))

    error = None

    if request.method == 'POST':
        mysql = get_mysql()
        cur = mysql.connection.cursor()

        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        try:
            cur.execute("SELECT * FROM admins WHERE username=%s", (username,))
        except Exception as e:
            return f"Database Error: {e}"
        admin = cur.fetchone()
        cur.close()

        if admin:
            stored_password = admin[2]
            if stored_password.startswith(('pbkdf2:', 'scrypt:', 'argon2:')):
                valid_login = check_password_hash(stored_password, password)
            else:
                valid_login = stored_password == password

            if valid_login:
                session['admin'] = username
                return redirect(url_for('admin.admin_dashboard'))

        error = "Invalid username or password"

    return render_template('login.html', error=error)


@admin_bp.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('admin.login'))


@admin_bp.route('/admin')
def admin_dashboard():
    if 'admin' not in session:
        return redirect(url_for('admin.login'))

    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM companies")
    data = cur.fetchall()
    cur.close()

    return render_template('admin.html', companies=data)


@admin_bp.route('/add_company', methods=['POST'])
def add_company():
    if 'admin' not in session:
        return redirect(url_for('admin.login'))

    mysql = get_mysql()
    data = request.form
    cur = mysql.connection.cursor()

    cur.execute("""
        INSERT INTO companies
        (company_name, job_role, ctc, cgpa, branches, backlogs, deadline, drive_date, reporting_time, venue, google_form_link)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        data['company_name'], data['job_role'], data['ctc'],
        data['cgpa'], data['branches'], data['backlogs'],
        data['deadline'], data['drive_date'], data['reporting_time'],
        data['venue'], data['google_form_link']
    ))

    mysql.connection.commit()
    cur.close()
    return redirect(url_for('admin.admin_dashboard'))


@admin_bp.route('/delete/<int:id>')
def delete_company(id):
    if 'admin' not in session:
        return redirect(url_for('admin.login'))

    mysql = get_mysql()
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM companies WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('admin.admin_dashboard'))

# 🔹 LOAD EDIT PAGE
@admin_bp.route('/edit/<int:id>')
def edit_company(id):
    if 'admin' not in session:
        return redirect(url_for('admin.login'))

    mysql = get_mysql()
    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM companies WHERE id=%s", (id,))
    company = cur.fetchone()
    cur.close()

    return render_template('edit_company.html', company=company)


# 🔹 UPDATE COMPANY
@admin_bp.route('/update/<int:id>', methods=['POST'])
def update_company(id):
    if 'admin' not in session:
        return redirect(url_for('admin.login'))

    mysql = get_mysql()
    data = request.form
    cur = mysql.connection.cursor()

    cur.execute("""
        UPDATE companies SET
        company_name=%s,
        job_role=%s,
        ctc=%s,
        cgpa=%s,
        branches=%s,
        backlogs=%s,
        deadline=%s,
        drive_date=%s,
        reporting_time=%s,
        venue=%s,
        google_form_link=%s
        WHERE id=%s
    """, (
        data['company_name'], data['job_role'], data['ctc'],
        data['cgpa'], data['branches'], data['backlogs'],
        data['deadline'], data['drive_date'], data['reporting_time'],
        data['venue'], data['google_form_link'],
        id
    ))

    mysql.connection.commit()
    cur.close()

    return redirect(url_for('admin.admin_dashboard'))
