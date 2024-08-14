from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from sqlalchemy import func
from . import db
from .instaloader_script import calculate_engagement

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def landing():
    return render_template('landing.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password']
        full_name = request.form['full_name']
        email = request.form['email']

        if not email:
            flash('Email is required', 'danger')
            return redirect(url_for('main.register'))

        existing_user = User.query.filter(func.lower(User.username) == username).first()
        if existing_user:
            flash('Username already exists', 'danger')
            return redirect(url_for('main.register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password, full_name=full_name, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('main.login'))

    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password']

        user = User.query.filter(func.lower(User.username) == username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = username
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

@main.route('/index', methods=['GET', 'POST'])
def index():
    if 'username' not in session:
        return redirect(url_for('main.landing'))

    current_user = User.query.filter_by(username=session['username']).first()
    print(f'Current User: {current_user}')  # Debug print

    engagement_data = None
    error_message = None

    if request.method == 'POST':
        username = request.form['username']
        engagement_data = calculate_engagement(username)

        if engagement_data and "error" in engagement_data:
            error_type = engagement_data["error"]
            error_message = {
                "The username was not found.": "Username tidak ditemukan.",
                "The account is private.": "Profil ini bersifat privat.",
                "Cannot calculate engagement due to zero division.": "Tidak dapat menghitung engagement karena pembagian dengan nol.",
                "Connection error occurred.": "Terjadi kesalahan koneksi. Silakan coba lagi nanti.",
                "Bad credentials.": "Kredensial buruk. Silakan cek kredensial Anda.",
                "Login required.": "Login diperlukan untuk mengakses data ini."
            }.get(error_type, "Terjadi kesalahan: " + error_type)
            engagement_data = None

    return render_template('index.html', engagement_data=engagement_data, error_message=error_message, current_user=current_user)

@main.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('main.landing'))

@main.route('/get-started', methods=['GET'])
def get_started():
    return redirect(url_for('main.login'))

@main.after_request
def add_header(response):
    response.cache_control.no_store = True
    response.cache_control.no_cache = True
    response.cache_control.must_revalidate = True
    return response