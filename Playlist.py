from tabulate import tabulate
from random import randint
import json


class Playlist:
    def __init__(self, name, repeat=False, shuffle=False):
        self._name = name
        self._repeat = repeat
        self._shuffle = shuffle
        self._songs = []
        self._song_index = 0
        self._played = []

    def add_song(self, song):
        self._songs.append(song)

    def remove_song(self, song):
        self._songs.remove(song)

    def add_songs(self, songs):
        self._songs += songs

    def get_songs(self):
        return self._songs

    def total_lenght(self):
        pass

    def artists(self):
        artists = {}
        for song in self._songs:
            if artists[song._artist]:
                artists[song._artist] += 1
            else:
                artists[song._artist] = 0
        return str(artists)

    def next_song(self):
        if self._repeat and self._song_index >= len(self._songs):
            self._song_index = 0
        song = self._songs[self._song_index]
        self._song_index += 1
        return song

    def pprint_playlist(self):
        return tabulate(headers=["Artist", "Song", "Lenght"])

    def get_dict(self):
        songs_dict = []
        for song in self._songs:
            songs_dict.append(song.__dict__)
        result = {
                'name': self._name,
                'repeat': self._repeat,
                'shuffle': self._shuffle,
                'song_index': self._song_index,
                'songs': songs_dict,
        }
        return result

    def save(self, filename):
        with open(filename, 'w') as f:
            json.dumps(self.get_dict(), f, indent=4)

    def load(self, filename):
        with open(filename, 'r') as f:
            data_d = json.load(f)
        return data_d

    def load_from_dict(self, data_d):
        playlist = Playlist("Name")
        songs = data_d.pop('songs')
        playlist.__dict__ = data_d
        for song in songs:
            newsong = Song()
            newsong .__dict__ = song
            playlist.add_song(newsong)
        return playlist
