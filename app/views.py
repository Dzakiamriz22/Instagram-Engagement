# views.py

from flask import Blueprint, render_template, request
from .instaloader_script import calculate_engagement

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    engagement_data = None
    error_message = None

    if request.method == 'POST':
        username = request.form['username']
        engagement_data = calculate_engagement(username)

        if engagement_data and "error" in engagement_data:
            error_type = engagement_data["error"]
            if error_type == "The username was not found.":
                error_message = "Username tidak diketahui."
            elif error_type == "The account is private.":
                error_message = "Profil ini bersifat privat."
            elif error_type == "Cannot calculate engagement due to zero division.":
                error_message = "Tidak dapat menghitung engagement karena pembagian dengan nol."
            else:
                error_message = "Terjadi kesalahan: " + error_type
            engagement_data = None

    return render_template('index.html', engagement_data=engagement_data, error_message=error_message)
