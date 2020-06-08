from datetime import datetime
from flask import redirect, url_for, flash, render_template
from flask_login import current_user

from . import teacher

from ._teacher import Teacher
from .forms import NewAssignmentForm

from app.decorators import required_access
from app.modules._classes import Assignment


@teacher.before_request
@required_access('Teacher')
def teacher_verification():
    # Required_access decorator already handled it
    return True


@teacher.route('/add_assignment', methods=['GET', 'POST'])
def add_assignment():
    form = NewAssignmentForm()

    if form.validate_on_submit():
        new_assignment = Assignment(date_assigned=datetime.utcnow(),
                                    assigned_by=current_user.ID,
                                    assigned_to=form.assigned_to.data,
                                    due_by=form.due_by.data,
                                    subject=form.subject.data,
                                    content=form.content.data,
                                    estimated_time=form.estimated_time.data
                                    )

        if new_assignment.add():
            return(redirect(url_for('main.dashboard')))
        else:
            flash('Unknown error!.')

    return render_template('add_assignment.html', form=form)