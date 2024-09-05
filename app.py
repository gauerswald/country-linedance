from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# PostgreSQL Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/country_linedance_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import the models
from models import Linedance


@app.route('/')
def index():
    linedances = Linedance.query.all()
    return render_template('index.html', linedances=linedances)

@app.route('/add', methods=['GET', 'POST'])
def add_dance():
    if request.method == 'POST':
        song = request.form['song']
        interpret = request.form['interpret']
        dance = request.form['dance']
        description = request.form['description']

        new_dance = Linedance(song=song, interpret=interpret, dance=dance, description=description)
        db.session.add(new_dance)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_dance.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_dance(id):
    dance = Linedance.query.get(id)
    if request.method == 'POST':
        dance.song = request.form['song']
        dance.interpret = request.form['interpret']
        dance.dance = request.form['dance']
        dance.description = request.form['description']

        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit_dance.html', dance=dance)

@app.route('/delete/<int:id>')
def delete_dance(id):
    dance = Linedance.query.get(id)
    db.session.delete(dance)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
