class MusicLibrary:
    def __init__(self):
        self.song_list = []

    def add(self, song_name):
        return self.song_list.append(song_name)

    def all(self):
        return self.song_list

    def remove(self, number):
        try:
            return self.song_list.pop(number)
        except IndexError:
            return None

from dataclasses import dataclass

@dataclass
class Track:
    title: str
    artist: str
    file: str