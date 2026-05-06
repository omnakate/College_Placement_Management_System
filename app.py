import os

from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# 🔐 Railway MySQL Config
app.config['MYSQL_HOST'] = os.environ.get('shinkansen.proxy.rlwy.net')
app.config['MYSQL_USER'] = os.environ.get('root')
app.config['MYSQL_PASSWORD'] = os.environ.get('ASDCCgQngQSaonnZIxIXgAdesaLHOPGN')
app.config['MYSQL_DB'] = os.environ.get('railway')
app.config['MYSQL_PORT'] = int(os.environ.get('10351'))

app.secret_key = os.environ.get('SECRET_KEY', 'dev_secret_key')

mysql = MySQL(app)

# ✅ Import Blueprints
from routes.admin_routes import admin_bp
from routes.student_routes import student_bp
from routes.student_auth import student_auth_bp

# ✅ Register Blueprints
app.register_blueprint(admin_bp)
app.register_blueprint(student_bp)
app.register_blueprint(student_auth_bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)