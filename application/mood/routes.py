from flask import Blueprint, render_template

mood_bp = Blueprint('mood', __name__)

@mood_bp.route('/')
def index():
    return render_template('mood/calendar.html')