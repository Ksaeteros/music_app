import tkinter as tk
from tkinter import messagebox
from client import get_song

def search_song():
    song_name = entry.get()
    song = get_song(song_name)
    if song:
        messagebox.showinfo("Song Info", f'Song: {song.song_name}\nArtist: {song.artist}\nAlbum: {song.album}\nURL: {song.url}')
    else:
        messagebox.showerror("Error", "Song not found")

root = tk.Tk()
root.title("Music Client")

label = tk.Label(root, text="Enter Song Name:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text="Search", command=search_song)
button.pack(pady=10)

root.mainloop()
