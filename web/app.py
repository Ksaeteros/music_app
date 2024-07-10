import sys
import os

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, flash, render_template, request, redirect, send_from_directory, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from client.client import get_song, get_featured_albums
from web.models import User, db, Playlist, Song

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/music_app'  # Actualiza con tus credenciales
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    song = None
    albums = get_featured_albums()  # Obtenemos los álbumes destacados desde Spotify

    if request.method == 'POST':
        song_name = request.form['song_name']
        song = get_song(song_name)

    return render_template('index.html', song=song, albums=albums)


#Añadir funcionalidad para obtener una música
@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    song = None
    if request.method == 'POST':
        song_name = request.form['song_name']
        song = get_song(song_name)
    return render_template('search.html', song=song)

#Añadir funcionalidad para dar like a una música
@app.route('/like', methods=['POST'])
@login_required
def like():
    song_data = request.form
    playlist = Playlist.query.filter_by(user_id=current_user.id).first()
    if not playlist:
        playlist = Playlist(name="My Playlist", user_id=current_user.id)
        db.session.add(playlist)
        db.session.commit()

    new_song = Song(
        song_name=song_data['song_name'],
        artist=song_data['artist'],
        album=song_data['album'],
        album_image=song_data['album_image'],
        url=song_data['url'],
        playlist=playlist
    )
    db.session.add(new_song)
    db.session.commit()
    return redirect(url_for('index'))

#Funcionalidad para mostrar el playlist de músicas
@app.route('/playlist')
@login_required
def playlist():
    playlist = Playlist.query.filter_by(user_id=current_user.id).first()
    songs = playlist.songs if playlist else []
    return render_template('playlist.html', songs=songs)

#Funcionalidad para el inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
        elif User.query.filter_by(email=email).first():
            flash('Email already registered')
        else:
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash('Registration successful, please log in.')
            return redirect(url_for('login'))
    return render_template('register.html')

#Funcionalidad para eliminar una música
@app.route('/delete/<int:song_id>', methods=['POST'])
@login_required
def delete_song(song_id):
    song = Song.query.get_or_404(song_id)
    if song.playlist.user_id == current_user.id:  # Verificar que la canción pertenece al usuario
        db.session.delete(song)
        db.session.commit()
    return redirect(url_for('playlist'))

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

