from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from application import db
from application.models import MoodEntry
from application.mood.forms import MoodForm
from datetime import date, timedelta

mood_bp = Blueprint('mood', __name__)

@mood_bp.route('/')
def landing():
    return render_template('landing.html')

@mood_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('mood/dashboard.html', username=current_user.username)

@mood_bp.route('/log', methods=['GET', 'POST'])
@login_required
def log_mood():
    form = MoodForm()
    if form.validate_on_submit():
        mood_entry = MoodEntry(
            mood=form.mood.data,
            intensity=form.intensity.data,
            tags=form.tags.data,
            notes=form.notes.data,
            user_id=current_user.id
        )
        db.session.add(mood_entry)
        db.session.commit()
        flash('✅ Mood logged successfully!', 'success')
        return redirect(url_for('mood.dashboard'))
    return render_template('mood/log_mood.html', form=form)



@mood_bp.route('/heatmap')
@login_required
def heatmap():
    entries = MoodEntry.query.filter_by(user_id=current_user.id).all()
    mood_data = {entry.date.strftime('%Y-%m-%d'): entry.mood for entry in entries}
    return render_template('mood/heatmap.html', mood_data=mood_data)

@mood_bp.route('/triggers')
@login_required
def triggers():
    return "<h1>Triggers Page (Coming Soon)</h1>"