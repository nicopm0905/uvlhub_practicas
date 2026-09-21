from flask import render_template
from app.features.notepad import notepad_bp


@notepad_bp.route('/notepad', methods=['GET'])
def index():
    return render_template('notepad/index.html')
