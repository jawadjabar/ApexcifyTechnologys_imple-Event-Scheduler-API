from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from datetime import datetime
from app.extensions import db
from app.models import Event

events_bp = Blueprint('events', __name__)

# Main events listing (GET only)
@events_bp.route('/', methods=['GET'])
def events():
    events = Event.query.order_by(Event.date).all()
    return render_template('events.html', events=events)

# Create event form (GET only)
@events_bp.route('/create', methods=['GET'])
def create_event():
    return render_template('create_event.html')

# Handle form submission (POST only)
@events_bp.route('/create', methods=['POST'])
def add_event():
    title = request.form.get('title')
    date_str = request.form.get('date')
    description = request.form.get('description')

    try:
        event_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        if event_date < datetime.today().date():
            flash('Date cannot be in the past', 'danger')
            return redirect(url_for('events.create_event'))

        new_event = Event(
            title=title,
            date=event_date,
            description=description
        )
        db.session.add(new_event)
        db.session.commit()

        flash('Event created successfully!', 'success')
        return redirect(url_for('events.events'))

    except ValueError:
        flash('Invalid date format', 'danger')
        return redirect(url_for('events.create_event'))