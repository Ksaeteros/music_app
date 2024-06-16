import sys
import os

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request
from client.client import get_song

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    song = None
    if request.method == 'POST':
        song_name = request.form['song_name']
        song = get_song(song_name)
    return render_template('index.html', song=song)

if __name__ == '__main__':
    app.run(debug=True)
