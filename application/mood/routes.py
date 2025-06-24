from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from application import db
from application.models import MoodEntry
from application.mood.forms import MoodForm
from datetime import date, timedelta , datetime
from sqlalchemy import or_, and_
from application.mood.nlp_utils import extract_keyphrases
from collections import Counter


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
    six_months_ago = date.today() - timedelta(days=182)
    entries = MoodEntry.query.filter(
        MoodEntry.user_id == current_user.id,
        MoodEntry.date >= six_months_ago
    ).all()

    mood_data = {e.date.isoformat(): e.mood for e in entries}
    mood_colors = {
        'Happy': '#28a745', 'Sad': '#6c757d', 'Angry': '#dc3545',
        'Anxious': '#fd7e14', 'Neutral': '#17a2b8', 'Excited': '#ffc107',
        'Depressed': '#343a40', 'Stressed': '#e83e8c', 'Calm': '#20c997',
        'Lonely': '#6f42c1', 'Frustrated': '#ff4c4c', 'Bored': '#adb5bd',
        'Hopeful': '#00bcd4', 'Grateful': '#9ccc65', 'Tired': '#a1887f'
    }

    return render_template(
        'mood/heatmap.html',
        mood_data=mood_data,
        mood_colors=mood_colors
    )

@mood_bp.route('/triggers')
@login_required
def triggers():
    moods = MoodEntry.query.filter_by(user_id=current_user.id).all()
    
    negative_moods = ['Sad', 'Anxious', 'Depressed', 'Frustrated', 'Stressed', 'Lonely']
    phrases = []

    for mood in moods:
        if mood.mood in negative_moods and mood.notes:
            phrases.extend(extract_keyphrases(mood.notes))

    most_common = Counter(phrases).most_common(10)

    return render_template('mood/triggers.html', triggers=most_common)

@mood_bp.route('/history')
@login_required
def mood_history():
    query = MoodEntry.query.filter_by(user_id=current_user.id)

    search = request.args.get('search')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    sort_by = request.args.get('sort_by', 'date')  # default: date
    order = request.args.get('order', 'desc')

    if search:
        query = query.filter(or_(
            MoodEntry.notes.ilike(f'%{search}%'),
            MoodEntry.tags.ilike(f'%{search}%'),
            MoodEntry.mood.ilike(f'%{search}%')
        ))

    if start_date:
        try:
            start = datetime.strptime(start_date, '%Y-%m-%d')
            query = query.filter(MoodEntry.date >= start)
        except:
            pass

    if end_date:
        try:
            end = datetime.strptime(end_date, '%Y-%m-%d')
            query = query.filter(MoodEntry.date <= end)
        except:
            pass


    sort_attr = getattr(MoodEntry, sort_by, MoodEntry.date)
    if order == 'asc':
        query = query.order_by(sort_attr.asc())
    else:
        query = query.order_by(sort_attr.desc())

    entries = query.all()
    return render_template('mood/history.html', entries=entries)