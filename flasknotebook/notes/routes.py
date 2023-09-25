from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from flasknotebook import db
from flasknotebook.models import Note
from flasknotebook.notes.forms import NoteForm

notes = Blueprint('notes', __name__)

@notes.route("/note/new", methods=['GET', 'POST'])
@login_required
def new_note():
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(note)
        db.session.commit()
        flash('Twoja notatka została zapisana!', 'succes')
        return redirect(url_for('users.user_notes', username=note.author.username))
    return render_template('create_note.html', title='Nowa notatka', form=form, legend='Nowa notatka')

@notes.route("/note/<int:note_id>")
def note(note_id):
    note = Note.query.get_or_404(note_id)
    return render_template('note.html', title=note.title, note=note)

@notes.route("/note/<int:note_id>/update", methods=['GET', 'POST'])
@login_required
def update_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.author != current_user:
        abort(403)
    form = NoteForm()
    if form.validate_on_submit():
        note.title = form.title.data
        note.content = form.content.data
        db.session.commit()
        flash('Twoja notatka została zaktualizowana!', 'success')
        return redirect(url_for('notes.note', note_id=note.id))
    elif request.method == 'GET':
        form.title.data = note.title
        form.content.data = note.content
    return render_template('create_note.html', title='Zaktualizuj notatkę', form=form, legend='Zaktualizuj notatkę')

@notes.route("/note/<int:note_id>/delete", methods=['POST'])
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.author != current_user:
        abort(403)
    db.session.delete(note)
    db.session.commit()
    flash('Twoja notatka została usunięta!', 'succes')
    return redirect(url_for('main.home'))
