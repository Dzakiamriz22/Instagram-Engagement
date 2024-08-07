from flask import Blueprint, render_template, request
from .instaloader_script import calculate_engagement

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def landing():
    return render_template('landing.html')

@main.route('/index', methods=['GET', 'POST'])
def index():
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

    return render_template('index.html', engagement_data=engagement_data, error_message=error_message)
