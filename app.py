import os

from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# 🔐 MySQL Config
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', '')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'campus_db')
app.config['MYSQL_PORT'] = int(os.environ.get('MYSQL_PORT', 3306))
app.secret_key = os.environ.get('SECRET_KEY', 'dev_secret_key')

mysql = MySQL(app)

# ✅ Import Blueprints (NOT *)
from routes.admin_routes import admin_bp
from routes.student_routes import student_bp

# ✅ Register Blueprints
app.register_blueprint(admin_bp)
app.register_blueprint(student_bp)


from routes.student_auth import student_auth_bp
app.register_blueprint(student_auth_bp)

if __name__ == "__main__":
    app.run(debug=True)
