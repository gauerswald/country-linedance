from app import db

class Linedance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song = db.Column(db.String(100), nullable=False)
    interpret = db.Column(db.String(100), nullable=False)
    dance = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Linedance {self.song}>'

# Initialize the database (run this once to create the tables)
db.create_all()
