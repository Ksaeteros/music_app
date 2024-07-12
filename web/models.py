from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin  
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password_hash = db.Column(db.String(500), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

class Playlist(db.Model):
    __tablename__ = 'playlist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('usuario.id'), nullable=False)  # Nueva columna
    songs = db.relationship('Song', backref='playlist', lazy=True)
    user = db.relationship('User', backref=db.backref('playlists', lazy=True))  # Relación con User


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(150), nullable=False)
    artist = db.Column(db.String(150), nullable=False)
    album = db.Column(db.String(150), nullable=False)
    album_image = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)  # URL de la canción
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)

